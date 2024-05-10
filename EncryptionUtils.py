from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.concatkdf import ConcatKDFHash
import os
import base64

class EncryptionUtils:
    KEY = b'1234567890123456'  # 16-byte key for AES

    @staticmethod
    def encrypt(plaintext):
        iv = os.urandom(16)  # 16-byte random IV
        cipher = Cipher(algorithms.AES(EncryptionUtils.KEY), modes.CBC(iv), backend=default_backend())
        encryptor = cipher.encryptor()
        padded_data = plaintext.ljust((len(plaintext) // 16 + 1) * 16)  # Padding for AES
        ciphertext = encryptor.update(padded_data.encode()) + encryptor.finalize()

        return iv + ciphertext  # Return IV + ciphertext

    @staticmethod
    def decrypt(ciphertext):
        iv = ciphertext[:16]  # Extract IV
        encrypted_data = ciphertext[16:]

        cipher = Cipher(algorithms.AES(EncryptionUtils.KEY), modes.CBC(iv), backend=default_backend())
        decryptor = cipher.decryptor()
        decrypted_data = decryptor.update(encrypted_data) + decryptor.finalize()

        return decrypted_data.strip().decode()  # Remove padding and decode

    @staticmethod
    def generate_iv():
        return os.urandom(16)  # Return 16-byte IV
