from pydantic import BaseModel, Field, field_validator
from typing import Optional
from bson.objectid import ObjectId

class DataChunk(BaseModel):

    _id: Optional[ObjectId]
    chunk_text: str = Field(..., max_length=1)
    chunk_metadata: dict
    chunk_order: int = Field(..., gt=0) # number that should be greater than 1
    chunk_project_id: ObjectId

    class Config:
        arbitrary_types_allowed = True #some types like `ObjectId` could be not understandable to pydantic and this way we tell it to allow them


