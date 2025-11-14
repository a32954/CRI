def encrypt(text, s):
    result = ""
    
    # Itera por cada caractere no texto
    for i in range(len(text)):
        char = text[i]
        
        # Criptografa caracteres maiúsculos
        if (char.isupper()):
            result += chr((ord(char) + s - 65) % 26 + 65)
        # Criptografa caracteres minúsculos
        elif (char.islower()):
            result += chr((ord(char) + s - 97) % 26 + 97)
        # Se não for letra (ex: espaço, pontuação), mantém como está
        else:
            result += char
            
    return result

# Bloco de teste
text = "CEASER CIPHER DEMO"
s = 4

print("Plain Text : " + text)
print("Shift pattern : " + str(s))
print("Cipher: " + encrypt(text, s))
    