
from ModelUsageData import ModelUsageData, write_usage_to_csv
from typing import Optional


from OpenAITest import OpenAITest 
from ResponseQuality import  ResponseQuality


 


questions = [
    "Please provide a detailed explanation of cloud computing, including its key benefits, common use cases, architecture, and real-world examples that can help a beginner understand the concept clearly.",
    
    "Explain in detail how recommendation systems work in e-commerce platforms, including collaborative filtering, content-based filtering, and hybrid approaches with practical examples.",
    
    "Provide a comprehensive comparison between laptops and tablets, including performance, portability, battery life, cost, and ideal use cases for different types of users.",
    
    "Describe the important factors that should be considered when buying a wireless noise-cancelling headphone, including sound quality, battery life, comfort, brand reliability, and pricing.",
    
    "Explain the concept of microservices architecture, including its advantages, disadvantages, design patterns, and how it differs from monolithic architecture with real-world examples.",
    
    "Provide a step-by-step guide for selecting a good smartphone based on performance, camera quality, battery life, software updates, and overall value for money.",
    
    "Explain how cloud storage works, including different types such as object storage, block storage, and file storage, along with their use cases and benefits.",
    
    "Describe how customers should evaluate different online shopping platforms based on pricing, delivery speed, product availability, return policies, and customer support.",
    
    "Explain the concept of artificial intelligence and machine learning, including key differences, types of learning, and practical applications in real-world scenarios.",
    
    "Provide a detailed explanation of how APIs work, including REST architecture, request-response cycle, authentication methods, and real-world usage examples."
]



     

 

qc = ResponseQuality()

 



def RunOpenAITest(system_message:str="", testtype:str ="", CheckResponseQuality:bool = True, )-> list[ModelUsageData]:

    oaiChat =  OpenAITest(system_prompt = system_message) 
    
    miData: list[ModelUsageData]= [] 
    miData = oaiChat.perform_cost_time(questions)

    if CheckResponseQuality:
        data  = qc.GetResponseQuality(miData)
        write_usage_to_csv(f"OpenAI_result_{testtype}.csv",data )
    
    print('Generated result for OPEN AI')
    
    if not CheckResponseQuality:
        return miData    
 

#Generate answers and quality response for regular prompt.

RunOpenAITest(testtype="Regular", CheckResponseQuality=True)

compress_prompt="""Compress the following prompt by removing unnecessary words while preserving intent.

Return a shorter version only.

Prompt:
"""


compressed_Prompts : Optional[list[ModelUsageData]]
#generate compressed prompts
compressed_Prompts = RunOpenAITest( system_message=compress_prompt, CheckResponseQuality=False)


questions = [ data.answer for data in compressed_Prompts ]    



#Generate answers for compressed prompts
RunOpenAITest( CheckResponseQuality=True, testtype="compressed")


