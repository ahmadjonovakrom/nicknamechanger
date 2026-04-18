import os
import asyncio
from telethon import TelegramClient
from telethon.tl.functions.account import UpdateProfileRequest

# ======================
# ENV VARIABLES
# ======================
api_id = 38763213
api_hash = "8094774228d8613c4078b6dd480a72f2"

# ======================
# NICKNAMES LIST
# ======================
names = [
    "Ahmadjonov",
    "Mm",
    "Indepented developer",
    "Shirmoynon",
    "Blacky",
    "Supervisor",
    "Mark",
    ".",
    "..",
    "Hey bro",
    "udkm",
    "I love my mom",
    "Not from the moon",
    "Shunchaki",
    "Dave Jones",
    "Mr Jones",
    "Money maker",
    "Chamomile tea",
    "Little dreamer",
]

# ======================
# CLIENT
# ======================
client = TelegramClient("session", api_id, api_hash)

async def main():
    await client.connect()

    print("Bot started successfully!")

    i = 0
    while True:
        name = names[i % len(names)]

        try:
            await client(UpdateProfileRequest(first_name=name))
            print("Changed nickname to:", name)
        except Exception as e:
            print("Error:", e)

        i += 1
        await asyncio.sleep(30)

asyncio.run(main())
