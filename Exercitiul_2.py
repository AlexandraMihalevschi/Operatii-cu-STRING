c = str(input("Introduceti un sir: "))
lm = 0
lc = 0
n = 0
s = 0

for i in range(0, len(c)+1):
    if (ord(c[i])>=48) and (ord(c[i])<=57):
        n+=1
    elif (ord(c[i])>=65) and (ord(c[i])<=90):
        lm+=1
    elif (ord(c[i])>=97) and (ord(c[i])<=122):
        lc+=1
    else: s+=1

print("Litere majuscule in sir sunt", lm, "de caractere")
print("Cifre in sir sunt", n, "de caractere")
print("Semne speciale in sir sunt", s, "de caractere")