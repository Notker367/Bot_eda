import telebot
from telebot import types

import lists as ls
import input_response as ir
import buttons_control as bc
import text_arhive as tx

# Создаем экземпляр бота
bot = telebot.TeleBot('5209249131:AAHBQQtPaC9eUhIM3WpqtXkxDm2x4x5Cb5U')


# Команда start
@bot.message_handler(commands=["eda", "back"])
def eda(m, res=False):
    # Добавляем три кнопки
    markup = bc.buttons_create(1)
    bot.send_message(m.chat.id,
                     tx.text_start_eda(),
                     reply_markup=markup)


@bot.message_handler(commands=["redact"])
def redact(m, res=False):
    # Добавляем три кнопки
    markup = bc.buttons_create(2)
    # отправляем на обработку сообщение
    ir.command_processing(m)
    bot.send_message(m.chat.id,
                     tx.text_for_redact(),
                     reply_markup=markup)


# Получение сообщений от юзера
@bot.message_handler(content_types=["text"])
def handle_text(message):
    # Назначаем текст для вывода основываясь на вводе
    send_text = ir.buttons_processing_first(message)
    # Отсылаем юзеру сообщение
    bot.send_message(message.chat.id, send_text)
    print(message)


# Запускаем бота
bot.polling(none_stop=True, interval=0)
