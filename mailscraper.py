from __future__ import print_function

import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from base64 import urlsafe_b64decode

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']
string_mail = ""
creds = None
# The file token.json stores the user's access and refresh tokens, and is
# created automatically when the authorization flow completes for the first
# time.
if os.path.exists('token.json'):
    creds = Credentials.from_authorized_user_file('token.json', SCOPES)
# If there are no (valid) credentials available, let the user log in.
if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    else:
        flow = InstalledAppFlow.from_client_secrets_file(
            'credentials.json', SCOPES)
        creds = flow.run_local_server(port=0)
    # Save the credentials for the next run
    with open('token.json', 'w') as token:
        token.write(creds.to_json())

try:
    # Call the Gmail API
    service = build('gmail', 'v1', credentials=creds)
    # get the content of the latest 10 emails in the inbox. If there are any attached files, print a message saying so. Try and except for that.
    # Print the emails with the following format: "From: <sender> Subject: <subject> Body: <body>" with 3 newlines between emails.
    # If there are no emails, print a message saying so.
    # If there is an error, print the error.
    userid = "germantarnoski16@gmail.com"
    results = service.users().messages().list(userId=userid, labelIds=['INBOX'], maxResults=10).execute()
    messages = results.get('messages', [])
    if not messages:
        print('No messages found.')
    else:
        for message in messages:
            msg = service.users().messages().get(userId=userid, id=message['id']).execute()


            payload = msg['payload']
            #save in a variable the name of the sender and the subject of the email


            headers = msg['payload']['headers']
            for header in headers:
                if header['name'] == 'From':
                    sender = header['value']
                if header['name'] == 'Subject':
                    subject = header['value']

            #create a list of senders to ignore. Incluide Google and linkedin.
            #setear una variable ignore que se setee con el valor que hay en la sexta posicion para cada renglon en el archivo messi.txt
            # cada renglon es de este estilo ["bbaumgart@itba.edu.ar", "messichiquito1812",["Futbol","Messi chiquito","Traba feo","Reunion HCI","HCI"],["germantarnoski16@gmail.com","nsuarezdurrels@itba.edu.ar"],["Oferta laboral,"Trabajo","Hola soy german"],["mperotti@itba.edu.ar"]["fbotti@itba.edu.ar"]]
            
            ignore = []
            with open("messi.txt", "r") as f:
                for line in f:
                    ignore.append(line[5])

            #if sender contains any of the words in the ignore list, continue to the next email.
            if any(word in sender for word in ignore):
                continue



            print("Remitente: ", sender)
            print("Asunto: ", subject)


            if 'parts' in payload:
                for part in payload['parts']:
                    if part['mimeType'] == 'text/plain':
                        body = urlsafe_b64decode(part['body']['data']).decode('utf-8')
                        break
            else:
                body = urlsafe_b64decode(payload['body']['data']).decode('utf-8')

            string_mail += "\n\n\n" + "Remitente: " + sender + "\nAsunto: " + subject + "\n" + body

            try:
                if msg['payload']['parts']:
                    print('This email has an attachment.')
                    print('\n\n\n')
            except:
                print('\n\n\n')

        #build a string object with concatenated Remitente, asunto, and body

except HttpError as error:
    # TODO(developer) - Handle errors from gmail API.
    print(f'An error occurred: {error}')