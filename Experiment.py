
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
    "Write a short thank-you message to a colleague for helping with a project.",
    "Design a high-level architecture for a smart model router that selects models based on prompt complexity and response quality.",
    "Generate Python code that reads a CSV file and calculates total cost grouped by model name.",
    "What factors should I consider when buying a wireless noise-cancelling headphone?",
    "Explain the tradeoffs between using a smaller LLM for fast responses and a larger LLM for complex reasoning tasks.",
    "Debug this Python error conceptually: TypeError: Object of type CustomClass is not JSON serializable.",
    "Summarize the benefits of using cloud computing for a small business in simple terms.",
    "What is the difference between Wi-Fi and Bluetooth?",
    "Create a production-ready architecture for an AI chatbot that uses RAG, model routing, observability, and cost tracking.",
    "Generate Python code that reads a JSON file and converts selected nested fields into a CSV file.",
    "Write five LinkedIn hashtags for a post about responsible AI.",
    "Explain the difference between Kubernetes HPA, VPA, and Cluster Autoscaler with examples.",
    "What is prompt caching in simple terms?",
    "Write Python code to call the OpenAI Responses API and print the model response.",
    "Give me three tips to improve focus while working from home.",
    "Compare RAG and fine-tuning for building a domain-specific AI assistant.",
    "Explain how to make a Python class JSON serializable using a to_dict method.",
    "Write a short LinkedIn post about continuous learning in Artificial Intelligence.",
    "What is the purpose of a README.md file in a GitHub project?",
    "Design an evaluation framework to compare baseline LLM responses against routed model responses using cost, latency, and quality metrics.",
    "Generate Python code that measures response time for a function using time.perf_counter.",
    "Explain what an API is using a simple real-world example.",
    "What are the main benefits of using version control with Git?",
    "Compare rule-based routing and LLM-based routing for selecting the best model in an AI platform.",
    "Write Python code that validates whether a string contains valid JSON and returns a Python dictionary.",
    "Summarize the concept of tokenization in large language models for a beginner.",
    "What are three common use cases of generative AI in business?",
    "Create a detailed system design for an enterprise AI assistant that supports multiple models, prompt logging, fallback handling, and user feedback.",
    "Generate Python code that uses pandas to calculate average latency, total tokens, and total cost from an experiment result CSV.",
    "Explain the difference between input tokens and output tokens.",
    "Write a simple professional email asking for a project status update.",
    "Analyze the cost, latency, and quality tradeoffs of routing simple prompts to gpt-4o-mini and complex prompts to gpt-4o.",
    "Fix this Python issue conceptually: json.dumps fails when the object contains datetime values.",
    "What is latency in an LLM application?",
    "Give me a simple explanation of cloud storage.",
    "Design a cost-aware model routing policy that decides between fast, quality, and code routes for different user prompt types.",
    "Write Python code that appends experiment results to a CSV file without overwriting existing rows.",
    "List five advantages of using Docker for application deployment.",
    "Explain why model routing can sometimes increase cost instead of reducing it.",
    "Generate Python code that maps route names like Simple, Quality, and Code to model names using a dictionary."
]



from ModelRouter import ModelRouter


router = ModelRouter(True)

# data = router.Calculate_Inference_Time(questions=questions)

# write_usage_to_csv("Baseline_model_version2_with_cost.csv",data )


routerEvalResult : list[ModelRouterMatrics] = []


for i, q in enumerate(questions):
    data : ModelRouterMatrics = None 
    print(f" Question No : {str(i+1)} -> {q}")
    data= router.single_quesetion_calculate_Inference_Time(q)
    if data :
       routerEvalResult.append(data)
    

save_to_json("RouterResult.json", routerEvalResult)
logging.info("Experiment completed")


    
    
