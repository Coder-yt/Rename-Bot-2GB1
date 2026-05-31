# ------------------------- #
# Don't Remove Credit 
# Ask Doubt @AU_Bot_Discussion 
# Owner @Mr_Mohammed_29 
# ------------------------- #

from motor.motor_asyncio import AsyncIOMotorClient
from config import MONGO_URI
import time


# ------------------------- #
# Don't Remove Credit 
# Ask Doubt @AU_Bot_Discussion 
# Owner @Mr_Mohammed_29 
# ------------------------- #

client = AsyncIOMotorClient(MONGO_URI)

db = client.rename_bot

users = db.users

leaderboard = db.leaderboard


# ------------------------- #
# Don't Remove Credit 
# Ask Doubt @AU_Bot_Discussion 
# Owner @Mr_Mohammed_29 
# ------------------------- #

async def update_leaderboard(user_id):

    await leaderboard.update_one(
        {"user_id": user_id},
        {
            "$inc": {
                "today": 1,
                "weekly": 1,
                "monthly": 1,
                "alltime": 1
            },
            "$set": {
                "user_id": user_id
            }
        },
        upsert=True
    )


# ------------------------- #
# Don't Remove Credit 
# Ask Doubt @AU_Bot_Discussion 
# Owner @Mr_Mohammed_29 
# ------------------------- #

async def get_user(uid):
    return await users.find_one({"_id": uid})

# ------------------------- #
# Don't Remove Credit 
# Ask Doubt @AU_Bot_Discussion 
# Owner @Mr_Mohammed_29 
# ------------------------- #

async def set_user(uid, data):
    await users.update_one(
        {"_id": uid},
        {"$set": data},
        upsert=True
    )


# ------------------------- #
# Don't Remove Credit 
# Ask Doubt @AU_Bot_Discussion 
# Owner @Mr_Mohammed_29 
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
                "banned": False,
                "premium": False
            }
        },
        upsert=True
    )

# ------------------------- #
# Don't Remove Credit 
# Ask Doubt @AU_Bot_Discussion 
# Owner @Mr_Mohammed_29 
# ------------------------- #

async def is_banned(uid):
    user = await get_user(uid)

    return user.get("banned", False) if user else False

# ------------------------- #
# Don't Remove Credit 
# Ask Doubt @AU_Bot_Discussion 
# Owner @Mr_Mohammed_29 
# ------------------------- #

async def get_all_users():
    return await users.find({}).to_list(length=None)

# ------------------------- #
# Don't Remove Credit 
# Ask Doubt @AU_Bot_Discussion 
# Owner @Mr_Mohammed_29 
# ------------------------- #

async def get_premium_status(uid):
    user = await get_user(uid)

    if not user:
        return False

    return user.get("premium", False)

# ------------------------- #
# Don't Remove Credit 
# Ask Doubt @AU_Bot_Discussion 
# Owner @Mr_Mohammed_29 
# ------------------------- #

async def setup_database():
    print("Dᴀᴛᴀʙᴀsᴇ Cᴏɴɴᴇᴄᴛᴇᴅ ✅")

# ------------------------- #
# Don't Remove Credit 
# Ask Doubt @AU_Bot_Discussion 
# Owner @Mr_Mohammed_29 
# ------------------------- #
