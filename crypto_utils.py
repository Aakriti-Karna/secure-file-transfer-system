from cryptography.fernet import Fernet

KEY_FILE = "secret.key"

def load_key():
    try:
        with open(KEY_FILE, "rb") as f:
            return f.read()
    except FileNotFoundError:
        key = Fernet.generate_key()
        with open(KEY_FILE, "wb") as f:
            f.write(key)
        return key

def encrypt_data(data: bytes) -> bytes:
    key = load_key()
    fernet = Fernet(key)
    return fernet.encrypt(data)

def decrypt_data(data: bytes) -> bytes:
    key = load_key()
    fernet = Fernet(key)
    return fernet.decrypt(data)
