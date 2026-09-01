from mcp.server import MCPServer

mcp = MCPServer("Demo")


@mcp.tool()
def add(a: int, b: int):
    """Add two numbers."""
    return a + b


@mcp.resource("greeting://{name}")
def greeting(name):
    """Greet someone by name."""
    return f"Hello, {name}!"


@mcp.prompt()
def summarize(text: str):
    return f"Summarize this text in one sentance:\n\n{text}"
