import text_arhive as tx


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
    # work_spisok(spisok.copy)
    spisok_and_index = adder_index(spisok)
    end_text = '\n '.join(spisok_and_index)
    return end_text


def adder_index(lst):
    xl = map(lambda x: str(lst.index(x) + 1) + ' - ' + x, lst)
    return xl


def work_spisok(x):
    if x == tx.text_command_arg('spisok', 0):
        file_link = 'data/holodos.txt'
    elif x == tx.text_command_arg('spisok', 1):
        file_link = 'data/pokypki.txt'
    elif x == tx.text_command_arg('spisok', 2):
        file_link = 'data/zakypka.txt'
    else:
        print("Error: неверный параметр в work_spisok :", x)
        return
    return file_link


def add_to_list(spisok, food):
    file = work_spisok(spisok)
    if check_have_in_file(spisok, food):
        print("Уже есть в файле")
        return
    f = open(file, 'a', encoding='UTF-8')
    f.write(f"\n{food}")
    # print(f.read())
    f.close()
    #  print(file, food)
    return


def del_to_list(spisok, food):
    file = work_spisok(spisok)

    return


def cahge_to_list(spisok, food):
    file = work_spisok(spisok)

    return


def check_have_in_file(spisok, food):
    file = work_spisok(spisok)
    f = open(file, 'r', encoding='UTF-8')
    spisok_l = f.read().split('\n')
    if food in spisok_l:
        # print('это уже есть')
        return True
    elif food not in spisok_l:
        # print('norm')
        return False
    else:
        print('Error: check_have_in_file', spisok_l, '+', food)
        return
