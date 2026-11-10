from contextlib import asynccontextmanager
from dataclasses import dataclass
from typing import cast

import asyncpg
from domain import aggregates, config
from mcp.server import MCPServer
from mcp.server.mcpserver import Context


@dataclass
class LifespanContext:
    pg: asyncpg.Pool


@asynccontextmanager
async def lifespan(mcp: MCPServer):
    async with asyncpg.create_pool(config.PG_URL) as pg:
        yield LifespanContext(pg=pg)


mcp = MCPServer("Demo", lifespan=lifespan, log_level="DEBUG")


@mcp.tool(title="Create Playable Character")
async def create_pc(
    ctx: Context,
    character_sheet: aggregates.CharacterSheetBody,
):
    """
    Create a new character sheet.

    Args:
        character_sheet: Fields for the character sheet.
    """

    async with (
        ctx.request_context.lifespan_context["pg"].acquire() as conn,
        conn.transaction(),
    ):
        await playable_characters.insert(conn, playable_character)


@mcp.resource("characters://playable/{pc_id}", title="Get Playable Character")
async def get_pc(
    ctx: Context[LifespanContext], pc_id: int
) -> aggregates.PlayableCharacter | None:
    """
    Get playable character.

    Args:
        name: The name of the character to be retrieved.

    Returns:
        JSON object representing the requested character.
    """

    async with ctx.request_context.lifespan_context.pg.acquire() as _conn:
        conn = cast(asyncpg.Connection, _conn)
        async with conn.transaction():
            return await aggregates.PlayableCharacter.get(conn, pc_id)


# @mcp.tool(title="Update Playable Character")
# async def update_pc(ctx: Context, pc_id: str):
#     await ctx.notify_resource_updated(f"characters://playable/{pc_id}")
