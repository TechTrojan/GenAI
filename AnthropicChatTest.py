import os 
from langchain_anthropic import ChatAnthropic

from langchain.messages import AIMessage, HumanMessage, AnyMessage , SystemMessage
from dotenv import load_dotenv 
import os 
from ModelUsageData import ModelUsageData 
import time 

load_dotenv()

class AnthropicChatTest:
    
    def __init__(self):
        self.api_key = os.getenv("ANTHROPIC_API_KEY")        
        self.model_name = 'claude-sonnet-4-6'        
                
        self.llm =  ChatAnthropic(
                model_name= self.model_name,
                max_tokens = 1000
                
            )
    

    def perform_cost_time(self, questions:list[str]) -> list[ModelUsageData] :
        
              
        data : list[ModelUsageData] = []      
        
        
        for question in questions:            
            usageData =  ModelUsageData()
            start_time = time.perf_counter() 
            
            
            response : AIMessage = None
            
            response = self.llm.invoke(
                [
                    HumanMessage(question)
                ]
            )

            end_time = time.perf_counter() 

            
            

            latency = end_time - start_time
            usageData.model_name = self.model_name
            usageData.question = question
            usageData.answer =    response.content
            usageData.prompt_token = int( response.usage_metadata["input_tokens"])
            usageData.response_token = int(response.usage_metadata["output_tokens"])
            usageData.total_response_time = latency
            
            data.append(usageData)
            break
            
        return data    

 
