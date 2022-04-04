import lists as ls
import text_arhive as tx


def buttons_processing_first(message):
    if message.text.strip() == tx.text_button("spec", 0):
        send_text = tx.text_button('spec', 0)
    elif message.text.strip() == tx.text_button("main", 0):
        send_text = ls.text_collector(1)
    elif message.text.strip() == tx.text_button("main", 1):
        send_text = ls.text_collector(2)
    elif message.text.strip() == tx.text_button("main", 2):
        send_text = ls.text_collector(3)
    else:
        send_text = "error buttons_processing_first"
    return send_text
