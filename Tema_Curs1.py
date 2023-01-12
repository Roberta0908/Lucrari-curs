#Cerinta 1: O variabila este un loc din memorie ce depoziteaza diferite valori.

#Cerinta 2:

# String
Liceu = 'Liceul Teoretic Emil Racovita'
print(f'Acesta este {Liceu}')
# Int
Nota = 10
print(f'El a luat nota {Nota}')
# Float
Pret = 125.60
print(f'Fondul de ten costa {Pret} lei')
# Boolean
invat_mate = False
print(f'Azi am invatat la mate: {invat_mate}')

#Cerinta 3:
print(type(Liceu))
print(type(Nota))
print(type(Pret))
print(type(invat_mate))

#Cerinta 4:

print(round(Pret))
#verificare tip de date
print(type(round(Pret)))

#Cernta 5:

print(f'Am invatat la {Liceu}')
Nota = str(Nota)
print(f'Astazi am luat nota {Nota} la matematica')
Pret = str(Pret)
print(f'Mi-am cumparat o bratara la pretul de {Pret} lei')
invat_mate = str(invat_mate)
print(f'Este {invat_mate} ca nu am invat')

#Cerinta 6:

nume = input('Introdu numele:')
prenume = input('Introdu prenumele:')
nr_caractere = len(f'{nume}{prenume}')
print(f'Numele complet are {nr_caractere} caractere')

#Cerinta 7:
lungime = int(input("Lungime dreptunghi: "))
latime = int(input('Latime dreptungh: '))
aria = lungime * latime
print(f'Aria dreptunghiului este {aria}')

#Cerinta 8:

prop1 = 'Coral is either the stupidest animal or the smartest rock'
print(prop1.count(' the '))

#Cerinta 9:

prop2 =  'Coral is eiTHEr THE stupidest animal or THE smartest rock'
print(prop2.count('the'))

#cerinta 10:

assert prop1 == int




