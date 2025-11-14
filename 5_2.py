# Código para Python 3
message = 'GIEWIVrGMTLIVrHIQS' # encrypted message
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for key in range(len(LETTERS)):
    translated = ''
    for symbol in message:
        if symbol in LETTERS:
            num = LETTERS.find(symbol)
            num = num - key
            
            if num < 0:
                num = num + len(LETTERS)
                
            translated = translated + LETTERS[num]
        else:
            translated = translated + symbol
            
    # Usando f-string para formatar a saída em Python 3
    print(f'Hacking key #{key}: {translated}')