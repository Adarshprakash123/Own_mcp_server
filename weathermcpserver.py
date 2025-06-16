from mcp.server.fastmcp import FastMCP

mcp=FastMCP("weather")

@mcp.tool()
async def weather(location:str)->str:
    """
    Get the weather for a given location
    """
    return  "The weather in {location} is sunny"

if __name__=="__main__":
    mcp.run(transport="streamable-http")