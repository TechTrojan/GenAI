from pydantic import BaseModel
from ModelUsageData import ModelUsageData 

    
from pydantic import BaseModel

class RouterResponse(BaseModel):
    route: str = ""
    confidence: float = 0.0
    reason: str = ""


from pydantic import BaseModel, Field

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