# Código para Python 3
import base64

# A string precisa ser 'bytes' (b"...")
encoded_data = base64.b64encode(b"Encode this text")

print("Encoded text with base 64 is")
# O resultado 'encoded_data' também é bytes,
# então usamos .decode() para imprimir como string
print(encoded_data.decode('utf-8'))

