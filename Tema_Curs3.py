#1: Declara o lista note_muzicale in care sa pui do re mi etc pana la do
#a. Afiseaz-o

note_muzicale= ['do','re','mi','fa','sol','la','si','do']
print(note_muzicale)

#b. Inversează ordinea folosind slicing si suprascrie aceasta lista, apoi printeaza varianta actuala (inversata)
note_muzicale_inversate = note_muzicale[::-1]
print(note_muzicale_inversate)

#c. Pe aceasta lista, aplica o metoda care banuiesti ca face același lucru, adica sa ii inverseze ordinea (Nu trebuie sa o suprascrii în acest caz, deoarece metoda face asta automat) si apoi printeaza varianta actuala a listei. Practic ai ajuns înapoi la varianta inițială
note_muzicale_inversate.reverse()
print(note_muzicale_inversate)

#2: Afiseaza pe ecran de cate ori apare nota ‘do’ in lista.
print(note_muzicale.count('do'))

#3: Avand 2 liste, [3, 1, 0, 2] si [6, 5, 4], gaseste 2 variante sa le unesti intr-o singura lista.
lista1 = [3, 1, 0, 2]
lista2 = [6, 5, 4]
lista1.extend(lista2)
print(lista1)
lista2.append(lista1)
print(lista2)

#4: Sorteaza si afiseaza lista generata la exercitiul anterior. Sterge numarul 0 din lista folosind o functie si apoi afiseaza din nou lista
lista1 = [3, 1, 0, 2, 6, 5, 4]
lista1.sort()
print(lista1)
lista1.remove(0)
print(lista1)

'''5: Folosind un if, verifica lista generata la exercitiul 3 si afiseaza pe fiecare ramura urmatoarele:
Lista este goala (IF)
Lista nu este goala (ELSE)
 '''
if len(lista1) >= 1:
    print('Lista nu este goala');
else:
    print('Lista este goala');

#6: Foloseste o functie care sa goleasca lista de la exercitiul 3
lista1_goala = [3, 1, 0, 2, 6, 5, 4]
lista1.clear()
print(lista1)

#7: Rescrie if-ul de la exercitiul 5 si verifica inca o data rezultatul. Acum ar trebui sa se afiseze ca lista e goala
if len(lista1) >= 1:
    print('Lista nu este goala');
else:
    print('Lista este goala');

#8: Avand dictionarul dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}, foloseste o functie ca sa afisezi Elevii (cheile)
dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
print(dict1.keys())

'''9: Printeaza cei 3 elevi din dictionarul de mai sus si respectiv notele lor
Ex: ‘Ana a luat nota {x}’. 
Doar nota o vei lua folosindu-te de cheie
'''
print(f'Ana a luat nota ', dict1['Ana'])
print(f'Gigel a luat nota ',dict1['Gigel'])
print(f'Dorel a luat nota ',dict1['Dorel'])

'''10: Imagineaza-ti ca Dorel a facut contestatie si a primit nota 6.
Modifica nota lui Dorel in 6
Printeaza nota lui dupa modificare
'''
dict1['Dorel'] = 6
print(dict1['Dorel'])

'''11: Imagineaza-ti ca Gigel se transfera din clasa.
Cauta o functie care sa il stearga
Vine un coleg nou. 
Adaugati-l in lista pe Ionica, cu nota 9
Printati dictionarul cu noii elevi
'''
dict1.pop('Gigel')
print(dict1)
dict1['Ionel'] = 9
print(dict1)

'''12: Ai urmatoarele seturi: 
zile_sapt = {'luni', 'marti', 'miercuri', 'joi', 'vineri', 'sambata', 'duminica'}
weekend = {'sambata', 'duminica'}
Incearca sa adaugi in setul zilele_sapt ziua de ‘luni’ si observa ce se intampla. 
Afiseaza setul zile_sapt si constata rezultatul adaugarii anterioare.
'''
zile_sapt = {'luni', 'marti', 'miercuri', 'joi', 'vineri', 'sambata', 'duminica'}
weekend = {'sambata', 'duminica'}
zile_sapt.add('luni')
print(zile_sapt)

'''13: Foloseste un if si verifica daca:
Weekend este un subset al zilelor din sapt (adica daca elementele din setul weekend se regasesc intre elementele din setul zile_sapt)
Weekend nu este un subset al zilelor din sapt
Hint: Va puteti folosi fie de operatorul de comparatie fie de o functie. Rezultatul fiecarui punct de mai sus va fi un boolean
'''
if weekend.issubset(zile_sapt):
    print('Weekend este un subset al zilelor din sapt');
else:
    print('Weekend nu este un subset al zilelor din sapt');

#14: Afiseaza diferentele dintre aceste 2 seturi (adica elementele care sunt in zile_sapt si nu sunt in weekend si invers)
zile_sapt.difference_update(weekend)
print(zile_sapt)
zile_sapt = {'luni', 'marti', 'miercuri', 'joi', 'vineri', 'sambata', 'duminica'}
weekend.difference_update(zile_sapt)
print(weekend)

#15: Afiseaza intersectia elementelor din aceste 2 seturi (adica elementele care exista in ambele seturi). Hint: Va puteti folosi de o functie
intersectia = zile_sapt.intersection(weekend)
print(intersectia)
intersectia = zile_sapt.intersection(weekend)
print(f"Intersectia dintre cele doua seturi este: {intersectia}")






