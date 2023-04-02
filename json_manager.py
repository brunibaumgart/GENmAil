import json
import telegrambot

# Definimos el nombre del archivo JSON donde vamos a guardar los datos
JSON_FILE = "datos.json"


def cargar_datos():
    # Cargamos los datos desde el archivo JSON y los devolvemos como un diccionario
    try:
        with open(JSON_FILE, "r") as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        # Si el archivo no existe, devolvemos un diccionario vacío
        return {}


def guardar_datos(datos):
    # Guardamos los datos en el archivo JSON
    with open(JSON_FILE, "w") as archivo:
        json.dump(datos, archivo)


def agregar_cuenta(chat_id, email, password):
    # Generamos un nuevo ID para la cuenta
    datos = cargar_datos()
    nuevo_id = str(len(datos) + 1)

    for cuenta in datos.values():
        if cuenta["email"] == email:
            print( "Ya existe una cuenta con ese email.")
            return

    # Creamos la nueva cuenta con los datos recibidos y la agregamos al diccionario
    nueva_cuenta = {
        "chat_id": chat_id,
        "email": email,
        "password": password,
        "keywords": [],
        "priority_senders": [],
        "reject_keywords": [],
        "reject_senders": [],
        "favorite_contact": []
    }
    datos[nuevo_id] = nueva_cuenta

    # Guardamos los datos actualizados en el archivo JSON
    guardar_datos(datos)

    # Devolvemos el ID generado para la cuenta
    return nuevo_id


def modificar_cuenta(id_cuenta, **nuevos_datos):
    # Modificamos la cuenta correspondiente al ID recibido con los nuevos datos recibidos
    datos = cargar_datos()
    cuenta = datos.get(id_cuenta)
    if cuenta:
        cuenta.update(nuevos_datos)
        datos[id_cuenta] = cuenta
        guardar_datos(datos)
        return True
    else:
        return False

#function that erases datos.json and then creates a new one with only {} inside
def reset_json():
    with open(JSON_FILE, "w") as archivo:
        json.dump({}, archivo)
def obtener_cuenta(id_cuenta):
    # Devolvemos la cuenta correspondiente al ID recibido
    datos = cargar_datos()
    return datos.get(id_cuenta)

#En cada objeto del json, compruebo coincidencias de chat_id. Si coincide es porque hay más de un mail address propio.
def obtener_cuentas_por_chat_id(chat_id):
    # Devolvemos la cuenta correspondiente al ID recibido
    datos = cargar_datos()
    cuentas = []
    for cuenta in datos.values():
        if cuenta["chat_id"] == chat_id:
            cuentas.append(cuenta)
    return cuentas



def eliminar_cuenta(id_cuenta):
    # Eliminamos la cuenta correspondiente al ID recibido
    datos = cargar_datos()
    if id_cuenta in datos:
        del datos[id_cuenta]
        guardar_datos(datos)
        return True
    else:
        return False

def update_account_by_email(email, attribute, value, add=True):
    # Buscar objeto en el JSON
    data=cargar_datos()
    account_id = None
    for key in data:
        if data[key]["email"] == email:
            account_id = key
            break

    if account_id is None:
        print(f"No existe una cuenta asociada a {email}")
    else:
        # Verificar si el valor ya existe
        if not add and value not in data[account_id][attribute]:
            print(f"El valor '{value}' no se encuentra en la lista de {attribute}")
            return
        elif add and value in data[account_id][attribute]:
            print(f"El valor '{value}' ya se encuentra en la lista de {attribute}")
            return

        # Actualizar el valor
        if add:
            print(f"Agregando {value} a {attribute} de {email}")
            data[account_id][attribute].append(value)
        else:
            data[account_id][attribute].remove(value)

        # Guardar cambios en el archivo
        with open('datos.json', 'w') as file:
            json.dump(data, file)

def get_param_arr_by_email(param_name, email, chat_id):
    to_print=""
    data = cargar_datos()
    for obj in data.values():
        if obj["email"] == email:
            to_print+=email
            to_print+=": "
            if obj[param_name] == []:
                to_print+="  "
                telegrambot.send_message(chat_id, to_print)
            else:
                for param in obj[param_name]:
                    to_print+=param
                    to_print+=" "
                telegrambot.send_message(chat_id, to_print)

    return None

def print_account_params_by_chat_id(chat_id, param_name, all=True):
    data = cargar_datos()
    for obj in data.values():
        if obj["chat_id"] == chat_id:
            get_param_arr_by_email(param_name, obj["email"], chat_id)
    return None

def print_accounts_by_chat_id(chat_id):
    data = cargar_datos()
    for obj in data.values():
        if obj["chat_id"] == chat_id:
            telegrambot.send_message(chat_id, obj)
    return None

def get_param_and_email_by_chat_id(chat_id):
    data = cargar_datos()
    for obj in data.values():
        if obj["chat_id"] == chat_id:
            return obj["email"], obj["keywords"]
    return None, None


def agregar_keyword(chat_id, keyword):
    with open('config.json', 'r') as f:
        data = json.load(f)

    if chat_id not in data:
        return f"No se encontró el chat_id {chat_id} en la base de datos."

    data[chat_id]['keywords'].append(keyword)

    with open('config.json', 'w') as f:
        json.dump(data, f, indent=2)

    return f"Se agregó la keyword {keyword} al chat_id {chat_id}."


def eliminar_keyword(chat_id, keyword):
    with open('config.json', 'r') as f:
        data = json.load(f)

    if chat_id not in data:
        return f"No se encontró el chat_id {chat_id} en la base de datos."

    if keyword not in data[chat_id]['keywords']:
        return f"No se encontró la keyword {keyword} en el chat_id {chat_id}."

    data[chat_id]['keywords'].remove(keyword)

    with open('config.json', 'w') as f:
        json.dump(data, f, indent=2)

    return f"Se eliminó la keyword {keyword} del chat_id {chat_id}."


def agregar_reject_keyword(chat_id, reject_keyword):
    with open('config.json', 'r') as f:
        data = json.load(f)

    if chat_id not in data:
        return f"No se encontró el chat_id {chat_id} en la base de datos."

    data[chat_id]['reject_keywords'].append(reject_keyword)

    with open('config.json', 'w') as f:
        json.dump(data, f, indent=2)

    return f"Se agregó el reject_keyword {reject_keyword} al chat_id {chat_id}."


def eliminar_reject_keyword(chat_id, reject_keyword):
    with open('config.json', 'r') as f:
        data = json.load(f)

    if chat_id not in data:
        return f"No se encontró el chat_id {chat_id} en la base de datos."

    if reject_keyword not in data[chat_id]['reject_keywords']:
        return f"No se encontró el reject_keyword {reject_keyword} en el chat_id {chat_id}."

    data[chat_id]['reject_keywords'].remove(reject_keyword)

    with open('config.json', 'w') as f:
        json.dump(data, f, indent=2)

    return f"Se eliminó el reject_keyword {reject_keyword} del chat_id {chat_id}."

def agregar_priority_senders(chat_id, new_senders):
    with open('config.json', 'r+') as f:
        data = json.load(f)
        if chat_id in data:
            data[chat_id]['priority_senders'].extend(new_senders)
            f.seek(0)
            json.dump(data, f, indent=4)
            return True
        else:
            return False

def eliminar_priority_senders(chat_id, senders_a_eliminar):
    with open('config.json', 'r+') as f:
        data = json.load(f)
        if chat_id in data:
            data[chat_id]['priority_senders'] = [sender for sender in data[chat_id]['priority_senders'] if sender not in senders_a_eliminar]
            f.seek(0)
            json.dump(data, f, indent=4)
            return True
        else:
            return False

def add_reject_sender(chat_id, sender):
    try:
        with open('data.json', 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        data = {}

    if chat_id in data:
        if 'reject_senders' in data[chat_id]:
            if sender not in data[chat_id]['reject_senders']:
                data[chat_id]['reject_senders'].append(sender)
        else:
            data[chat_id]['reject_senders'] = [sender]
    else:
        return 'Chat ID not found'

    with open('data.json', 'w') as f:
        json.dump(data, f, indent=2)

def remove_reject_sender(chat_id, sender):
    try:
        with open('data.json', 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        data = {}

    if chat_id in data and 'reject_senders' in data[chat_id]:
        if sender in data[chat_id]['reject_senders']:
            data[chat_id]['reject_senders'].remove(sender)
        else:
            return 'Sender not found'
    else:
        return 'Chat ID or reject_senders not found'

    with open('data.json', 'w') as f:
        json.dump(data, f, indent=2)

