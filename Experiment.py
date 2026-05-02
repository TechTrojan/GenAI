
from ModelUsageData import ModelUsageData, write_usage_to_csv
from typing import Optional


from OpenAITest import OpenAITest 
from ResponseQuality import  ResponseQuality


 
questions = [
    "What is prompt engineering, and how can I break it down step by step to understand its main techniques, practical applications, and best practices for beginners?",

    "How does retrieval-augmented generation (RAG) work, and what questions should I ask myself to understand each component such as document loading, chunking, embeddings, retrieval, and response generation?",

    "What is responsible AI, and how can I systematically explore fairness, bias, safety, explainability, governance, and real-world implementation through self-questioning?",

    "How does cloud computing function, and what follow-up questions should I ask to understand service models, deployment models, scalability, cost optimization, and security considerations?",

    "What is Kubernetes, and how can self-ask prompting help me understand its architecture, key components, deployment workflow, scaling, and troubleshooting process?",

    "How do large language models (LLMs) work, and what sequence of self-questions can help me understand tokens, parameters, training, fine-tuning, inference, and limitations?",

    "What is prompt injection, and how can I use self-ask prompting to explore attack categories, vulnerabilities, detection methods, prevention strategies, and enterprise security implications?",

    "How does vector search operate, and what self-directed questions can help me understand embeddings, similarity metrics, indexing, storage, retrieval accuracy, and enterprise AI applications?",

    "What is agentic AI, and how can I break it into smaller self-questions to understand tools, memory, planning, orchestration, multi-agent systems, and production challenges?",

    "How can I design a production-grade AI system, and what self-ask questions should I use to evaluate architecture, scalability, observability, governance, security, and long-term maintenance?"
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
 
system_message="""You are AI engineer who has knowledge of concepts related to Generative AI, Agentic AI and related concepts."""


answers : Optional[list[ModelUsageData]]
#generate compressed prompts
answers = RunOpenAITest( system_message=system_message, testtype="Regular", CheckResponseQuality=True)


system_message="""Answer the question by decomposing it into sub-questions.
Follow this exact format:

Question : <Question>

Are follow up question needed here  : Yes/No.
Follow up: <sub-question>
Intermediate answer : <answer>
... (repeat as needed)
So the final answer is : <final_answer> 

Begin !
Question : 
"""


answers : Optional[list[ModelUsageData]]
#generate compressed prompts
answers = RunOpenAITest( system_message=system_message, testtype="SelfAsk",CheckResponseQuality=True)





