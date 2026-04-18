from MistralAiChat import MistralAiChat
from ModelUsageData import ModelUsageData
from pprint import pprint
import json 


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


miChat = MistralAiChat()

miData : list[ModelUsageData] 

# miData = miChat.perform_cost_time(questions)

# print(json.dumps(miData[0].__dict__, indent=2))

from OpenAITest import OpenAITest 
# oaiChat =  OpenAITest() 

# miData = oaiChat.perform_cost_time(questions)

# print(json.dumps(miData[0].__dict__, indent=2))

from AnthropicChatTest import AnthropicChatTest

anthChat = AnthropicChatTest()
miData = anthChat.perform_cost_time(questions)

print(json.dumps(miData[0].__dict__, indent=2))

