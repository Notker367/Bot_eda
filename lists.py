# Загружаем список регулярных покупок
def get_spisok(x):
    if x == 1:
        file_link = 'data/holodos.txt'
    elif x == 2:
        file_link = 'data/pokypki.txt'
    elif x == 3:
        file_link = 'data/zakypka.txt'
    else:
        print("Error: неверный параметр в get_spisok")
    f = open(file_link, 'r', encoding='UTF-8')
    spisok = f.read().split('\n')
    f.close()
    return spisok


# Собираем сообщение добавляя к каждому эллементу нидекс от 1..
def text_collector(number_spisok):
    spisok = get_spisok(number_spisok)
    work_spisok(spisok.copy)
    spisok_and_index = adder_index(spisok)
    end_text = '\n '.join(spisok_and_index)
    return end_text


def adder_index(lst):
    xl = map(lambda x: str(lst.index(x) + 1) + ' - ' + x, lst)
    return xl


def work_spisok(x=None):
    return x

