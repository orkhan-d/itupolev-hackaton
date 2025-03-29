from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = "7372916582:AAF1415L-jgBxu4NhirCiXpD_f7rknWFuZ8"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_text = (
        "Вы пидор?\n"
    )
    

    keyboard = [
        [
            InlineKeyboardButton("Рассписание", web_app=WebAppInfo(url="https://kai.ru/raspisanie")),
            InlineKeyboardButton("Сайт каи", web_app=WebAppInfo(url="https://ваше-мини-приложение2.com")),
        ],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)


    await update.message.reply_text(
        text=message_text,
        reply_markup=reply_markup,
        parse_mode='Markdown'
    )

def main():
    application = Application.builder().token(TOKEN).build()
    
    application.add_handler(CommandHandler("start", start))
    
    application.run_polling()

if __name__ == "__main__":
    main()