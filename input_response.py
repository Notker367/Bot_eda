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


def command_processing(massage):
    ml = massage.text.split()
    if len(ml) == 1:
        return
    elif len(ml) != 4:
        print('Неверное кол-во аргументов для command_processing')
        return
    elif len(ml) >= 4 and ml[0] == '/redact':
        redact_processing(ml)
    else:
        print('Error: command_processing')
        return
  # print(ml)


def redact_processing(ml):
    action = ml[1]
    spisok = ml[2]
    food = ml[3]
    if action == tx.text_command_arg('comand', 0):
        action_f = ls.add_to_list
    elif action == tx.text_command_arg('comand', 1):
        action_f = ls.del_to_list
    elif action == tx.text_command_arg('comand', 2):
        action_f = ls.change_to_list
    else:
        print('Error: redact_processing - action')
    action_f(spisok, food)
 #   print(action, spisok, food)
