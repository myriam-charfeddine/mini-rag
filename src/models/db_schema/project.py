from pydantic import BaseModel, Field, field_validator
from typing import Optional
from bson.objectid import ObjectId

class Project(BaseModel):
    
    _id: Optional[ObjectId]
    project_id: str = Field(..., min_length=1) #the field `project_id` should at least have a length of 1

    @field_validator('project_id') #to validate that the `project_id` contains only num and alpha values:
    def validate_project_id(cls, value): #cls refers to the class `project_id` and value refers to its value
        if not value.isalnum():
            raise ValueError("project_id must be alphanumeric")
        
        return value
    
    class Config:
        arbitrary_types_allowed = True #some types like `ObjectId` could be not understandable to pydantic and this way we tell it to allow them




