c = str(input("Introduceti CPN-ul: "))
d = 0
for i in c:
    if (ord(i)>=48) and (ord(i)<=57): 
        d+=1   
    
if (d==len(c)) and (d==13):
    print("Codul este introdus corect")
else: print("Introduceti un nou cod, format numai din cifre")