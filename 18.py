# Código para Python 3
import random, string, sys
# Assumindo que o código da página anterior foi salvo como 'substitution.py'
import substitution 

def main():
    for i in range(1000):
        key = substitution.getRandomKey()
        message = random_string()
        print(f'Test {i + 1}: String: "{message[:50]}..."')
        print(f"Key: {key}")
        
        encrypted = substitution.translateMessage(message, key, 'E')
        decrypted = substitution.translateMessage(encrypted, key, 'D')
        
        if decrypted != message:
            print(f'ERROR: Decrypted: "{decrypted}" Key: {key}')
            sys.exit()
            
    print('Substitution test passed!')

def random_string(size = 5000, chars = string.ascii_letters + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

if __name__ == '__main__':
    main()