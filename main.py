import telebot
from telebot import types

import lists

# Создаем экземпляр бота
bot = telebot.TeleBot('5209249131:AAHBQQtPaC9eUhIM3WpqtXkxDm2x4x5Cb5U')





# Команда start
@bot.message_handler(commands=["eda"])
def eda(m, res=False):
    # Добавляем три кнопки
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Холодельник")
    item2 = types.KeyboardButton("Покупки")
    item3 = types.KeyboardButton("Закупка")
    markup.add(item1)
    markup.add(item2)
    markup.add(item3)
    bot.send_message(m.chat.id,
                     'Нажми: \nХолодельник - для получения списка того что в холодельнике'
                     '\nПокупки - для списка того что мы регулярно покупаем'
                     '\nЗакупка - для получения списка того что планируем купить или добавить что-то на следующую',
                     reply_markup=markup)


# Получение сообщений от юзера
@bot.message_handler(content_types=["text"])
def handle_text(message):
    # Если юзер прислал Покупки, выдаем ему список всех продуктов из регулярных покупок
    if message.text.strip() == 'Покупки':
        send_text = lists.text_collector()
    else:
        send_text = "error"
    # Отсылаем юзеру сообщение в его чат
    print(send_text)
    bot.send_message(message.chat.id, send_text)








# Запускаем бота
bot.polling(none_stop=True, interval=0)
