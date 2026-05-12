import telebot

TOKEN = "8732190858:AAGgpYEjs6TqBoI6pmsXUBWNOgxx85X5N-0"

bot = telebot.TeleBot(8732190858:AAGgpYEjs6TqBoI6pmsXUBWNOgxx85X5N-0)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Bot is running ✅")

print("Bot Started...")
bot.infinity_polling()
