import requests
import json


TOKEN = '6259751667:AAG8OVuM_5rzbfndPPw1vM1Z5bNHAi7oA0U'
URL = f'https://api.telegram.org/bot{TOKEN}/'

waiting_for_input = False
option= ''
def get_updates(offset=None):
    url = URL + 'getUpdates?timeout=100'
    if offset:
        url += f'&offset={offset}'
    response = requests.get(url)
    return json.loads(response.content)

def send_message(chat_id, text):
    url = URL + f'sendMessage?chat_id={chat_id}&text={text}'
    requests.get(url)


user_prefs = {}

def handle_message(message_text, chat_id, waiting_for_input):
    #global cant that updates everytime it enters here
    global option
    if not waiting_for_input:

        if message_text == '/start':
            send_message(chat_id, '¡Bienvenido! Envíe ayuda para ver las opciones disponibles.')
        elif message_text == 'ayuda':
            send_message(chat_id, 'Las opciones disponibles son: \n'
                                  'A) Agregar palabras clave, es decir Emails que contengan alguna de las frases guardadas seran mas importantes \n'
                                  'B) Evitar spam, es decir agregar direcciones de correo de las cuales no se quieren recibir resumenes \n'
                                  'C) Agregar remitentes importantes, es decir direcciones de correo en las cuales se quieren recibir resumenes en el momento ocurrido \n')
        elif message_text == 'a' or message_text == 'A':
            send_message(chat_id, 'Escriba la frase o la palabra clave:\n' )
            option= 'a'
            return True
        elif message_text == 'b' or message_text == 'B':
            send_message(chat_id, 'Escriba la direccion de correo de la cual no desea recibir resumenes:\n' )
            option = 'b'
            return True
        elif message_text == 'c' or message_text == 'C':
            send_message(chat_id, 'Escriba la direccion de correo de la cual desea recibir resumenes en el momento ocurrido:\n' )
            option = 'c'
            return True
        else:
            send_message(chat_id, 'No entiendo lo que quiere decir. Envíe ayuda para ver las opciones disponibles.')

def main():
    global option
    last_update_id = -1
    global waiting_for_input
    while True:
        updates = get_updates(last_update_id)
        if 'result' in updates and updates['result']:
            for update in updates['result']:
                if(last_update_id<update['update_id']):
                    last_update_id = update['update_id']
                    chat_id = update['message']['chat']['id']
                    message_text = update['message']['text']
                    if not waiting_for_input:
                        waiting_for_input = handle_message(message_text, chat_id, waiting_for_input)
                    else:
                        send_message(chat_id, f'Recibido: {message_text} de la opcion {option}')
                        waiting_for_input = False

if __name__ == '__main__':
    main()
