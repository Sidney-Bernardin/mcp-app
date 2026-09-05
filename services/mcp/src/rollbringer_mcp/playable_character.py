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

    row = await ctx.request_context.lifespan_context.pg.fetchrow(
        """
        SELECT * FROM
        playable_characters
        WHERE name = '$1'
        """,
        name,
    )

    return str(row)


@mcp.tool(title="Update Playable Character")
async def update_pc(ctx: Context, pc_id: str):
    """Add two numbers."""
    await ctx.notify_resource_updated(f"characters://playable/{pc_id}")
