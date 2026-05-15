# ------------------------- #
# Don't Remove Credit 
# Ask Doubt @AU_Bot_Discussion 
# Owner @Mr_Mohammed_29 
# ------------------------- #
from motor.motor_asyncio import AsyncIOMotorClient
from config import MONGO_URI
import time

client = AsyncIOMotorClient(
    MONGO_URI,
    maxPoolSize=50,
    minPoolSize=10,
    serverSelectionTimeoutMS=5000
)
db = client.rename_bot

users = db.users

# ------------------------- #
# CREATE INDEXES
# ------------------------- #

async def setup_database():
    await users.create_index("premium")
    await users.create_index("banned")
   
# ------------------------- #

async def get_user(uid):
    return await users.find_one({"_id": uid})

async def set_user(uid, data):
    await users.update_one(
        {"_id": uid},
        {"$set": data},
        upsert=True
    )

# ------------------------- #

async def add_user(uid):
    await users.update_one(
        {"_id": uid},
        {
            "$setOnInsert": {
                "prefix": "",
                "suffix": "",
                "caption": "",
                "thumb": "",
                "banned": False
            }
        },
        upsert=True
    )
# ------------------------- #

async def is_banned(uid):
    user = await get_user(uid)
    return user.get("banned", False) if user else False

# ------------------------- #

async def get_all_users():
    return await users.find({}).to_list(length=None)
    
# ------------------------- #
# Don't Remove Credit 
# Ask Doubt @AU_Bot_Discussion 
# Owner @Mr_Mohammed_29 
# ------------------------- #
