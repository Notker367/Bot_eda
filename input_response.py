import lists as ls


def buttons_processing_first(message):
    if message.text.strip() == 'Холодельник':
        send_text = ls.text_collector(1)
    elif message.text.strip() == 'Покупки':
        send_text = ls.text_collector(2)
    elif message.text.strip() == 'Закупка':
        send_text = ls.text_collector(3)
    else:
        send_text = "error"
    return send_text
