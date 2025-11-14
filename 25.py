# Código para Python 3
# 'pip install pyDes' pode ser necessário
import pyDes

# Em Python 3, dados, chave e IV devem ser 'bytes'
data = b"DES Algorithm Implementation"
key = b"DESCRYPT" # Chave de 8 bytes
iv = b"\0\0\0\0\0\0\0\0" # IV de 8 bytes

k = pyDes.des(key, pyDes.CBC, iv, pad=None, padmode=pyDes.PAD_PKCS5)

d = k.encrypt(data)
# {d!r} é o equivalente em f-string do antigo '%r'
print(f"Encrypted: {d!r}")

decrypted_data = k.decrypt(d)
print(f"Decrypted: {decrypted_data!r}")

assert decrypted_data == data
print("Assert OK!")