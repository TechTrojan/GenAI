
from ModelUsageData import ModelUsageData
from ModelRouterResponse import ModelRouterMatrics , RouterResponse
import logging
from UtilityFunctions import  write_usage_to_csv, save_to_json, write_dict_list_to_csv 

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

# from OpenAITest import OpenAITest 
# from ResponseQuality import  ResponseQuality
# from AnthropicChatTest import AnthropicChatTest
# from MistralAiChat import MistralAiChat


questions = [    
    "What factors should I consider when buying a wireless noise-cancelling headphone?",
    "Summarize the benefits of using cloud computing for a small business in simple terms.",
    "Write a short LinkedIn post about continuous learning in Artificial Intelligence.",
    "Explain the difference between Kubernetes HPA, VPA, and Cluster Autoscaler with examples.",
    "Compare RAG and fine-tuning for building a domain-specific AI assistant.",
    "Design a high-level architecture for a smart model router that selects models based on prompt complexity.",
     "Generate Python code that reads a CSV file, calculates average latency by model name, and prints the result.",
    "Debug this Python error conceptually: TypeError: Object of type CustomClass is not JSON serializable.",
    "Create a production-ready architecture for an AI chatbot that uses RAG, model routing, observability, and cost tracking.",
    "Explain the tradeoffs between using a smaller LLM for fast responses and a larger LLM for complex reasoning tasks."
]


# qc = ResponseQuality()


# def RunMistralAIModel():
#     miChat = MistralAiChat()
#     miData: list[ModelUsageData]= [] 
    
#     miData = miChat.perform_cost_time(questions)
    
#     data  = qc.GetResponseQuality(miData)

#     write_usage_to_csv("MistralAI_result.csv",data )
    
#     print('Generated result for MistralAI')



# def RunOpenAITest():

#     oaiChat =  OpenAITest() 
#     miData: list[ModelUsageData]= [] 
#     miData = oaiChat.perform_cost_time(questions)

#     data  = qc.GetResponseQuality(miData)

#     write_usage_to_csv("OpenAI_result.csv",data )
    
#     print('Generated result for OPEN AI')    

# def RunAnthropicTest(): 
    
#     anthChat = AnthropicChatTest()
    
#     miData: list[ModelUsageData]= [] 
#     miData = anthChat.perform_cost_time(questions)
    
#     data  = qc.GetResponseQuality(miData)

#     write_usage_to_csv("Anthropic_result.csv",data )
    
#     print('Generated result for Anthropic')

#RunMistralAIModel()
#RunOpenAITest()
#RunAnthropicTest()

from ModelRouter import ModelRouter


router = ModelRouter(True)

#data = router.Calculate_Inference_Time(questions=questions)

#write_usage_to_csv("Baseline_model.csv",data )


routerEvalResult : list[ModelRouterMatrics] = []


for i, q in enumerate(questions):
    data : ModelRouterMatrics = None 
    print(f" Question No : {str(i+1)} -> {q}")
    data= router.single_quesetion_calculate_Inference_Time(q)
    if data :
       routerEvalResult.append(data)
    

save_to_json("RouterResult.json", routerEvalResult)

    
    
