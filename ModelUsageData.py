class ModelUsageData:
    model_name = ''
    question: str =''
    answer : str = ''
    prompt_token: int =0 ,
    response_token : int =0 ,
    total_token : int = 0     
    total_response_time :float = 0.0
    relevance:int=0 ,
    clarity:int=0 ,
    completeness:int=0 ,
    usefulness:int=0 ,
    overall_score:int=0 
    
    