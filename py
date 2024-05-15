pip install python-telegram-bot

from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Токен вашего бота
TOKEN = "6460798601:AAHPXNYNdpB6YwexAHB0X_xz4tJJ1eTV8CE
"

# Словарь продуктов и их цен
products = {
    "морковка": 50,
    "картошка": 30,
    "лук": 40,
    "веревка": 20,
    "щавель": 60
}

# Функция обработки команды /start
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Привет! Я бот для продажи продуктов. Выбери продукт, который хочешь купить:\n"
                              "/морковка\n/картошка\n/лук\n/веревка\n/щавель")

# Функция обработки выбора продукта
def select_product(update: Update, context: CallbackContext) -> None:
    product = update.message.text.replace("/", "")
    if product in products:
        update.message.reply_text(f"Вы выбрали {product}. Цена: {products[product]} рублей.")
    else:
        update.message.reply_text("Извините, такого продукта у нас нет.")

# Основная функция
def main() -> None:
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.regex(r'^/(морковка|картошка|лук|веревка|щавель)$'), select_product))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
