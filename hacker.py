# Hackare
from main import euclideanExtended, decrypt
import math, sympy

def primeFactori(n):
    factors = []
    # Söka igenom en lista med primtal  
    for i in list(sympy.primerange(0, math.sqrt(n))): 
        # Kolla ifall n är delbart med primatalet 
        if n % i == 0:
            factors.append(int(i)) 
            factors.append(int(n / i)) 
    return factors

#Ta emot n, e och med
n = int(input("n: "))
e = int(input("e: "))

#Primtalsfaktorisera n till [p,q]
pq_arr = primeFactori(n)
print(pq_arr)

#Ta fram d med hjälp e och (p-1)*(q-1)
phin = (pq_arr[0] - 1) * (pq_arr[1] - 1)
d = euclideanExtended(e, phin)

encrypted = int(input("encrypted message: "))
#Avkryptera x=med^d (mod n)
secret = decrypt(d, n, encrypted)

print("Secret message: " + str(secret))