import csv
from typing import List

class ModelUsageData:
    model_name = ''
    question: str = ''
    answer: str = ''
    prompt_token: int = 0
    response_token: int = 0
    total_token: int = 0
    total_response_time: float = 0.0
    relevance: int = 0
    clarity: int = 0
    completeness: int = 0
    usefulness: int = 0
    overall_score: int = 0
    

def write_usage_to_csv(file_name: str, data: List[ModelUsageData]):
    with open(file_name, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)

        # Header
        writer.writerow([
            "Sr.No",
            "model_name", "question", "answer",
            "prompt_token", "response_token", "total_token",
            "total_response_time",
            "relevance", "clarity", "completeness",
            "usefulness", "overall_score"
        ])
        i=1 
        # Rows
        for item in data:
            writer.writerow([
                i, 
                item.model_name,
                item.question,
                item.answer,
                item.prompt_token,
                item.response_token,
                item.total_token,
                item.total_response_time,
                item.relevance,
                item.clarity,
                item.completeness,
                item.usefulness,
                item.overall_score
            ])
            
            i=i+1 