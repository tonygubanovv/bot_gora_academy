from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler

# Функция, которая будет выполняться при команде /start
async def start(update: Update, context):
    await update.message.reply_text('Привет! Стартуем')

# Основная функция для запуска бота
def main():
    # Замените 'YOUR_TOKEN' на токен вашего бота
    app = ApplicationBuilder().token('7437201314:AAGUEOV9TNMUrm-s7vHgrJAergloSxrnww8').build()

    # Добавляем обработчик команды /start
    app.add_handler(CommandHandler('start', start))

    # Запускаем бота
    app.run_polling()

if __name__ == '__main__':
    main()
