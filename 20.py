# Código para Python 3
from cryptography.fernet import Fernet

key = Fernet.generate_key()
cipher_suite = Fernet(key)

# A mensagem deve ser 'bytes' (b"...")
cipher_text = cipher_suite.encrypt(b"This example is used to demonstrate cryptography module")
print(f"Cipher text: {cipher_text}")

# A descriptografia também retorna 'bytes'
plain_text_bytes = cipher_suite.decrypt(cipher_text)

# Decodifique para string para imprimir
plain_text = plain_text_bytes.decode('utf-8')
print(f"Plain text: {plain_text}")