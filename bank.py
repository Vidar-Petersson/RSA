# Bank
from main import gcd, euclideanExtended

#Avkryptera users meddelande, x^d (mod n)
def decrypt(d, n, encrypted):
    return pow(encrypted, d, n)

#Slumpa två primtal, p och q, Största möjliga n som Wolfram Alpha klarar
p, q = 7287373636218011609807966031486137775465374700085554587441841697660499126775855135181538705777, 5906016738011854925174024949492411475239976917928128514491383521447161079749394816078272144233
n = p*q

#Ta fram e som är relativt primt till (p-1)*(q-1) {Inte har gemensamma faktorer}
phin = (p-1)*(q-1)
for i in range(2, phin - 1):
    if (gcd(i, phin) == 1):
        e = i
        break

#Skicka n och e till user
print("n: " + str(n))
print("e: " + str(e))

#Ta fram d, e*dΞ1 (mod(p-1)*(q-1))
d = euclideanExtended(e, phin)

print("d: " + str(d))
print("phin: " + str(phin))

encrypted = int(input("Received message from user: "))
decrypted = decrypt(d, n, encrypted)
print("Decrypted: " + str(decrypted))