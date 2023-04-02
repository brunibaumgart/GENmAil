import openai
from mailscraper import string_mail

openai.api_key = "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"

nombre = "German"

#refactor the following 3 strings into a single string with 3 newlines between them
text1 = "Vos sos mi asistente de emails. Mi nombre es "
text2 = " Recién recibí este mail de parte de "
text3 = " Necesito que me digas de qué se trata, a modo de resumen. Decime solo " \
        "la información nueva que necesito saber. El resumen tiene que ser más corto que el original. " \
"Indicar claramente cual es el asunto del mail y cual el resumen. Si hay fechas, indicarlas. " \


input = string_mail

#put all emails on a list. Each email starts with "Remitente:"
emails = string_mail.split("Remitente: ")[1:]

escribir_archivo = ""

#iterate over the list of emails and create a prompt for each one
for email in emails:
    #get the sender and the subject of the email
    sender = email.split("\nAsunto: ")[0]
    subject = email.split("\nAsunto: ")[1].split("\n")[0]
    #get the body of the email
    body = email.split("\nAsunto: ")[1]
    #create the prompt
    prompt = text1 + nombre + text2 + sender + text3 + "\nEmail: \n"+ body
    completion = openai.Completion.create(engine="text-davinci-003", prompt=prompt, max_tokens=2048)
    escribir_archivo += "\n" + completion.choices[0].text + "\n"

with open("output.txt", "w") as f:
     f.write(escribir_archivo)
spam = ["Messi chiquito", "Futbol", "Traba feo", "Reunion HCI", "HCI", "Oferta laboral", "Trabajo", "Hola soy german"]
#iterar por cada palabra dentrro de output.txt y checkear si esta en la lista spam, si es asi, cambiar la posicion del mail una posicion hacia arriba y anotarlo como checkeado
#si no esta en la lista spam, anotarlo como checkeado y seguir con el siguiente mail



for word in escribir_archivo:
    if word in spam:
        #mover el mail una posicion hacia arriba
        #anotar como checkeado
        continue
    else:
        #anotar como checkeado
        continue