from langchain_openai import ChatOpenAI
from typing import List

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
       
    
    def GetResponseQuality(self, data_list: List[ModelUsageData]) -> List[ModelUsageData]:

        system_prompt = """
        You are an expert evaluator assessing the quality of an AI-generated response.

        Evaluate the response based on the following criteria (score each from 1 to 5):

        1. Relevance
        2. Clarity
        3. Completeness
        4. Usefulness

        Be critical and do not give high scores unless the response is clearly strong.

        Return ONLY a valid JSON object in the following format:

        {
            "relevance": <number>,
            "clarity": <number>,
            "completeness": <number>,
            "usefulness": <number>,
            "overall_score": <number>
        }
        """

        user_prompt = """
        Question:
        {question}

        Response:
        {response}
        """

        for data in data_list:
            try:
                user_prompt_input = user_prompt.format(
                    question=data.question,
                    response=data.answer
                )

                messages = [
                    SystemMessage(content=system_prompt),
                    HumanMessage(content=user_prompt_input)
                ]

                response = self.llm.invoke(messages)

                parsed = json.loads(response.content)

                # Update object
                data.relevance = parsed.get("relevance", 0)
                data.clarity = parsed.get("clarity", 0)
                data.completeness = parsed.get("completeness", 0)
                data.usefulness = parsed.get("usefulness", 0)
                data.overall_score = parsed.get("overall_score", 0)

            except Exception as e:
                print(f"Error processing item: {data.question}")
                print(str(e))

        return data_list  
        
    
    
    
    
    
      




