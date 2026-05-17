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
    
    #models 
    _small_task_Model:OpenAITest = None 
    _medium_task_Model:AnthropicChatTest = None 
    _reason_code_task__Model:OpenAITest = None 
    
    _qc :ResponseQuality = None 
    _modelRouteList  : dict = None 
    
    def __init__(self, enableRouter:bool=False ):
        self._enableRouter = enableRouter
        self._qc = ResponseQuality()
        
        if self._enableRouter :
            self.__initiate_router_trafic_matrix()
            self.__load_RotuerModels()
            
           
            
        else:
            self.__init__default_Model()
        
    def __initiate_router_trafic_matrix(self):
        self._modelRouteList = dict()
        self._modelRouteList['Simple']= 'gpt-4o-mini'
        self._modelRouteList['Quality']= 'claude-sonnet-4-6'
        self._modelRouteList['Code']= 'gpt-4o'
        
    def __init__default_Model(self):
        self._default_Model = OpenAITest(model_name= 'gpt-4o', token_size=1000, temperature=0.4)        
        
    def __load_RotuerModels(self):
        self._router_Model = MistralAiChat()
        self._small_task_Model = OpenAITest(self._modelRouteList['Simple'],500,0.4)
        self._medium_task_Model = AnthropicChatTest( self._modelRouteList['Quality'])
        self._reason_code_task__Model = OpenAITest( self._modelRouteList['Code'],2000,0.2)
        
        
    
    def Calculate_Inference_Time(self, questions:list[str])->list[Any]:
        data : list[Any] 
        if ( not self._enableRouter):
            miData: list[ModelUsageData]= []     
            miData = self._default_Model.perform_cost_time(questions)
            
            data  = self._qc.GetResponseQuality(miData)
        
            

        
        return data
    
    def __RouteTraffic__(self, routeType:str ) -> str :
        selectedModel : str = 'gpt-4o-mini' 
        
        if routeType in  self._modelRouteList:
            selectedModel = self._modelRouteList [routeType]
        
        return selectedModel


        
    def __GetLLMResult__(self, model_to_route:str, question:str )-> ModelRouterMatrics:
        data : ModelRouterMatrics = None 
        
        if model_to_route == 'gpt-4o-mini' :
            data = self._small_task_Model.single_quesetion_perform_cost_time(question)
        elif model_to_route == 'claude-sonnet-4-6' :
            data = self._medium_task_Model.single_question_perform_cost_time(question)
        else:
            data = self._reason_code_task__Model.single_quesetion_perform_cost_time(question)

        return data             
        
        
        
    
    def single_quesetion_calculate_Inference_Time(self, question:str)->ModelRouterMatrics:
        result =  ModelRouterMatrics ()
        result.question = question
        
        data : ModelUsageData
        result.routerMatrix  = self._router_Model.single_question(question)
        
        modelToRoute:str
        
        try:
            result.routerResponse = RouterResponse.model_validate_json(result.routerMatrix.answer)            
            modelToRoute = self.__RouteTraffic__(result.routerResponse.route)
        except Exception as e:
            logging.error(str(e))
            result.routerResponse= None 
            modelToRoute='gpt-4o-mini'

        result.llmResponse = self.__GetLLMResult__(modelToRoute, question)        

             

        return result 
        
        
        
        
        
         
        
            

        
        return data     
    
              
            
        
        
        
            