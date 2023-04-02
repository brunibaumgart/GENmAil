import requests
import lista
import re
import io
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

def output_sender(chat_id):
    send_message(chat_id, 'Resumen de correos:\n')
    with io.open('output.txt', encoding="utf8") as f:
        content = f.read()
    byte_count = 0
    message_chunks = ""
    messages = content.split('Asunto: ')[1:]
    for message in messages:
        # Add the starter of the message back to the beginning of each chunk
        byte_count+= len(message)+len('Asunto: ')+1
        if not byte_count > 4000:
            message_chunks += f'Asunto: {message}\n'
        else:
            send_message(chat_id, message_chunks+'\n')
            message_chunks = f'Asunto: {message}\n'
            byte_count = len(message)+len('Asunto: ')+1
    send_message(chat_id, message_chunks+'\n')

def handle_message(message_text, chat_id, waiting_for_input):
    #global cant that updates everytime it enters here
    global option
    if not waiting_for_input:

        if message_text == '/start':
            send_message(chat_id, '¡Bienvenido! Ahora le voy a solicitar que complete el siguiente formulario/me de sus credenciales.\n'
                                  'Primero necesito su cuenta de gmail y seguido por un espacio su contraseña.\n')
            option='start'
            return True
        elif message_text.lower() == 'ayuda':
            send_message(chat_id, 'Las opciones disponibles son: \n'
                                  'A) Agregar palabras clave, es decir Emails que contengan alguna de las frases guardadas seran mas importantes \nEn caso de enviar mas de una palabra o frase hacerlo seoarado por comas\nPor ej: Futbol,Frases del dia,Gatitos'
                                  'B) Evitar spam, es decir agregar direcciones de correo de las cuales no se quieren recibir resumenes \n'
                                  'C) Agregar remitentes importantes, es decir direcciones de correo en las cuales se quieren recibir resumenes en el momento ocurrido \n'
                                    'D) Agregar remitentes rechazables, es decir direcciones de correo de las cuales no te interesa recibir mails \n'
                                  'E) Enviar resumen de correos \n')
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
        elif message_text.lower() == 'out':
            output_sender(chat_id)

        else:
            send_message(chat_id, 'No entiendo lo que quiere decir. Envíe ayuda para ver las opciones disponibles.')


def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))


def handle_option(message_text, chat_id, option):
    users = lista.parse_json('users.json')
    #handels each option recieven the text and sending another message according to it
    if option == 'a':
        send_message(chat_id, 'Agregando palabra clave: '+ message_text)
        keywords = message_text.split(',')
        for user in users:
            if user["chat_id"] == chat_id:
                for keyword in keywords:
                    user["keywords"].append(keyword)
                lista.save_json(users, 'users.json')
                break
    elif option == 'b':
        spam= message_text.split(',')
        for user in users:
            if user["chat_id"] == chat_id:
                for sp in spam:
                    user["reject_senders"].append(sp)
                lista.save_json(users, 'users.json')
                break
        send_message(chat_id, 'Agregando direccion de correo a la lista de spam: '+ message_text)
    elif option == 'c':
        if not is_valid_email(message_text):
            send_message(chat_id, 'No es una direccion de correo valida.  Envie devuelta por favor')
            return True
        priority_senders = message_text.split(',')
        for user in users:
            if user["chat_id"] == chat_id:
                for senders in priority_senders:
                    user["priority_senders"].append(senders)
                lista.save_json(users, 'users.json')
        send_message(chat_id, 'Agregando direccion de correo a la lista de remitentes importantes: '+ message_text)
    elif option == 'd':
        spam_users= message_text.split(',')
        for user in users:
            if user["chat_id"] == chat_id:
                for sp in spam_users:
                    user["reject_senders"].append(sp)
                lista.save_json(users, 'users.json')
                break
    elif option == 'start':
        gmail = message_text.split(' ')[0]
        password = message_text.split(' ')[1]
        if not is_valid_email(gmail):
            send_message(chat_id, 'No es una direccion de correo valida. Enviar devuelta ambos')
            return True
        else:
            for user in users:
                if user["email"] == gmail:
                    # Si el correo electrónico ya existe, mostramos un mensaje de error al usuario
                    print(f"Ya existe un usuario con correo electrónico '{gmail}'.")
                    break
                else:
                    new_user = {
                        "chat_id": chat_id,
                        "email": gmail,
                        "password": password if password else None,
                        "keywords": [],
                        "priority_senders": [],
                        "reject_keywords": [],
                        "reject_senders": [],
                        "favorite_contact": []
                    }
                    users.append(new_user)
                    lista.save_json(users, 'users.json')
        send_message(chat_id, 'Cuenta de gmail: '+ gmail)
        send_message(chat_id, 'Contraseña: ' + password)
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
                        waiting_for_input = handle_option(message_text, chat_id, option)
                        send_message(chat_id, f'Recibido: {message_text} de la opcion {option}')


if __name__ == '__main__':
    main()
