from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters
from middlewares.log import log_middleware
from commands.offline import offline_handler
from commands.help import help_handler
from commands.uptime import uptime_handler
from dotenv import load_dotenv
from os import getenv

load_dotenv()

bot_token = getenv("BOT_TOKEN")

app = ApplicationBuilder().token(bot_token).build()

app.add_handler(MessageHandler(filters.ALL, log_middleware), group=1)

app.add_handler(CommandHandler(["start", "enablelive", "disablelive", "enablerank", "disablerank", "changetitle"], offline_handler))
app.add_handler(CommandHandler("help", help_handler))
app.add_handler(CommandHandler("uptime", uptime_handler))

if getenv("DEVELOPMENT"):
  app.run_polling()

from flask import Flask, request

server = Flask(__name__)
port = int(getenv("PORT", '8443'))
secret_token = getenv("SECRET_TOKEN")
webhook_url = getenv("WEBHOOK_URL")

@server.route('/webhook', methods=['POST'])
def webhook_handler():
  json_string = request.stream.read().decode('utf-8')
  update = Update.de_json(json.loads(json_string), app)
  app.process_update(update)

  return 'ok', 200

app.run_webhook(
  listen="0.0.0.0",
  port=port,
  secret_token=secret_token,
  webhook_url=webhook_url
)