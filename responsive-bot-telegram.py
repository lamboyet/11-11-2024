'''

import requests

def send_telegram_message(token, chat_id, message):
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {'chat_id':chat_id,
               'text': message
               }
    response = requests.post(url,data=payload)
    return response.json()

bot_token = "7793875485:AAEp1utsvSvGbXe-u7Id6Pd_M0dDLv03KyI"
chat_id ="-4514881782"
message = "REMINDER"

response = send_telegram_message(bot_token, chat_id, message)

'''

from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN: Final = '7793875485:AAEp1utsvSvGbXe-u7Id6Pd_M0dDLv03KyI'
BOT_USERNAME = '@thesecondpythonhippobot'


# commands
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hello thanks for chatting with me. I am bot')


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('i am bot please type something so i can respond')


async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('This is a custom command')


# responses

def handle_response(text: str) -> str:
    processed: str = text.lower()

    if 'hello' in processed:
        return 'Hi!'
    if 'how are you?' in processed:
        return 'I am good. How are you feeling today?'

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text

    print(f'User({update.message.chat.id}) in {message_type}: "{text}"')
    if message_type == 'group':
        if BOT_USERNAME in text:
            new_text: str = text.replace(BOT_USERNAME, '').strip()
            response: str = handle_response(new_text)
        else:
            return
    else:
        response: str = handle_response(text)

        print('Bot:', response)
        await update.message.reply_text(response)

async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
        print(f'Update {update} caused error {context.error}')

if __name__ == '__main__':
        print('Starting bot...')
        app = Application.builder().token(TOKEN).build()

        # commands
        app.add_handler(CommandHandler('start', start_command))
        app.add_handler(CommandHandler('help', help_command))
        app.add_handler(CommandHandler('custom', custom_command))

        # messages

        app.add_handler(MessageHandler(filters.TEXT, handle_message))

        # errors

        app.add_error_handler(error)

        print('Polling...')
        app.run_polling(poll_interval=3)
