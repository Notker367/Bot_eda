# Загружаем список регулярных покупок
def get_pokypki():
    f = open('data/pokypki.txt', 'r', encoding='UTF-8')
    pokypki = f.read().split('\n')
    f.close()
    return pokypki


# Собираем сообщение добавляя к каждому эллементу нидекс от 1..
def text_collector():
    pokypki = get_pokypki()
    pokypki = adder_index(pokypki)
    end_text = '\n '.join(pokypki)
    # send_text2 = *pokypki
    return end_text


def adder_index(lst):
    interact_index = [range(1, len(lst))]
    xl = map(lambda x: str(lst.index(x) + 1) + ' - ' + x, lst)
    return xl
