from cryptography.fernet import Fernet

def gen_key():
    key= Fernet.generate_key() 
    with open("pass.key", "wb") as key_file:key_file.write(key)

def get_key():
    return open("pass.key", "rb").read()

