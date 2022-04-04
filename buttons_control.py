import telebot as tg
import text_arhive as tx


def buttons_create(x):
    markup = tg.types.ReplyKeyboardMarkup(resize_keyboard=True)
    if x == 1: # Для глав меню
        markup.row(tx.text_button("main", 0),
                   tx.text_button("main", 1),
                   tx.text_button("main", 2),)
    elif x == 2: # Для холодельник
        markup.add(tx.text_button('spec', 0))
        markup.row(tx.text_button('redact', 0),
                   tx.text_button('redact', 1),
                   tx.text_button('redact', 2))
    else:
        print('Error: Не верный аргумент в buttons_create')
        return
    return markup
