from contextlib import asynccontextmanager
from dataclasses import dataclass

import asyncpg
from mcp.server import MCPServer
from mcp.server.mcpserver import Context

import config


@dataclass
class LifespanContext:
    pg: asyncpg.Pool


async def init_connection(conn: asyncpg.Connection):
    await conn.set_builtin_type_codec("hstore", codec_name="pg_contrib.hstore")


@asynccontextmanager
async def lifespan(mcp: MCPServer):
    async with asyncpg.create_pool(config.PG_URL, init=init_connection) as pg:
        yield LifespanContext(pg=pg)


mcp = MCPServer("Demo", lifespan=lifespan)


if __name__ == "__main__":
    mcp.run()
