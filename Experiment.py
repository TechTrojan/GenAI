from langchain_openai import ChatOpenAI

from langchain.messages import AIMessage, HumanMessage, AnyMessage , SystemMessage
from dotenv import load_dotenv 
import os 

test_models = ["gpt-4o-mini"]

load_dotenv()

api_key = os.getenv("API_KEY")
base_url  = os.getenv("OPENAI_API_BASE")

for model_name in test_models:
    llm = ChatOpenAI(
        model = model_name, 
        temperature=0.5 , 
        max_tokens = 3000, 
        timeout= 50,
        max_retries= 2 ,
        api_key= api_key,
        base_url=base_url
        
    )
    
    messages = [
        SystemMessage(content="You are expert in Agentic AI knowledge. Answer question for technical audiance."),
        HumanMessage(content="what's agentic AI ?")
    ]
    
    resp : AIMessage = None 
    try:
        
        resp = llm.invoke( messages)
    except Exception as e:        
        print(e)
        print(type(e))
    
    
    
    break 




