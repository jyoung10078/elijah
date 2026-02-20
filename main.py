from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_core.output_parsers import PydanticOutputParser
from langchain.agents import create_agent
from langchain_core.messages import AIMessage
from tools import search_tool, wiki_tool, save_tool

load_dotenv()

class ResearchResponse(BaseModel):
    topic: str
    summary: str
    sources: list[str]
    tools_used: list[str]


parser = PydanticOutputParser(pydantic_object=ResearchResponse)
format_instructions = parser.get_format_instructions()

system_prompt = f"""You are a research assistant that will help generate a research paper.
Answer the user query and use necessary tools.
Wrap the output in this format and provide no other text:
{format_instructions}"""

tools = [search_tool, wiki_tool, save_tool]
agent = create_agent(
    model="claude-sonnet-4-6",
    tools=tools,
    system_prompt=system_prompt,
    debug=True,
)

query = input("What can I help you research? ")
raw_response = agent.invoke({"messages": [{"role": "user", "content": query}]})

# Extract the final AI message content from the response
messages = raw_response.get("messages", [])
last_ai_content = ""
for msg in reversed(messages):
    if isinstance(msg, AIMessage) and msg.content:
        last_ai_content = msg.content if isinstance(msg.content, str) else ""
        break
    if isinstance(msg, dict) and msg.get("type") == "ai" and msg.get("content"):
        last_ai_content = msg["content"] if isinstance(msg["content"], str) else ""
        break

try:
    structured_response = parser.parse(last_ai_content)
    print(structured_response)
except Exception as e:
    print("Error parsing response:", e, "Raw content:", last_ai_content or raw_response)
