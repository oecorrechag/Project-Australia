# 1. Library imports
from pydantic import BaseModel

# 2. Class for models.
class inputs(BaseModel):
    t:float=3
    frequency:float=2
    recency:float=30
    T:float=90

class profit(BaseModel):
    frequency:float=2
    monetary:float=1200

class cltv(BaseModel):
    frequency:float=2
    recency:float=30
    T:float=90
    monetary:float=1200
    