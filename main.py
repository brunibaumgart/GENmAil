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
emails = input.split("Remitente:")[1:]

#iterate over the list of emails and create a prompt for each one
for email in emails:
    partes_mail = email.split("\n")
    remitente = partes_mail[0]
    prompt = text1 + nombre + "." + text2 + remitente + text3
    i = 0
    for parte in partes_mail:
        if i == 0:
            continue
        else:
            prompt += parte
        i += 1

    # completion = openai.Completion.create(engine="text-davinci-003", prompt=prompt, max_tokens=2048)

    print(prompt)

    #
    with open("output.txt", "a") as f:
        # f.write(completion.choices[0].text)
        f.write(prompt)
