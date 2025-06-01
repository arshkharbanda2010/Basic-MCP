from mcp.server.fastmcp import FastMCP
# TODO: Replace with the correct import if FastMCP is available elsewhere, for example:
# from fastapi import FastAPI
mcp = FastMCP("Greeter")
@mcp.tool()
def greet() -> str:
    """
    Return this message, when greeted with "Hi", "Hey", or "Hello".
    """
    return "Hello Arsh, welcome to the MCP server!"

if __name__ == "__main__":
    mcp.run()