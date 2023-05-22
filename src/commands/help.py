from telegram import Update
from telegram.constants import ParseMode
from telegram.ext import ContextTypes
from time import sleep

async def help_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
  text = 'Jika ada pertanyaan/saran bisa hubungi admin [Fears](https://t.me/apakamukangen) atau admin [\#DDF](https://t.me/deepdarkfearss) lainnya'
  sticker = 'CAACAgUAAxkBAAENmJlkareKz8RG6N1e9b6CRe8SRNtYwgAC8xMAAgM8-VS58bBFB1dalS8E'

  await update.message.reply_text(text, parse_mode=ParseMode.MARKDOWN_V2, disable_web_page_preview=True)
  sleep(1)
  await update.message.reply_sticker(sticker)