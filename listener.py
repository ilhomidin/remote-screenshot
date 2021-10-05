import datetime
import os
import socket

import telethon
from PIL import ImageGrab


hostname = socket.gethostname()
client = telethon.TelegramClient(
    "screenshot",
    os.environ["API_ID"],
    os.environ["API_HASH"]
).start(bot_token=os.environ["BOT_TOKEN"])


@client.on(telethon.events.NewMessage(pattern=f"^/screen {hostname}$"))
def send_screenshot(event: telethon.events.NewMessage.Event):
    screenshot = ImageGrab.grab().save(bytearray(), "PNG")
    client.send_file(
        event.message.to_id,
        screenshot,
        caption=f"📺 {hostname}\n 🕒 {datetime.datetime.now()}",
    )


if __name__ == "__main__":
    client.run_until_disconnected()
