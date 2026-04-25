from langchain_openai import ChatOpenAI

from langchain.messages import AIMessage, HumanMessage, AnyMessage , SystemMessage
from dotenv import load_dotenv 
import os 
from ModelUsageData import ModelUsageData 
import time 

load_dotenv()

class OpenAITest:
    def __init__(self, system_prompt:str = ''):
        self.api_key = os.getenv("API_KEY")
        self.base_url  = os.getenv("OPENAI_API_BASE")
        self.model_name = 'gpt-4o-mini'   
        self._system_prompt     =system_prompt
        self.llm = ChatOpenAI(
                model = self.model_name, 
                temperature=0.5 , 
                max_tokens = 500, 
                timeout= 50,
                max_retries= 2 ,
                api_key= self.api_key,
                base_url=self.base_url
        
            )
       
    
    def perform_cost_time(self, questions:list[str]) -> list[ModelUsageData] :
        
              
        data : list[ModelUsageData] = []      
      
        i=1
        for i, question in enumerate(questions):            
            usageData =  ModelUsageData()
            start_time = time.perf_counter() 
            
            print("Generating response for model {} , Question No. {}".format(self.model_name, i+1))
            
            
            
            messages : list[AnyMessage] = []
            if self._system_prompt:
                messages.append(SystemMessage( self._system_prompt))
                
            messages.append(HumanMessage(question))                
                
            response : AIMessage = None
            
            response = self.llm.invoke( messages        )

            end_time = time.perf_counter() 

            
            

            latency = end_time - start_time
            usageData.model_name = self.model_name
            usageData.question = question
            usageData.answer =    response.content
            usageData.prompt_token = int( response.usage_metadata["input_tokens"])
            usageData.response_token = int(response.usage_metadata["output_tokens"])
            usageData.total_token = usageData.prompt_token + usageData.response_token
            usageData.total_response_time = latency
            
            data.append(usageData)
            i=i+ 1
            
            
            
        return data      
        
    
    
    
    
    
      




