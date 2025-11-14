# Código para Python 3
from itertools import cycle
import base64

def xor_crypt_string(data, key='awesomepassword', encode=False, decode=False):
    
    key_bytes = key.encode('utf-8') # Chave como bytes
    
    if decode:
        # 1. Decodifica de Base64 para bytes
        data_bytes = base64.b64decode(data)
        # 2. Faz o XOR byte a byte
        xored_bytes = bytes([b ^ k for b, k in zip(data_bytes, cycle(key_bytes))])
        # 3. Decodifica o resultado do XOR de bytes para string
        return xored_bytes.decode('utf-8')
        
    else: # Modo de codificação
        # 1. Codifica a string de entrada para bytes
        data_bytes = data.encode('utf-8')
        # 2. Faz o XOR byte a byte
        xored_bytes = bytes([b ^ k for b, k in zip(data_bytes, cycle(key_bytes))])
        
    if encode:
        # 3. Codifica o resultado do XOR para Base64 e retorna como string
        return base64.b64encode(xored_bytes).decode('utf-8').strip()
    
    # Se 'encode' for False (uso interno), retorna bytes brutos
    return xored_bytes

# Bloco de teste
secret_data = "XOR procedure"

print("The cipher text is")
encoded_data = xor_crypt_string(secret_data, encode=True)
print(encoded_data)

print("The plain text fetched")
decoded_data = xor_crypt_string(encoded_data, decode=True)
print(decoded_data)