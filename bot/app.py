import os
from dotenv import load_dotenv
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

load_dotenv()

TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [
        [
            InlineKeyboardButton("ℹ️ Інформація про ГО", callback_data='info'),
            InlineKeyboardButton("📄 Документи ГО", callback_data='documents'),
        ],
        [InlineKeyboardButton("✍️ Як вступити в ГО", callback_data='join')],
        [InlineKeyboardButton("❓ Потрібна допомога?", callback_data='help')],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)
    if update.message:
        await update.message.reply_text('Вітаю, я бот ГО «Інвестори ЖК «Голосіївська долина», оберіть необхідний розділ:', reply_markup=reply_markup)
    elif update.callback_query:
        await update.callback_query.edit_message_text('Вітаю, я бот ГО «Інвестори ЖК «Голосіївська долина», оберіть необхідний розділ:', reply_markup=reply_markup)

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()

    if query.data == 'info':
        text = (
            "9 серпня 2023 р. було зареєстровано Громадську організацію “Інвестори ЖК “Голосіївська долина”, "
            "основною метою якої є сприяння якнайшвидшому отриманню інвесторами речових прав на свої об’єкти інвестування. "
            "ГО – це юридична особа, яка діє в межах та спосіб чинного законодавства України.\n\n"
            "Керівництво ГО – Прищепа Микола та Євсюков Родіон.\n\n"
            "🏛️ **Юридична інформація**\n\n"
            "**Код:** 45326768\n"
            "**Адреса:** Україна, 03022, місто Київ, вулиця Холодноярська, будинок 7/9\n"
            "**Керівник:** Прищепа Микола Миколайович\n"
            "**Діяльність:** 94.99 Діяльність інших громадських організацій, н.в.і.у.\n"
            "**Стан:** зареєстровано\n"
            "**Дата реєстрації:** 09.08.2023\n"
            "**Телефони:** 380679849622"
        )
        keyboard = [[InlineKeyboardButton("🔙 Назад", callback_data='start')]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(text=text, reply_markup=reply_markup, parse_mode='Markdown')

    elif query.data == 'documents':
        text = (
            "Документи ГО:\n\n"
            "1. 📜 [Статут](https://docs.google.com/file/d/1AMbymvqa4-RoIJoaPB9ZlpLIVfeMwnGI/edit?usp=docslist_api&filetype=msword)\n"
            "2. 📑 [Положення членства](https://docs.google.com/file/d/1GTDp3NGbFcs7Cqz5cE8SJbY2guHqSaGV/edit?usp=docslist_api&filetype=msword)"
        )
        keyboard = [[InlineKeyboardButton("🔙 Назад", callback_data='start')]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(text=text, reply_markup=reply_markup, parse_mode='Markdown')

    elif query.data == 'join':
        text = (
            "Для вступу в ГО слід заповнити [Заяву на вступ](https://docs.google.com/file/d/1F4BLRMUGNIL952aYNLh93qN-vvaYjN3Q/edit?usp=docslist_api&filetype=msword) "
            "(роздрукувати, підписати, сфотографувати або відсканувати) та заповнити Форму Google Forms "
            "(тут слід буде завантажити і Вашу заяву, і ще один документ).\n\n"
            "Після виконання зазначених дій формується протокол про вступ, а інвестори долучаються до окремої групи у Телеграмі."
        )
        keyboard = [[InlineKeyboardButton("🔙 Назад", callback_data='start')]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(text=text, reply_markup=reply_markup, parse_mode='Markdown')

    elif query.data == 'help':
        text = (
            "Потрібна допомога?\n\n"
            "Зв'яжіться через Telegram: [@seksot777](https://t.me/seksot777) або [@fibonacc1_man](https://t.me/fibonacc1_man)"
        )
        keyboard = [[InlineKeyboardButton("🔙 Назад", callback_data='start')]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(text=text, reply_markup=reply_markup, parse_mode='Markdown')

    elif query.data == 'start':
        await start(update, context)

def main() -> None:
    application = Application.builder().token(TELEGRAM_TOKEN).build()

    application.add_handler(CommandHandler('start', start))
    application.add_handler(CallbackQueryHandler(button))

    application.run_polling()

if __name__ == '__main__':
    main()