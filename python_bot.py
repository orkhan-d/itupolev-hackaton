from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = "7372916582:AAF1415L-jgBxu4NhirCiXpD_f7rknWFuZ8"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_text = "Добро пожаловать\n"
    
    keyboard = [
        [
            InlineKeyboardButton("Наш проект", 
                               web_app=WebAppInfo(url="https://example.com"))
        ],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.effective_message.reply_text(
        text=message_text,
        reply_markup=reply_markup
    )

def main():
    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.run_polling()

if __name__ == "__main__":
    main()
