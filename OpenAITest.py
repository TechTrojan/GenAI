from langchain_openai import ChatOpenAI

from langchain.messages import AIMessage, HumanMessage, AnyMessage , SystemMessage
from dotenv import load_dotenv 
import os 
from ModelUsageData import ModelUsageData 
import time 

load_dotenv()

class OpenAITest:
    def __init__(self):
        self.api_key = os.getenv("API_KEY")
        self.base_url  = os.getenv("OPENAI_API_BASE")
        self.model_name = 'gpt-4o-mini'        
        self.llm = ChatOpenAI(
                model = self.model_name, 
                temperature=0.5 , 
                max_tokens = 1000, 
                timeout= 50,
                max_retries= 2 ,
                api_key= self.api_key,
                base_url=self.base_url
        
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
        
    
    
    
    
    
      




