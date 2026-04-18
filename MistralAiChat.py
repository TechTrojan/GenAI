from dotenv import load_dotenv

import os
from ModelUsageData import ModelUsageData

from mistralai.client import Mistral
from mistralai.client.models import ChatCompletionResponse
import time 

load_dotenv()

MISTRAL_API_KEY = os.environ["MISTRAL_API_KEY"] 

class MistralAiChat:
    def __init__(self):
        self.client = Mistral(
                api_key=MISTRAL_API_KEY
                )

        self.model_name = "mistral-small-latest"
         
    
    def perform_cost_time(self, questions:list[str]) -> list[ModelUsageData] :
        
              
        data : list[ModelUsageData] = []      
        
        
        for question in questions:            
            usageData =  ModelUsageData()
            start_time = time.perf_counter() 
            
            self.response : ChatCompletionResponse = None
            
            response = self.client.chat.complete(   
                model = self.model_name, 
                max_tokens = 1000, 
                messages=[
                    {"role": "user", "content": question }
                ],
            )

            end_time = time.perf_counter() 

            
            response.usage.completion_tokens

            latency = end_time - start_time
            usageData.model_name = self.model_name
            usageData.question = question
            usageData.answer =    response.choices[0].message.content
            usageData.prompt_token = response.usage.prompt_tokens
            usageData.response_token = response.usage.completion_tokens            
            usageData.total_response_time = latency
            
            data.append(usageData)
            break
            
        return data            
            
            
            

