
from pydantic import BaseModel, Field

class RouterResponse(BaseModel):
    route: str = ""
    confidence: float = 0.0
    reason: str = ""
