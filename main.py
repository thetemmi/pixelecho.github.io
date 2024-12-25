from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext

# Список ігор
GAMES = {
    "super_mario": {
        "name": "Super Mario Bros.",
        "url": "https://ваш_хостинг/super_mario.html"
    },
    "sonic": {
        "name": "Sonic the Hedgehog",
        "url": "https://emu64.vercel.app/SonicTheHedgehog"
    }
}

# Команда старт
def start(update: Update, context: CallbackContext):
    keyboard = [
        [InlineKeyboardButton("Играть в Super Mario Bros.", url=GAMES["super_mario"]["url"])],
        [InlineKeyboardButton("Играть в Sonic the Hedgehog", url=GAMES["sonic"]["url"])]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text("Привет! Выберите игру для запуска:", reply_markup=reply_markup)

# Основная функция
def main():
    # Замените YOUR_BOT_TOKEN на токен вашего бота
    updater = Updater("YOUR_BOT_TOKEN", use_context=True)

    # Обработчики команд
    updater.dispatcher.add_handler(CommandHandler("start", start))

    # Запуск бота
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
