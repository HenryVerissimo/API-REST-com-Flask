import asyncio

from .mongodb_connection import MongoCollection
from datetime import datetime

from os import getenv
from dotenv import load_dotenv

load_dotenv()

log_db_uri = getenv("LOG_DB_URI")
log_db = getenv("LOG_DB")
log_collection = getenv("LOG_COLLECTION")


class MongoLog:
    def __init__(self, collection: MongoCollection) -> None:
        self.__collection = collection


    async def log_info(self, file_name: str, message: str) -> None:
        info = {
            "level": "INFO",
            "message": message,
            "file_name": file_name,
            "date": datetime.utcnow()    
        }

        async with self.__collection as con:
            await con.insert_one(info)

    async def log_error(self, file_name: str, message: str) -> None:
        info = {
            "level": "ERROR",
            "message": message,
            "file_name": file_name,
            "date": datetime.utcnow()
        }

        async with self.__collection as con:
            await con.insert_one(info)


mongo_collection = MongoCollection(log_db_uri, log_db, log_collection)

def log_info(file_name: str, message: str) -> None:
    asyncio.run(MongoLog(mongo_collection).log_info(file_name, message))

def log_error(file_name:str, message: str) -> None:
    asyncio.run(MongoLog(mongo_collection).log_error(file_name, message))
