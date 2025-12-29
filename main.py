import telebot
from flask import Flask, request

BOT_TOKEN = "8216372386:AAGY2XW3SpGxRWDMR2pnyzGijJj1lN4rrUQ"
GROUP_CHAT_ID = -5337188658  # replace later

bot = telebot.TeleBot(BOT_TOKEN)
app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "Bot is running"

@app.route(f"/{BOT_TOKEN}", methods=["POST"])
def webhook():
    json_str = request.get_data().decode("UTF-8")
    update = telebot.types.Update.de_json(json_str)
    bot.process_new_updates([update])
    return "OK", 200

@bot.message_handler(content_types=["text", "photo", "video", "document", "audio"])
def forward_message(message):
    bot.forward_message(
        GROUP_CHAT_ID,
        message.chat.id,
        message.message_id
    )

    bot.reply_to(
        message,
        "❤️ Thanks my friend! Your content just reached ABDY — welcome to the squad!"
    )

if __name__ == "__main__":
    bot.remove_webhook()
    app.run(host="0.0.0.0", port=10000)