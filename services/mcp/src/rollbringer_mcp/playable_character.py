from typing import cast

from asyncpg import Connection
from mcp.server.mcpserver import Context

from rollbringer_mcp.main import LifespanContext, mcp


@mcp.resource("characters://playable/{pc_id}", title="Get Playable Character")
async def get_pc(ctx: Context[LifespanContext], name: str):
    """
    Get playable character.

    Args:
        name: The name of the character to be retrieved.

    Returns:
        JSON object representing the requested character.
    """

    async with ctx.request_context.lifespan_context.pg.acquire() as _conn:
        conn = cast(Connection, _conn)
        async with conn.transaction():
            pass


@mcp.tool(title="Update Playable Character")
async def update_pc(ctx: Context, pc_id: str):
    """Add two numbers."""
    await ctx.notify_resource_updated(f"characters://playable/{pc_id}")
