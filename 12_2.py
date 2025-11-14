# Código para Python 3
import base64

decoded_data = base64.b64decode("RW5jb2RlIHRoaXMgdGV4dA==")

print("decoded text is ")
# O resultado 'decoded_data' é bytes,
# então usamos .decode() para imprimir como string
print(decoded_data.decode('utf-8'))