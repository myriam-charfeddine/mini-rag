from pydantic import BaseModel, Field, field_validator
from typing import Optional
from bson.objectid import ObjectId

class Project(BaseModel):
    
    id: Optional[ObjectId] = Field(None, alias="_id")
    project_id: str = Field(..., min_length=1) #the field `project_id` should at least have a length of 1

    @field_validator('project_id') #to validate that the `project_id` contains only num and alpha values:
    def validate_project_id(cls, value): #cls refers to the class `project_id` and value refers to its value
        if not value.isalnum():
            raise ValueError("project_id must be alphanumeric")
        
        return value
    
    class Config:
        arbitrary_types_allowed = True #some types like `ObjectId` could be not understandable to pydantic and this way we tell it to allow them

    #using the following func we get indexing for our db to faster the search, instead of looking for the whole docs in db, MongoDB consults
    #the indexes (created from specific filelds, then it retrieve the data to which that ``index`` points)
    @classmethod
    def get_indexes(cls): # `cls` refers to the current class
        return [
            {
                "key": [
                    ("project_id", 1) # 1 indicates an ascending index (use -1 for descending)
                ],
                "name": "project_id_index_1", # name of the index
                "unique":True
            }
        ]



