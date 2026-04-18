class ModelUsageData:
    model_name = ''
    question: str =''
    answer : str = ''
    prompt_token: int =0 ,
    response_token : int =0 ,
    total_token : int = 0     
    total_response_time :float = 0.0
    
    