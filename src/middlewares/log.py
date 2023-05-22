from telegram import Update
from telegram.ext import ContextTypes
from dotenv import load_dotenv
from os import getenv

load_dotenv()

log_channel_id = int(getenv("LOG_CHANNEL_ID"))

async def log_middleware(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
  message = update.message
  user = message.from_user
  text = message.text

  log_text = f'User Id: {user.id}\n' + f'First Name: {user.first_name}\n' + f'Last Name: {user.last_name}\n' + f'Usn: @{user.username}'
  border_sticker = "CAACAgUAAxkBAAENmNVkauJ6RHh4CM52E3ax1SugzL_7ZwACLQADqZrmFqa-yO6xA3ODLwQ"
  
  forwarded_message = await message.forward(log_channel_id)
  await forwarded_message.reply_text(log_text)
  await context.bot.send_sticker(log_channel_id, border_sticker)