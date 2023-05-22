from telegram import Update
from telegram.ext import ContextTypes

async def offline_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
  await update.message.reply_text('Saat ini bot sedang offline cuy, ketik /help untuk informasi lebih lanjut')