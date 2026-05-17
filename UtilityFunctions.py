import csv
from typing import List, Dict, Any
from ModelRouterResponse import ModelUsageData, ModelRouterMatrics 


import json 


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


 

def write_dict_list_to_csv(file_name: str, data: List[Dict[str, Any]]):
    
    # Handle empty data
    if not data:
        print("No data found.")
        return

    # Extract column names dynamically from first dictionary
    headers = list(data[0].keys())

    with open(file_name, mode='w', newline='', encoding='utf-8') as file:

        writer = csv.writer(file)

        # Write Header
        writer.writerow(["Sr.No"] + headers)

        # Write Rows
        for index, item in enumerate(data, start=1):

            row = [index]

            for header in headers:
                row.append(item.get(header, ""))

            writer.writerow(row)            

def save_to_json(file_name: str, data: list[ModelRouterMatrics]):

    with open(file_name, "w", encoding="utf-8") as file:

        json.dump(
            [x.model_dump() for x in data],
            file,
            indent=2
        )      