import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import os
from pyrogram import Client, filters
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup
)
from pyrogram.types import CallbackQuery
from google_trans_new import google_translator


import pyrogram
logging.getLogger("pyrogram").setLevel(logging.WARNING)

# Get a bot token from botfather
TOKEN = os.environ.get("TOKEN", "")

# Get from my.telegram.org (or @UseTGXBot)
APP_ID = int(os.environ.get("APP_ID", ""))

# Get from my.telegram.org (or @UseTGXBot)
API_HASH = os.environ.get("API_HASH", "")
app = Client(
        "ggt",
        bot_token=TOKEN,api_hash=API_HASH,
            api_id=APP_ID
    )

keyboard = InlineKeyboardMarkup(
    [[
    InlineKeyboardButton("മലയാളം", callback_data="Malayalam"),
    InlineKeyboardButton("தமிழ்", callback_data="Tamil"),
    InlineKeyboardButton("हिन्दी", callback_data="Hindi")
    ],[
    InlineKeyboardButton("ಕನ್ನಡ", callback_data="Kannada"),
    InlineKeyboardButton("తెలుగు", callback_data="Telugu"),
    InlineKeyboardButton("मराठी", callback_data="Marathi")
    ],[
    InlineKeyboardButton("ગુજરાતી", callback_data="Gujarati"),
    InlineKeyboardButton("ଓଡ଼ିଆ", callback_data="Odia"),
    InlineKeyboardButton("বাংলা", callback_data="bn")
    ],[
    InlineKeyboardButton("ਪੰਜਾਬੀ", callback_data="Punjabi"),
    InlineKeyboardButton("فارسی", callback_data="Persian"),
    InlineKeyboardButton("English", callback_data="English")
    ],[
    InlineKeyboardButton("español", callback_data="Spanish"),
    InlineKeyboardButton("français", callback_data="French"),
    InlineKeyboardButton("русский", callback_data="Russian")
    ],[
    InlineKeyboardButton("עִברִית", callback_data="hebrew"),
    InlineKeyboardButton("العربية", callback_data="arabic"),
    ]]
)

@app.on_message(filters.command(['start']))
def start(client, message):
            message.reply_text(text =f"Hello **{message.from_user.first_name }** \n\n __I am simple Google Translater Bot \n I can translate any language to you selected language__",reply_to_message_id = message.message_id , parse_mode="markdown", reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("Support 🇮🇳" ,url="https://t.me/lntechnical") ],
                 [InlineKeyboardButton("Subscribe 🧐", url="https://youtube.com/c/LNtechnical") ]
           ]
        ) )
	
@app.on_message(filters.text & filters.private)
async def echo(client, message):
    await message.reply_text(
        text = "Select language 👇",
        reply_markup = keybord
    )

@app.on_callback_query()
async def translate_text(bot, update):
    tr_text = update.message.reply_to_message.text
    cbdata = update.data
    translator = google_translator()
    translated_text = translator.translate(tr_text, lang_tgt=cbdata)
    await update.message.edit(translated_text)
  	

app.run()
