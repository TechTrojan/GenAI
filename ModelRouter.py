from typing import Optional 
from OpenAITest import OpenAITest
from MistralAiChat import MistralAiChat
from AnthropicChatTest import AnthropicChatTest 
from ModelUsageData import ModelUsageData, write_usage_to_csv
from ResponseQuality import ResponseQuality
from typing import Any 
from ModelRouterResponse import ModelRouterMatrics, RouterResponse
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)


class ModelRouter:
    
    _enableRouter:bool = False 
    _default_Model :OpenAITest = None 
    _router_Model: MistralAiChat = None 
    _small_task_Model:OpenAITest = None 
    _medium_task_Model:AnthropicChatTest = None 
    _reason_code_task__Model:OpenAITest = None 
    _qc :ResponseQuality = None 
    
    def __init__(self, enableRouter:bool=False ):
        self._enableRouter = enableRouter
        self._qc = ResponseQuality()
        
        if self._enableRouter :
            self.__load_RotuerModels()
        else:
            self.__init__default_Model()
        
    
    def __init__default_Model(self):
        self._default_Model = OpenAITest(model_name= 'gpt-4o', token_size=1000, temperature=0.4)        
        
    def __load_RotuerModels(self):
        self._router_Model = MistralAiChat()
    
    def Calculate_Inference_Time(self, questions:list[str])->list[Any]:
        data : list[Any] 
        if ( not self._enableRouter):
            miData: list[ModelUsageData]= []     
            miData = self._default_Model.perform_cost_time(questions)
            
            data  = self._qc.GetResponseQuality(miData)
        
            

        
        return data   
    
    def single_quesetion_calculate_Inference_Time(self, question:str)->ModelRouterMatrics:
        result =  ModelRouterMatrics ()
        result.question = question
        
        data : ModelUsageData
        result.routerMatrix  = self._router_Model.single_question(question)
        
        try:
            result.routerResponse = RouterResponse.model_validate_json(result.routerMatrix.answer)
            logging.info(result.routerResponse)
        
        except Exception as e:
            logging.error(str(e))
            result.routerResponse= None 
            
        return result 
        
        
        
        
        
         
        
            

        
        return data     
    
              
            
        
        
        
            