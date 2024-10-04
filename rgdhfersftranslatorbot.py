from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import google.generativeai as genai

genai.configure(api_key='GEMINI API KEY')

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Hi! Send me a message in Telugu (even if it’s written in English), and I will translate it to English.')

def translate(update: Update, context: CallbackContext) -> None:
    text_to_translate = update.message.text

    try:
        response = genai.GenerativeModel(model_name="gemini-1.5-flash").generate_content(f'"{text_to_translate}" \n this text is in telugu i wantu to translate it in english and keep it short... within 50 words')

        translated_text = response.text
        update.message.reply_text(f'Translated to English: {translated_text}')
    except Exception as e:
        update.message.reply_text(f'Sorry, I could not translate the message. Error: {e}')

def main() -> None:
    updater = Updater("TELEGRAM ACCES KEY", use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))

    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, translate))

    updater.start_polling()

    updater.idle()

if __name__ == '__main__':
    main()
