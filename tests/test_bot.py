import os
import pytest
from telegram import InlineKeyboardMarkup, InlineKeyboardButton, Update
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes
from telegram.ext._application import ApplicationBuilder
from unittest.mock import AsyncMock

from bot.app import start, button

@pytest.mark.asyncio
async def test_start_command():
    # Arrange
    mock_update = AsyncMock(Update)
    mock_context = AsyncMock(ContextTypes.DEFAULT_TYPE)
    
    # Act
    await start(mock_update, mock_context)
    
    # Assert
    mock_update.message.reply_text.assert_called_once_with(
        'Вітаю, я бот ГО «Інвестори ЖК «Голосіївська долина», оберіть необхідний розділ:',
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("ℹ️ Інформація про ГО", callback_data='info'), 
             InlineKeyboardButton("📄 Документи ГО", callback_data='documents')],
            [InlineKeyboardButton("✍️ Як вступити в ГО", callback_data='join')],
            [InlineKeyboardButton("❓ Потрібна допомога?", callback_data='help')]
        ])
    )

@pytest.mark.asyncio
async def test_button_info():
    # Arrange
    mock_update = AsyncMock(Update)
    mock_context = AsyncMock(ContextTypes.DEFAULT_TYPE)
    mock_update.callback_query.data = 'info'
    
    # Act
    await button(mock_update, mock_context)
    
    # Assert
    mock_update.callback_query.edit_message_text.assert_called_once_with(
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
        "**Телефони:** 380679849622",
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🔙 Назад", callback_data='start')]]),
        parse_mode='Markdown'
    )

@pytest.mark.asyncio
async def test_button_help():
    # Arrange
    mock_update = AsyncMock(Update)
    mock_context = AsyncMock(ContextTypes.DEFAULT_TYPE)
    mock_update.callback_query.data = 'help'
    
    # Act
    await button(mock_update, mock_context)
    
    # Assert
    mock_update.callback_query.edit_message_text.assert_called_once_with(
        "Потрібна допомога?\n\n"
        "Зв'яжіться через Telegram: [@seksot777](https://t.me/seksot777) або [@fibonacc1_man](https://t.me/fibonacc1_man)",
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🔙 Назад", callback_data='start')]]),
        parse_mode='Markdown'
    )