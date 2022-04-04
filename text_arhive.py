def text_start_eda():
    text = 'Нажми: \nХолодельник - для получения списка того что в холодельнике' \
           '\nПокупки - для списка того что мы регулярно покупаем' \
           '\nЗакупка - для получения списка того что планируем купить'
    return text


def text_for_redact():
    test = 'Выбери действие для редактирования'
    return test


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
    return xl[arg]
