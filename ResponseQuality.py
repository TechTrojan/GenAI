from langchain_openai import ChatOpenAI

from langchain.messages import AIMessage, HumanMessage, AnyMessage , SystemMessage
from dotenv import load_dotenv 
import os 
from ModelUsageData import ModelUsageData 
import time 
import json 

load_dotenv()

class ResponseQuality:
    def __init__(self):
        self.api_key = os.getenv("API_KEY")
        self.base_url  = os.getenv("OPENAI_API_BASE")
        self.model_name = 'gpt-4o'        
        self.llm = ChatOpenAI(
                model = self.model_name, 
                temperature=0.5 , 
                max_tokens = 200, 
                timeout= 50,
                max_retries= 2 ,
                api_key= self.api_key,
                base_url=self.base_url
        
            )
       
    
    def GetResponseQuality(self,  data : ModelUsageData ) -> ModelUsageData :
        
        response : AIMessage = None
        system_prompt="""
        You are an expert evaluator assessing the quality of an AI-generated response.

            Evaluate the response based on the following criteria (score each from 1 to 5):

            1. Relevance: How well the response answers the question
            2. Clarity: How clear and easy to understand the response is
            3. Completeness: How thoroughly the response covers the important aspects
            4. Usefulness: How helpful and practical the response is

            Be critical and do not give high scores unless the response is clearly strong.
            
            Return ONLY a valid JSON object in the following format (no explanation, no extra text):

            {
            "relevance": <number>,
            "clarity": <number>,
            "completeness": <number>,
            "usefulness": <number>,
            "overall_score": <number>
            }
        """     
            
        user_prompt="""

            Question:
            {question}

            Response:
            {response}

           """
        
        try:
            
            
                
            user_prompt_input= user_prompt.format(question=data.question, response=data.answer)
            
            messages = [
                SystemMessage(content=system_prompt),
                HumanMessage(content=user_prompt_input)
                
            ]
            
            response = self.llm.invoke(
                messages
            
            )
            
            parsed = json.loads(response.content)
            
            data.relevance = parsed["relevance"]
            data.clarity=  parsed["clarity"]
            data.completeness=  parsed["completeness"]
            data.usefulness=  parsed["usefulness"]
            data.overall_score=  parsed["overall_score"]
        
        except Exception as e:
            print(str(e))
             
            
        return data      
        
    
    
    
    
    
      




