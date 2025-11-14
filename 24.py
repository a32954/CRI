# Código para Python 3
import onetimepad

# 'pip install onetimepad' pode ser necessário
cipher = onetimepad.encrypt('One Time Cipher', 'random')

print("Cipher text is ")
print(cipher)
print("Plain text is ")

msg = onetimepad.decrypt(cipher, 'random')
print(msg)