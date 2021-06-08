import sys
from os import execl
from time import sleep

from . import BOTLOG, BOTLOG_CHATID, HEROKU_APP, bot
from telethon import TelegramClient, events

chat= "@HeXamonbot"

@bot.on(events.NewMessage(chats=chat))
async def my_event_handler(event):
      if 'A wild Rayquaza' in event.raw_text:
           await bot.disconnect()
           execl(sys.executable, sys.executable, *sys.argv)
