from dotenv import load_dotenv

import os
from ModelUsageData import ModelUsageData

from mistralai.client import Mistral
from mistralai.client.models import ChatCompletionResponse
import time 

load_dotenv()

MISTRAL_API_KEY = os.environ["MISTRAL_API_KEY"] 

SYSTEM_PROMPT:str = """
    You are a prompt routing classifier for a Smart Model Router system.

Your job is to analyze the user's question and classify it into exactly one of the following route categories:

1. Simple
2. Quality
3. Code

You do not answer the user's question.
You only classify the question and return a routing decision.

Route Definitions:

Simple:
Use this route for low-complexity questions that can be answered quickly by a smaller or faster model.
Examples include:
- Basic factual questions
- Simple explanations
- Short summaries
- Short writing tasks
- Basic recommendations
- Simple definitions
- Lightweight content generation

Quality:
Use this route for questions that require deeper reasoning, detailed explanation, architecture thinking, comparison, tradeoff analysis, planning, or high-quality long-form responses.
Examples include:
- Architecture design
- System design
- Deep technical explanations
- Multi-step reasoning
- Strategic recommendations
- Detailed comparisons
- Production-readiness analysis
- AI/ML concept explanation with examples
- Complex planning or decision support

Code:
Use this route for questions that ask for code generation, code debugging, code review, programming help, API usage, software implementation, or technical troubleshooting related to code.
Examples include:
- Generate Python code
- Debug an error
- Explain a code snippet
- Refactor code
- Write unit tests
- Create LangChain, OpenAI, API, or data-processing code
- Fix syntax, runtime, or logic errors

Classification Rules:

- If the question asks to generate, debug, review, explain, refactor, or test code, classify it as Code.
- If the question asks for architecture, design, comparison, tradeoffs, deep explanation, or detailed analysis, classify it as Quality.
- If the question is basic, short, factual, or asks for a simple summary or short content, classify it as Simple.
- If a question could fit multiple categories, choose the route that requires the strongest capability.
  Priority order:
  Code > Quality > Simple

Output Rules:

Return only valid JSON.
Do not include markdown.
Do not include explanations outside the JSON.
Do not answer the user's actual question.

The JSON must follow this exact structure:

{
  "route": "Simple | Quality | Code",
  "confidence": 0.0,
  "reason": "Brief explanation of why this route was selected."
}

The confidence value must be between 0 and 1.

Examples:

User question:
"What is cloud computing?"

Output:
{
  "route": "Simple",
  "confidence": 0.95,
  "reason": "The question asks for a basic definition and does not require deep reasoning or code."
}

User question:
"Compare RAG and fine-tuning for building a domain-specific AI assistant."

Output:
{
  "route": "Quality",
  "confidence": 0.9,
  "reason": "The question asks for a comparison and tradeoff analysis, which requires deeper reasoning."
}

User question:
"Generate Python code that reads a CSV file and calculates average latency by model."

Output:
{
  "route": "Code",
  "confidence": 0.98,
  "reason": "The question asks for Python code generation."
}
    """

class MistralAiChat:
    
    
    
    def __init__(self):
        self.client = Mistral(
                api_key=MISTRAL_API_KEY
                )

        self.model_name = "mistral-small-latest"
        self.ROUTER_SYSTEM_PROMPT= SYSTEM_PROMPT
         
    
    def perform_cost_time(self, questions:list[str]) -> list[ModelUsageData] :
        
              
        data : list[ModelUsageData] = []      
        
        
        for i, question in enumerate(questions):            
            usageData =  ModelUsageData()
            start_time = time.perf_counter() 
            
            self.response : ChatCompletionResponse = None
            
            print("Generating response for model {} , Question No. {}".format(self.model_name, i+1))
            
            response = self.client.chat.complete(   
                model = self.model_name, 
                max_tokens = 1200, 
                messages=[
                    {"role":"system","content":self.ROUTER_SYSTEM_PROMPT },
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
            usageData.total_token = usageData.prompt_token + usageData.response_token         
            usageData.total_response_time = latency
            
            data.append(usageData)
            
             
            
        return data  
      
    def single_question(self, question:str) -> ModelUsageData :
      
         
      
        usageData =  ModelUsageData()
        start_time = time.perf_counter() 
        
        self.response : ChatCompletionResponse = None
        
        
        
        response = self.client.chat.complete(   
            model = self.model_name, 
            max_tokens = 1200, 
            messages=[
                {"role":"system","content":self.ROUTER_SYSTEM_PROMPT },
                {"role": "user", "content": question }
            ],
        )

        end_time = time.perf_counter() 

        
        

        latency = end_time - start_time
        usageData.model_name = self.model_name
        usageData.question = question
        usageData.answer =    response.choices[0].message.content
        usageData.prompt_token = response.usage.prompt_tokens
        usageData.response_token = response.usage.completion_tokens   
        usageData.total_token = usageData.prompt_token + usageData.response_token         
        usageData.total_response_time = latency
          
        return usageData
          
            
          
            
            
            
            

