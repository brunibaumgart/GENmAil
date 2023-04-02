class Person:
    def __init__(self, chat_id, mail, password, keywords=[], priority_senders=[], reject_keywords=[], reject_senders=[], favorite_contact=[]):
        self._chat_id = chat_id
        self._mail = mail
        self._password = password
        self._keywords = keywords
        self._priority_senders = priority_senders
        self._reject_keywords = reject_keywords
        self._reject_senders = reject_senders
        self._favorite_contact = favorite_contact

    def get_chat_id(self):
        return self._chat_id
    def get_mail(self):
        return self._mail
    def get_password(self):
        return self._password
    def get_keywords(self):
        return self._keywords
    def get_priority_senders(self):
        return self._priority_senders
    def get_reject_keywords(self):
        return self._reject_keywords
    def get_reject_senders(self):
        return self._reject_senders
    def get_favorite_contact(self):
        return self._favorite_contact