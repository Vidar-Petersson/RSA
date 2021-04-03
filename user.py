#User

#Ta emot n och e
n = int(input("n: "))
e = int(input("e: "))

#Bestäm sitt meddelande (med>n)
#secret = int(input("Hemligt meddelande: "))
secret = 666

#Kryptera med: y=med^e (mod n)
encrypted = pow(secret, e, n)

#Skicka till banken
print("encrypted: " + str(encrypted))