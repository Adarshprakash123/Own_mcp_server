from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent
from langchain_groq import ChatGroq

from dotenv import load_dotenv
load_dotenv()

import asyncio
async def main():
    client=MultiServerMCPClient(
        {
            "math":{
                "command":"python",
                "args":["mathmcpserver.py"],
                "transport":"stdio"
            }
        }
    )
    import os
    os.environ["GROQ_API_KEY"]=os.getenv("GROQ_API_KEY")
    tools=await client.get_tools()
    model=ChatGroq(model="qwen-qwq-32b")
    agent=create_react_agent(
        model,tools
    )
    math_response=await agent.ainvoke(
        {"messages":[{
            "role":"user",
            "content":"what is (3+5)*12"
        }]}
    )
    print("Full response:", math_response)
    print("Response type:", type(math_response))

    # Convert to standard dict
    response_dict =  dict(math_response)

    # Access messages safely
    last_message = response_dict["messages"][-1]
    print("Final Answer:", last_message.content)
    print("Response keys:", response_dict.keys())

asyncio.run(main())