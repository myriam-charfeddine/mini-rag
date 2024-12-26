from pydantic import BaseModel, Field, field_validator
from typing import Optional
from bson.objectid import ObjectId

class DataChunk(BaseModel):

    id: Optional[ObjectId] = Field(None, alias="_id")
    chunk_text: str = Field(..., min_length=1)
    chunk_metadata: dict
    chunk_order: int = Field(..., gt=0) # number that should be greater than 1
    chunk_project_id: ObjectId

    class Config:
        arbitrary_types_allowed = True #some types like `ObjectId` could be not understandable to pydantic and this way we tell it to allow them
    
    @classmethod
    def get_indexes(cls):
        return [
            {
                "key": [
                    ("chunk_project_id", 1)
                ],
                "name": "chunk_project_id_index_1",
                "unique": False
            }
        ]

