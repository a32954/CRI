# Código para Python 3

# 'string.maketrans' mudou para 'str.maketrans'
source = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
dest = 'NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm'
rot13trans = str.maketrans(source, dest)

# Função para traduzir texto
def rot13(text):
    return text.translate(rot13trans)

def main():
    txt = "ROT13 Algorithm"
    print(rot13(txt))

if __name__ == "__main__":
    main()