import datetime
import os
import io
import socket

import telethon
from PIL import ImageGrab


hostname = socket.gethostname()
client = telethon.TelegramClient(
    telethon.sessions.MemorySession(),
    os.environ["API_ID"],
    os.environ["API_HASH"],
).start(bot_token=os.environ["BOT_TOKEN"])


@client.on(telethon.events.NewMessage(pattern=f"^/screen {hostname}$"))
async def send_screenshot(event: telethon.events.NewMessage.Event):
    storage = io.BytesIO()
    ImageGrab.grab().save(storage, "PNG")
    await client.send_file(
        event.chat_id,
        storage.getvalue(),
        reply_to=event.message.id,
        caption=f"📺 `{hostname}`\n🕒 {datetime.datetime.now()}",
    )


if __name__ == "__main__":
    client.run_until_disconnected()
