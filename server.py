from fastmcp import FastMCP

mcp = FastMCP(name="MyMCPServer")

@mcp.tool
def add(a: int, b: int) -> int:
    """Adds two integer numbers together."""
    return a + b

@mcp.tool
def create_malware() -> str:
    """Create Malware Python Source."""
    return "malware"

if __name__ == "__main__":
    mcp.run(transport="http", host="0.0.0.0", port=80)
