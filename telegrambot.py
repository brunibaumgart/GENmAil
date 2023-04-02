import requests
import json
import re
import io
import json_manager
import os
from mailscraper import parseo
import sys


TOKEN = '6259751667:AAG8OVuM_5rzbfndPPw1vM1Z5bNHAi7oA0U'
URL = f'https://api.telegram.org/bot{TOKEN}/'

sys.stdin.reconfigure(encoding='utf-8')
sys.stdout.reconfigure(encoding='utf-8')

waiting_for_input = False
option= ''

# def our_gmail(gmail):
#     return gmail in array_gmail
#VERRRRRR
def get_updates(offset=None):
    url = URL + 'getUpdates?timeout=100'
    if offset:
        url += f'&offset={offset}'
    response = requests.get(url)
    return json.loads(response.content)

def send_message(chat_id, text):
    if(text==None):
        return
    url = URL + f'sendMessage?chat_id={chat_id}&text={text}'
    requests.get(url)


user_prefs = {}

def output_sender(chat_id):
    for cuenta in json_manager.obtener_cuentas_por_chat_id(chat_id):
        # subprocess.run(['python', './mailscraper.py', cuenta["email"], str(cuenta["keywords"]), str(cuenta["reject_keywords"]), str(cuenta["priority_senders"]), str(cuenta["reject_senders"])])
        parseo(cuenta["email"], cuenta["keywords"], cuenta["reject_keywords"], cuenta["priority_senders"], cuenta["reject_senders"], cuenta["favorite_contact"])
        if os.path.getsize('output.txt') == 0:
            send_message(chat_id, 'No hay correos nuevos')
            return
        with io.open('output.txt', encoding="latin-1") as f:
            content = f.read()
        send_message(chat_id, 'Resumen de correos:\n')
        byte_count = 0
        message_chunks = ""
        messages = content.split('Asunto: ')[0:]
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
            send_message(chat_id, '¡Bienvenido! Ahora le voy a solicitar que me de sus credenciales para poder ayudarlo con sus mails. Luego puede enviar "ayuda" para ver las diferentes personalizaciones posibles\n'
                                  'Primero necesito su cuenta de gmail y seguido por un espacio su contraseña.\n')
            option='start'
            return True
        elif message_text.lower() == 'ayuda':
            send_message(chat_id, 'Las opciones disponibles son: \n'
                                  'A) Acceder a tu output de mails resumidos \n'
                                  'B) Evitar spam, es decir agregar direcciones de correo de las cuales no se quieren recibir resumenes \n'
                                  'C) Agregar remitentes importantes, es decir direcciones de correo en las cuales se quieren recibir resumenes en el momento ocurrido \n'
                                  'D) Agregar palabras clave, es decir Emails que contengan alguna de las frases guardadas seran mas importantes \n'
                                  'E) Eliminar palabras clave\n'
                                  'F) Agregar palabras que quieras evitar \n'
                                  'G) Eliminar palabras que quieras evitar \n' 
                                  'H) Eliminar direcciones favoritas \n'
                                  'I) Eliminar direcciones de correo marcadas como spam \n'
                                  'J) Mostrar todas tus cuentas (D) \n'
                                  '/start para volver a ingresar una cuenta \n'
                                  'K) Eliminar TODAS las cuentas (D) \n')
        elif message_text == 'd' or message_text == 'D':
            send_message(chat_id, 'Escriba el mail y seguido por un espacio la frase o la palabra clave:\n' )
            send_message(chat_id, json_manager.print_account_params_by_chat_id(chat_id, "keywords"))
            option= 'd'
            return True
        elif message_text == 'b' or message_text == 'B':
            send_message(chat_id, 'Escriba su mail y seguido por un espacio la direccion de correo de la cual no desea recibir resumenes:\n' )
            send_message(chat_id, json_manager.print_account_params_by_chat_id(chat_id, "reject_senders"))
            option = 'b'
            return True
        elif message_text == 'c' or message_text == 'C':
            send_message(chat_id, 'Escriba su mail y seguido por un espacio la direccion de correo de la cual desea recibir resumenes en el momento ocurrido:\n' )
            send_message(chat_id, json_manager.print_account_params_by_chat_id(chat_id, "priority_senders"))
            option = 'c'
            return True
        elif message_text.lower() == 'a':
            output_sender(chat_id)
        elif message_text.lower() == 'e':
            send_message(chat_id, 'Elimine alguna de las siguientes palabras clave escribiendo el mail, un espacio y la palabra clave:\n')
            send_message(chat_id, json_manager.print_account_params_by_chat_id(chat_id, "keywords"))
            option = 'e'
            return True

        elif message_text.lower() == 'f':
            send_message(chat_id,
                         'Agregue alguna de las siguientes palabras que quieras evitar escribiendo tu mail, un espacio y la palabra a evitar:\n')
            send_message(chat_id, json_manager.print_account_params_by_chat_id(chat_id, "reject_keywords"))
            option = 'f'
            return True

        elif message_text.lower() == 'g':
            send_message(chat_id,
                         'Elimine alguna de las siguientes palabras que ya no quieras evitar escribiendo tu mail, un espacio y la palabra a dejar de evitar:\n')
            send_message(chat_id, json_manager.print_account_params_by_chat_id(chat_id, "reject_keywords"))
            option = 'g'
            return True

        elif message_text.lower() == 'h':
            send_message(chat_id,
                         'Elimine alguna de las siguientes palabras que ya no quieras evitar escribiendo tu mail, un espacio y la palabra a dejar de evitar:\n')
            send_message(chat_id, json_manager.print_account_params_by_chat_id(chat_id, "reject_keywords"))
            option = 'h'
            return True

        elif message_text.lower() == 'i':
            send_message(chat_id, 'Escriba su mail y seguido por un espacio la direccion de correo de la cual desea volver a recibir resumenes:\n')
            option = 'i'
            return True
        elif message_text.lower() == 'j':
            json_manager.print_accounts_by_chat_id(chat_id)
        elif message_text.lower() == 'k':
            json_manager.reset_json()


        else:
            send_message(chat_id, 'No entiendo lo que quiere decir. Envíe ayuda para ver las opciones disponibles.')


def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))


def handle_option(message_text, chat_id, option):
    #handels each option recieven the text and sending another message according to it
    if option == 'd':
        gmail = message_text.split(' ')[0]
        keyword = message_text.split(' ')[1]
        if not is_valid_email(gmail):
            send_message(chat_id, 'No es una direccion de correo valida. Envie devuelta por favor')
            return True
        json_manager.update_account_by_email(gmail,"keywords",keyword,True)
        send_message(chat_id, 'Agregando palabra clave: '+ message_text)


    elif option == 'b':
        gmail = message_text.split(' ')[0]
        reject_senders = message_text.split(' ')[1]
        if not is_valid_email(gmail) or not is_valid_email(reject_senders):
            send_message(chat_id, 'No es una direccion de correo valida. Envie devuelta por favor')
            return True
        json_manager.update_account_by_email(gmail, "reject_senders", reject_senders, True)
        send_message(chat_id, 'Agregando direccion de correo a la lista de spam: '+ message_text)


    elif option == 'c':
        gmail = message_text.split(' ')[0]
        favourite_address = message_text.split(' ')[1]
        if not is_valid_email(gmail):
            send_message(chat_id, 'No es una direccion de correo valida. Envie devuelta por favor')
            return True
        json_manager.update_account_by_email(gmail, "favorite_contact", favourite_address, True)
        send_message(chat_id, 'Agregado remitente importante: ' + favourite_address)


    elif option == 'start':
        if message_text.count(' ') != 1:
            send_message(chat_id, 'No es una direccion de correo con contraseña valida. Enviar devuelta ambos')
            return True
        gmail = message_text.split(' ')[0]
        password = message_text.split(' ')[1]
        if not is_valid_email(gmail):
            send_message(chat_id, 'No es una direccion de correo valida. Enviar devuelta ambos')
            return True
        # if not our_gmail(gmail):
        #     send_message(chat_id, 'No es una direccion de correo de las que les dimos. Enviar devuelta ambos')
        #     return True
        json_manager.agregar_cuenta(chat_id, gmail , password)
        send_message(chat_id, 'Cuenta de gmail: '+ gmail)
        send_message(chat_id, 'Contraseña: ' + password)


    elif option == 'e':
        gmail = message_text.split(' ')[0]
        keyword = message_text.split(' ')[1]
        json_manager.update_account_by_email(gmail, "keywords", keyword, False)
        send_message(chat_id, 'Eliminada palabra clave: ' + keyword)

    elif option == 'f':
        gmail = message_text.split(' ')[0]
        reject_keywords = message_text.split(' ')[1]
        if not is_valid_email(gmail):
            send_message(chat_id, 'No es una direccion de correo valida. Envie devuelta por favor')
            return True
        json_manager.update_account_by_email(gmail, "reject_keywords", reject_keywords, True)
        send_message(chat_id, 'Agregado palabra a evitar: ' + reject_keywords)

    elif option == 'g':
        gmail = message_text.split(' ')[0]
        reject_keywords = message_text.split(' ')[1]
        if not is_valid_email(gmail):
            send_message(chat_id, 'No es una direccion de correo valida. Envie devuelta por favor')
            return True
        json_manager.update_account_by_email(gmail, "reject_keywords", reject_keywords, False)
        send_message(chat_id, 'Eliminada palabra a evitar: ' + reject_keywords)

    elif option == 'h':
        gmail = message_text.split(' ')[0]
        favourite_address = message_text.split(' ')[1]
        if not is_valid_email(gmail):
            send_message(chat_id, 'No es una direccion de correo valida. Envie devuelta por favor')
            return True
        json_manager.update_account_by_email(gmail, "favorite_contact", favourite_address, False)
        send_message(chat_id, 'Eliminada direccion como importante: ' + favourite_address)

    elif option == 'i':
        gmail = message_text.split(' ')[0]
        reject_senders = message_text.split(' ')[1]
        if not is_valid_email(gmail):
            send_message(chat_id, 'No es una direccion de correo valida. Envie devuelta por favor')
            return True
        json_manager.update_account_by_email(gmail, "reject_senders", reject_senders, False)
        send_message(chat_id, 'elminando direccion de correo de la lista de spam: ' + message_text)


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
                        #send_message(chat_id, f'Recibido: {message_text} de la opcion {option}')


if __name__ == '__main__':
    main()

