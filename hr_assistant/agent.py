# step 7 : build the agent that ties the llm and search tool together

from langchain.agents import create_agent
from hr_assistant import config

def create_hr_agent(llm, tools):
    return create_agent(model=llm, 
                        tools = tools, 
                        system_prompt= config.SYSTEM_PROMPT)

