# Código para Python 3
def p_and_q(n):
    data = []
    for i in range(2, n): # Começa do 2
        if n % i == 0:
            data.append(i)
    # Se 'n' for um produto de dois primos, isso retornará (p, q)
    return tuple(data) 

def euler(p, q):
    return (p - 1) * (q - 1)

def private_index(e, euler_v):
    for i in range(2, euler_v):
        if (i * e) % euler_v == 1:
            return i
            
def decipher(d, n, c):
    # pow(c, d, n) é mais eficiente que (c ** d % n)
    return pow(c, d, n)

def main():
    # Em Py3, input() retorna string, então int(input()) é o correto
    e = int(input("input e: "))
    n = int(input("input n: "))
    c = int(input("input c: "))
    
    p_and_q_v = p_and_q(n)
    # print(f"[p_and_q]: {p_and_q_v}")
    
    euler_v = euler(p_and_q_v[0], p_and_q_v[1])
    # print(f"[euler]: {euler_v}")
    
    d = private_index(e, euler_v)
    # print(f"[d]: {d}")
    
    plain = decipher(d, n, c)
    print(f"plain: {plain}")

if __name__ == "__main__":
    main()