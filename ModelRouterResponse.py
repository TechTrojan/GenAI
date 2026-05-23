from ModelUsageData import ModelUsageData 
 

from pydantic import BaseModel, Field
from RouterResponse import RouterResponse




class ModelRouterMatrics(BaseModel):
    question: str = ""

    routerMatrix: ModelUsageData = Field(
        default_factory=ModelUsageData
    )

    llmResponse: ModelUsageData = Field(
        default_factory=ModelUsageData
    )

    routerResponse: RouterResponse = Field(
        default_factory=RouterResponse
    )