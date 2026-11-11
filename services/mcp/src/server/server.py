import logging
from contextlib import asynccontextmanager
from dataclasses import dataclass
from typing import cast

import asyncpg
from domain import aggregates, config
from domain.repositories.postgres import character_sheets
from mcp.server import MCPServer
from mcp.server.mcpserver import Context

logging.basicConfig(format="%(levelname)s: %(message)s")
logger = logging.getLogger(__name__)


@dataclass
class LifespanContext:
    pg: asyncpg.Pool


@asynccontextmanager
async def lifespan(mcp: MCPServer):
    async with asyncpg.create_pool(config.PG_URL) as pg:
        yield LifespanContext(pg=pg)


mcp = MCPServer("Demo", lifespan=lifespan, log_level="DEBUG")


@mcp.tool(title="Create Character Sheet")
async def create_pc(
    ctx: Context[LifespanContext],
    character_sheet: aggregates.CharacterSheetBody,
):
    """
    Create a new character sheet.

    Args:
        character_sheet: Fields for the character sheet.

    Returns:
        If of the new character sheet.
    """

    async with (
        ctx.request_context.lifespan_context.pg.acquire() as conn,
        conn.transaction(),
    ):
        await character_sheets.insert(conn, character_sheet)
        return


@mcp.resource("characters://playable/{pc_id}", title="Get Character Sheet")
async def get_pc(ctx: Context, pc_id: int) -> aggregates.CharacterSheet | None:
    """
    Get character sheet.

    Args:
        name: The name of the character sheet to be retrieved.

    Returns:
        JSON object representing the requested character sheet.
    """

    lifespan = cast(LifespanContext, ctx.request_context.lifespan_context)

    async with lifespan.pg.acquire() as _conn:
        conn = cast(asyncpg.Connection, _conn)
        async with conn.transaction():
            return await character_sheets.select(conn, pc_id)


@mcp.tool(title="Update Character Sheet")
async def update_pc(
    ctx: Context[LifespanContext],
    pc_id: int,
    update: aggregates.PartialCharacterSheet,
):
    """
    Update character sheet.

    Args:
        pc_id: The name of the character sheet to be updated.
    """

    async with (
        ctx.request_context.lifespan_context.pg.acquire() as conn,
        conn.transaction(),
    ):
        await character_sheets.update(conn, pc_id, update)
        await ctx.notify_resource_updated(f"characters://playable/{pc_id}")
