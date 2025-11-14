# Código para Python 3 (com correções de bugs do PDF)
import math, pyperclip

def main():
    myMessage= 'Toners raiCntisippoh' # O texto cifrado do exemplo
    myKey = 6
    
    plaintext = decryptMessage(myKey, myMessage)
    
    print("The plain text is")
    # O original trapaceava (printava a resposta). Este chama a função:
    print(plaintext) 

def decryptMessage(key, message):
    # Calcular o número de colunas na grade
    numOfColumns = math.ceil(len(message) / key)
    numOfRows = key
    
    # Calcular o número de "caixas sombreadas" (células vazias)
    numOfShadedBoxes = (int(numOfColumns) * numOfRows) - len(message)
    
    # Erro no PDF original: 'float('')' foi corrigido para ['']
    plaintext = [''] * int(numOfColumns)
    
    col = 0
    row = 0
    
    for symbol in message:
        plaintext[col] += symbol
        col += 1 # Próxima coluna
        
        # Se for a última coluna OU estiver em uma caixa sombreada,
        # volte para a coluna 0 e vá para a próxima linha.
        if (col == numOfColumns) or (col == numOfColumns - 1 and row >= numOfRows - numOfShadedBoxes):
            col = 0
            row += 1
            
    return ''.join(plaintext)

if __name__ == '__main__':
    main()