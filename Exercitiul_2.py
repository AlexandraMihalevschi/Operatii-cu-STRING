c = str(input("Introduceti un sir: "))
alfabet=0
cifre=0
numere=0
litere=0
for i in (len (c)):
    if (ord(c[i])>=48) and (ord(c[i])<=57): 
       cifre+=1 
    elif ((ord(c[i])>=65) and (ord(c[i])<=90):
        alfabet+=1
    elif (ord(c[i])>=97) and (ord(c[i])<=122):
        litere+=1
    else:
        special+=1
        
print ("Numărul total de majuscule din acest șir:", alfabet)
print ("Numărul total de cifre din acest șir:", cifre)
print ("Numărul total de caractere speciale din acest șir:", special)