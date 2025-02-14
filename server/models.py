from dataclasses import dataclass
from pymongo import MongoClient
from typing import List
from enum import Enum
import os

class UserRole(Enum):
    ADMIN = "admin"
    MANAGER = "manager"
    USER = "user"
@dataclass
class UserPreferences:
    timezone: str

@dataclass
class User:
    username: str
    password: str
    roles: List[UserRole]
    preferences: UserPreferences
    active: bool = True
    created_ts: float

class UserModel:
    def __init__(self):
        mongo_uri = os.getenv("MONGO_URI", "mongodb://localhost:27017")
        self.client = MongoClient(mongo_uri)
        self.db = self.client["my_database"]
        self.collection = self.db["users"]

    def create_user(self, user: User):
        user_dict = user.__dict__
        user_dict["preferences"] = user.preferences.__dict__
        result = self.collection.insert_one(user_dict)
        return str(result.inserted_id)

    def get_user(self, username: str):
        user_dict = self.collection.find_one({"username": username})
        if user_dict:
            user_dict["preferences"] = UserPreferences(**user_dict["preferences"])
            return User(**user_dict)
        return None

    def update_user(self, username: str, update_data: dict):
        result = self.collection.update_one({"username": username}, {"$set": update_data})
        return result.modified_count

    def delete_user(self, username: str):
        result = self.collection.delete_one({"username": username})
        return result.deleted_count