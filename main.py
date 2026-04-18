import os
import asyncio
from telethon import TelegramClient
from telethon.tl.functions.account import UpdateProfileRequest

# ======================
# ENV VARIABLES
# ======================
api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")

# ======================
# NICKNAMES LIST
# ======================
names = [
    "Akrom ⚡",
    "Akrom 🚀",
    "Akrom 🔥",
    "Akrom 👑"
]

# ======================
# CLIENT
# ======================
client = TelegramClient("session", api_id, api_hash)

async def main():
    await client.start()

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