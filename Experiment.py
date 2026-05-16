
from ModelUsageData import ModelUsageData, write_usage_to_csv



from OpenAITest import OpenAITest 
from ResponseQuality import  ResponseQuality
from AnthropicChatTest import AnthropicChatTest
from MistralAiChat import MistralAiChat



questions = [
    "What factors should I consider when buying a wireless noise-cancelling headphone?",
    
    "Explain the key differences between SSD and HDD storage in simple terms."
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
