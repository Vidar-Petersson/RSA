## Fil med hjälpfunktioner till de andra programmen

import math

#Hittar största gemensamma nämnare (euklides algoritm)
def gcd(a, b):
    while a != 0:
        a, b = b % a, a
    return b

#Ta fram d, e*dΞ1 (mod(p-1)*(q-1)), med euklides utökade algoritm
def euclideanExtended(e, phin):
    u1, u2, u3 = 1, 0, e
    v1, v2, v3 = 0, 1, phin
    while v3 != 0:
        q = u3 // v3
        v1, v2, v3, u1, u2, u3 = (u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3
    return u1 % phin

#Avkryptera users meddelande, x^d (mod n)
def decrypt(d, n, encrypted):
    return (encrypted ** d) % n