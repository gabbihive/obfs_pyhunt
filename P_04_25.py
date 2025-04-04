import base64 as x
import random as y

if __name__ == "__main__":
    a = y.randint(1000, 4999)
    s = [0, 1] # Fibonacci sequence initialization
    for i in range(2, a): 
        s.append(s[-1] + s[-2]) 
    b = s[:a] 
    c = [b[i] % 10 for i in range(len(b))]  
    e = ''.join(map(str, c)) 
    f = ''.join(y.choices(''.join([chr(i) for i in range(97, 123)]), k=len(e))) 
    g = ''.join(e[i] + f[i] for i in range(len(e))) 
    print(x.b64encode(g.encode()).decode()) 