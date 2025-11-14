# Código para Python 3
# Observação: 'pip install pycryptodome' é necessário

from Crypto import Random
from Crypto.PublicKey import RSA
import base64

def generate_keys():
    modulus_length = 256*4 # 1024 bits
    privatekey = RSA.generate(modulus_length, Random.new().read)
    publickey = privatekey.publickey()
    return privatekey, publickey

def encrypt_message(a_message, publickey):
    # A implementação no PDF é insegura e obsoleta.
    # Mas, para seguir o tutorial, faria a criptografia "crua":
    encrypted_msg = publickey.encrypt(a_message, 32)[0]
    encoded_encrypted_msg = base64.b64encode(encrypted_msg)
    return encoded_encrypted_msg

def decrypt_message(encoded_encrypted_msg, privatekey):
    decoded_encrypted_msg = base64.b64decode(encoded_encrypted_msg)
    decoded_decrypted_msg = privatekey.decrypt(decoded_encrypted_msg)
    return decoded_decrypted_msg

# A mensagem deve ser 'bytes'
a_message = b"This is the illustration of RSA algorithm of asymmetric cryptography"

privatekey , publickey = generate_keys()
encrypted_msg = encrypt_message(a_message , publickey)
decrypted_msg = decrypt_message(encrypted_msg, privatekey)

# .exportKey() retorna bytes, então decodificamos para imprimir
print(f"{privatekey.exportKey().decode('utf-8')} - ({len(privatekey.exportKey())})")
print(f"{publickey.exportKey().decode('utf-8')} - ({len(publickey.exportKey())})")

# Mensagens também são bytes, decodifique-as
print(f" Original content: {a_message.decode('utf-8')} - ({len(a_message)})")
print(f"Encrypted message: {encrypted_msg.decode('utf-8')} - ({len(encrypted_msg)})")
print(f"Decrypted message: {decrypted_msg.decode('utf-8')} - ({len(decrypted_msg)})")