#-------------------------#

#Don't Remove Credit

#Ask Doubt @AU_Bot_Discussion

#Owner @Mr_Mohammed_29

#-------------------------#

from motor.motor_asyncio import AsyncIOMotorClient
from config import MONGO_URI
import time

client = AsyncIOMotorClient(MONGO_URI)
db = client.rename_bot

users = db.users

#-------------------------#

async def get_premium_status(uid):
user = await users.find_one({"_id": uid})
if not user:
return False

if not user.get("premium"):  
    return False  

expiry = user.get("premium_expiry", 0)  

if expiry and time.time() > expiry:  
    await users.update_one(  
        {"_id": uid},  
        {"$set": {"premium": False, "premium_expiry": 0}}  
    )  
    return False  

return True

#-------------------------#

async def get_user(uid):
return await users.find_one({"_id": uid})

async def set_user(uid, data):
await users.update_one(
{"_id": uid},
{"$set": data},
upsert=True
)

#-------------------------#

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

#-------------------------#

async def is_banned(uid):
user = await get_user(uid)
return user.get("banned", False) if user else False

#-------------------------#

async def get_all_users():
return await users.find({}).to_list(length=None)

#-------------------------#

#Don't Remove Credit

#Ask Doubt @AU_Bot_Discussion

#Owner @Mr_Mohammed_29

#-------------------------#
