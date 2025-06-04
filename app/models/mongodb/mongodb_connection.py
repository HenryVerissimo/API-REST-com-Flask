from pymongo import AsyncMongoClient


class MongoCollection:
    def __init__(self, db_uri, database_name:str, collection_name: str):
        self.db_uri = db_uri
        self.database_name = database_name
        self.collection_name = collection_name

        self.client = None
        self.database = None
        self.collection = None
    
    async def connect_to_database(self):

        self.client = AsyncMongoClient(self.db_uri)
        self.database = self.client[self.database_name]
        self.collection = self.database[self.collection_name]

    async def __aenter__(self) -> object:
        await self.connect_to_database()
        return self.collection
    
    async def __aexit__(self, exc_type, exc_val, exc_tb) -> None:
        await self.client.close()
