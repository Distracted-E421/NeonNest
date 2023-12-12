from cryptography.fernet import Fernet

def generate_key():
    """Generates a key for encryption and decryption using Fernet."""
    return Fernet.generate_key()

def encrypt_data(key, data):
    """Encrypts data using the provided key.
    
    Args:
        key: A bytes-like object representing the encryption key.
        data: A string to be encrypted.

    Returns:
        A bytes-like object representing the encrypted data.
    """
    cipher_suite = Fernet(key)
    encrypted_data = cipher_suite.encrypt(data.encode())
    return encrypted_data

def decrypt_data(key, encrypted_data):
    """Decrypts data using the provided key.
    
    Args:
        key: A bytes-like object representing the decryption key.
        encrypted_data: A bytes-like object representing the encrypted data.

    Returns:
        A string representing the decrypted data.
    """
    cipher_suite = Fernet(key)
    decrypted_data = cipher_suite.decrypt(encrypted_data).decode()
    return decrypted_data
