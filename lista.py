import json

def save_json(filename, data):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)
def parse_json(filename):
    with open(filename, 'r') as f:
        data = json.load(f)

    users = []
    for user_data in data:
        user = {
            "email": user_data["email"],
            "password": user_data["password"],
            "keywords": user_data["keywords"],
            "priority_senders": user_data["priority_senders"],
            "reject_keywords": user_data["reject_keywords"],
            "reject_senders": user_data["reject_senders"],
            "favorite_contact": user_data["favorite_contact"]
        }
        users.append(user)

    return users

# Llamamos a la función parse_json y guardamos los resultados en una variable
users = parse_json('users.json')

for user in users:
    email = user['email']
    password = user['password']
    keywords = user['keywords']
    priority_senders = user['priority_senders']
    reject_keywords = user['reject_keywords']
    reject_senders = user['reject_senders']
    favorite_contact = user['favorite_contact']

    # Aquí puedes hacer lo que quieras con las variables,
    # por ejemplo, imprimirlas en pantalla:
    print(f"Email: {email}")
    print(f"Password: {password}")
    print(f"Keywords: {keywords}")
    print(f"Priority senders: {priority_senders}")
    print(f"Reject keywords: {reject_keywords}")
    print(f"Reject senders: {reject_senders}")
    print(f"Favorite contact: {favorite_contact}")
