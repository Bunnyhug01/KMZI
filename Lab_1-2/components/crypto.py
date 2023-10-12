from cryptography.fernet import Fernet


def encrypt(text:str):
    key = Fernet.generate_key()
    f = Fernet(key)
    token = f.encrypt(bytes(text, encoding='utf-8'))
    return token