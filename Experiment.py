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


#miChat = MistralAiChat()

#miData : list[ModelUsageData] 

# miData = miChat.perform_cost_time(questions)

# print(json.dumps(miData[0].__dict__, indent=2))

#from OpenAITest import OpenAITest 
# oaiChat =  OpenAITest() 

# miData = oaiChat.perform_cost_time(questions)

# print(json.dumps(miData[0].__dict__, indent=2))

#from AnthropicChatTest import AnthropicChatTest

# anthChat = AnthropicChatTest()
# miData = anthChat.perform_cost_time(questions)

#print(json.dumps(miData[0].__dict__, indent=2))

from ResponseQuality import  ResponseQuality

qc = ResponseQuality()

data = ModelUsageData()
data.question="What factors should I consider when buying a wireless noise-cancelling headphone?"
data.answer="""
# Buying Wireless Noise-Cancelling Headphones: Key Factors\n\n## Sound Quality\n- **Driver size and type** (larger drivers often produce richer bass)\n- **Frequency response range**\n- **Codec support** (aptX, AAC, LDAC for higher quality audio)\n- **Sound signature** (balanced, bass-heavy, bright - matches your preference)\n\n## Noise Cancellation Performance\n- **ANC strength** (how much external noise is blocked)\n- **Transparency/ambient mode** (letting in outside sound when needed)\n- **Effectiveness across frequencies** (low hum vs. voices)\n\n## Comfort & Fit\n- Ear cup size and padding material\n- Headband adjustability and weight\n- Over-ear vs. on-ear design\n- Suitability for glasses wearers\n\n## Battery Life\n- ANC-on vs. ANC-off hours\n- Charging time\n- Quick charge capability\n\n## Connectivity\n- Bluetooth version (5.0+ preferred)\n- Multi-device pairing\n- Range stability\n\n## Practical Features\n- Microphone quality for calls\n- Physical controls vs. touch controls\n- Companion app availability\n- Foldability for travel\n\n## Budget Considerations\n- **Premium:** Sony WH-1000XM5, Bose QuietComfort 45\n- **Mid-range:** Anker Soundcore Q45, JBL Live 660\n- **Budget:** options around $50-80\n\n## Use Case\n- **Travel** \u2192 prioritize ANC and battery\n- **Office** \u2192 prioritize mic and comfort\n- **Gym** \u2192 consider sweat resistance\n\nWould you like more detail on any specific factor?
"""

data  = qc.GetResponseQuality(data)

