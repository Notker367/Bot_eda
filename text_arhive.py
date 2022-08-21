def text_start_eda():
    text = f'Нажми: \n{text_button("main",0)} - для получения списка того что в холодельнике' \
           f'\n{text_button("main",1)} - для списка того что мы регулярно покупаем' \
           f'\n{text_button("main",2)} - для получения списка того что планируем купить'
    return text


def text_for_redact(arg=None):
    if arg is None:
        text = 'Выбери действие для редактирования' \
                '\n Структура команды: redact <команда> <список> <текст>' \
                '\n Сейчас работает redact add h\p\z text (одинаковые не добавляет)'
    elif arg == 1:
        text = 'text_for_redact 1'
    else:
        text = 'Error text_for_redact'
    return text


def text_button(list, arg):
    if list == 'main':
        xl = ['Холодельник',
              'Покупки',
              'Закупка']
    elif list == 'redact':
        xl = ['Добавить',
              'Убрать',
              'Изменить']
    elif list == 'spec':
        xl = ['/back',
              'Отчистить всё']
    else:
        print('Error: Неверный аргумент для text_button')
        return
    return xl[arg]


def text_command_arg(list, arg):
    if list == 'comand':
        xl = ['add',
              'del',
              'chg']
    elif list == 'spisok':
        xl = ['h',
              'p',
              'z']
    else:
        print('Error: Неверный аргумент для text_command_arg')
        return
    return xl[arg]
