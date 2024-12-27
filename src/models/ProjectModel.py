from .BaseDataModel import BaseDataModel
from .db_schema import Project
from .enums.DataBaseEnum import DataBaseEnum

class ProjectModel(BaseDataModel):
    def __init__(self, db_client: object):
        super().__init__(db_client=db_client)
        self.collection = self.db_client[DataBaseEnum.COLLECTION_PROJECT_NAME.value]
    
    @classmethod #in the following func we init our project and we create index, why this function? =>since the indexing should be created at the beggining, so it should be in __init__ or the creation of indexes is asyncio since we are using MOTOR for Mongo, so we made another func that is asyncio and that calls __init__ and create index at the same time
    async def create_instance(cls, db_client: object):
        instance = cls(db_client)
        await instance.init_collection()
        return instance

    async def init_collection(self):
        all_collection = await self.db_client.list_collection_names()

        if DataBaseEnum.COLLECTION_PROJECT_NAME.value not in all_collection:
           self.collection = self.db_client[DataBaseEnum.COLLECTION_PROJECT_NAME.value]
           indexes = Project.get_indexes()
           for index in indexes:
               await self.collection.create_index(
                   index["key"],
                   name=index["name"],
                   unique=index["unique"]
               )
    
    async def create_project(self, project: Project):
        result = await self.collection.insert_one(project.model_dump(by_alias=True, exclude_unset=True))
        project.id = result.inserted_id
        return project
    
    async def get_project_or_create_one(self, project_id: str):
        record = await self.collection.find_one({
            "project_id": project_id
        })

        if record is None:
            #create new project
            project = Project(project_id=project_id)
            project = await self.create_project(project=project)

            return project
        
        return Project(**record) #convert the dict `record` to a Project Object
    
    async def get_all_projects(self, page: int = 1, page_size: int = 10):
        #count the total number of documents
        total_documents = await self.collection.count_documents({}) #when the filter is empty it returns all the docs
        
        #calculate the total number of pages based on page_size, using pagination is memory_efficient (instead of loading all docs at once)
        total_pages = total_documents // page_size
        if total_documents % page_size > 0:
            total_pages += 1
        
        #A cursor is like a "pointer" to the database results. Instead of loading all documents into memory at once, the cursor fetches only a small portion of data at a time

        cursor = self.collection.find().skip((page-1) * page_size).limit(page_size) #we are skipping some docs to start from a specific page `page` and we only return a limited nb of docs
        projects = []

        async for document in cursor:
            projects.append(
                Project(**document) # to convert the document into a Project Object
                )
            
        return projects, total_pages
        

        

        




    
 



  
