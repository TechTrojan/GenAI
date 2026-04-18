
from ModelUsageData import ModelUsageData, write_usage_to_csv



from OpenAITest import OpenAITest 
from ResponseQuality import  ResponseQuality
from AnthropicChatTest import AnthropicChatTest
from MistralAiChat import MistralAiChat



questions = [
    "What factors should I consider when buying a wireless noise-cancelling headphone?",
    
    "Explain the key differences between SSD and HDD storage in simple terms.",
    
    "Give me 5 tips for choosing a good office chair for long working hours.",
    
    "Compare laptops vs tablets for students and suggest when to choose each.",
    
    "Write a short promotional message for an online shopping platform highlighting fast delivery and great customer service.",
    
    "Explain in detail how a recommendation system works in e-commerce platforms.",
    
    "Provide a step-by-step guide to selecting a good smartphone based on performance, battery life, and camera quality.",
    
    "Summarize the benefits of cloud computing for small businesses in a structured bullet-point format.",
    
    "Explain how customers should evaluate different online marketplaces based on pricing, delivery, return policies, and customer support, and provide guidance for making a smart purchase decision.",
    
    "Create a structured comparison of three popular online shopping platforms based on user experience, pricing, delivery speed, and trust factors, and present it in a clear table format."
]

# questions = [
#     "What factors should I consider when buying a wireless noise-cancelling headphone?",
    
#     "Explain the key differences between SSD and HDD storage in simple terms."
#     ]

qc = ResponseQuality()


def RunMistralAIModel():
    miChat = MistralAiChat()
    miData: list[ModelUsageData]= [] 
    
    miData = miChat.perform_cost_time(questions)
    
    data  = qc.GetResponseQuality(miData)

    write_usage_to_csv("MistralAI_result.csv",data )
    
    print('Generated result for MistralAI')



def RunOpenAITest():

    oaiChat =  OpenAITest() 
    miData: list[ModelUsageData]= [] 
    miData = oaiChat.perform_cost_time(questions)

    data  = qc.GetResponseQuality(miData)

    write_usage_to_csv("OpenAI_result.csv",data )
    
    print('Generated result for OPEN AI')    

def RunAnthropicTest(): 
    
    anthChat = AnthropicChatTest()
    
    miData: list[ModelUsageData]= [] 
    miData = anthChat.perform_cost_time(questions)
    
    data  = qc.GetResponseQuality(miData)

    write_usage_to_csv("Anthropic_result.csv",data )
    
    print('Generated result for Anthropic')

RunMistralAIModel()
RunOpenAITest()
RunAnthropicTest()
