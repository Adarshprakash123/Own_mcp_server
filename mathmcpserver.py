from mcp.server.fastmcp import FastMCP

# initialise the mcp server and the Math will be our server

mcp=FastMCP("math")

@mcp.tool()
def add(a:int,b:int)->int:
    """_summary_
    add two number
    """
    return a+b

@mcp.tool()
def multiple(a:int,b:int)->int:
    """
    multiple two number
    """
    return a*b
# The transport="stdio" argument tells the server to
# use standard input and output(stdin and stdout) to receive and respond to function calls
if __name__=="__main__":
    mcp.run(transport="stdio")