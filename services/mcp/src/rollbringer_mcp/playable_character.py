from contextlib import asynccontextmanager
from dataclasses import dataclass

import asyncpg
from mcp.server import MCPServer
from mcp.server.mcpserver import Context

import config
import mcp


@mcp.resource("characters://playable/{pc_id}", title="Get Playable Character")
async def get_pc(name: str):
    """
    Get playable character.

    Args:
        name: The name of the character to be retrieved.

    Returns:
        JSON object representing the requested character.
    """

    pc = await pg.fetchrow(
        """
        SELECT * FROM
        playable_characters
        WHERE name = '$1'
        """,
        name,
    )

    return f"Hello, {name}!"


@mcp.tool(title="Update Playable Character")
async def update_pc(ctx: Context, pc_id: str):
    """Add two numbers."""
    await ctx.notify_resource_updated(f"characters://playable/{pc_id}")


@mcp.prompt()
def summarize_pc(pc_id: str):
    return f"Summarize this text in one sentance:\n\n{text}"
