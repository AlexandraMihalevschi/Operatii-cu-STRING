c = str(input("Dati numele si prenumele: "))
lc=0
lm=0

for i in c:
    if (ord(i)>=65) and (ord(i)<=90):
        lm+=1
    elif (ord(i)>=97) and (ord(i)<=122):
        lc+=1

nume, prenume = c.split()

if (nume.title()==nume)and(prenume.title()==prenume)and(lm+lc==len(nume)+len(prenume)):
    print(f"Totul este scris corect. Salut {nume} {prenume}!")
else: print("Introduceti din nou datele cerute")