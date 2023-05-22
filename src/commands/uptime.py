from telegram import Update
from telegram.ext import ContextTypes
from time import time
import math

start_time = time()

async def uptime_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
  uptime_total = round(time() - start_time)
  uptime_hours = math.floor(uptime_total / 3600)
  uptime_total -= uptime_hours * 3600
  uptime_minutes = math.floor(uptime_total / 60)
  uptime_total -= uptime_minutes * 60
  uptime_seconds = uptime_total

  if uptime_hours != 0 and uptime_minutes != 0:
    await update.message.reply_text(f"{uptime_hours}h {uptime_minutes}m {uptime_seconds}s")
  elif uptime_hours == 0 and uptime_minutes != 0:
    await update.message.reply_text(f"{uptime_minutes}m {uptime_seconds}s")
  else:
    await update.message.reply_text(f"{uptime_seconds}s")