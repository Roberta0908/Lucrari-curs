#1: Functie care sa calculeze si sa returneze suma a 2 numere
def suma(x,y):
    print(x+y)
suma(2,3)
suma(152,17)

#2: Functie care sa returneze TRUE daca un numar este par, FALSE pt impar
def nr_par(x):
    if x % 2 == 0:
        print('TRUE');
    else:
        print('FALSE')
nr_par(3)
nr_par(20)

'''3: Functie care returneaza numarul total de caractere din numele tau complet.
(nume, prenume, nume_mijlociu)'''

def nr_caractere():
    x = input('Introdu numele complet:')
    print(f'Numar caractere:{len(x)}')
nr_caractere()
nr_caractere()

#4:  Functie care returneaza aria dreptunghiului

def aria_dreptunghiului(x,y):
    print(x*y)
aria_dreptunghiului(2,3)
aria_dreptunghiului(18,20)

#5: Functie care returneaza aria cercului
def aria_cerc(r):
    print(3.14*r*r)
aria_cerc(2)
aria_cerc(8)

#8: Functie care primeste o LISTA de numere si returneaza o LISTA doar cu numerele pozitive
# Nu-mi dau seama cum sa afisez lista
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
def lista_nrPoz():
    lista_nrPoz = []
    for numar in numere:
        if numar > 0:
            lista_nrPoz.append(numar)
    return lista_nrPoz
print(lista_nrPoz())


'''Pentru toate exercitiile
Apelati functia de cel putin 2 ori cu valori diferite pentru a testa
Daca functia are return, printati raspunsul
1. Functie care sa calculeze si sa returneze suma a 2 numere
'''
# cazul in care putem introduce numerele de la tastatura, e mai dinamic
x = int(input('Introdu primul numar: '))
y = int(input('Introdu al doilea numar: '))


def suma_numere(x, y):
    suma = x + y
    return (f'Suma celor doau numere este: {suma}')


print(suma_numere(x, y))


# cazul in care punem argumentele cand apelam functia
def suma_numere(a, b):
    suma = a + b
    return (f'Suma celor doau numere este: {suma}')


print(suma_numere(8, 10))
print(suma_numere(78, 10))

'''2. Functie care sa returneze TRUE daca un numar este par, FALSE pt impar'''


def par_impar(numar):  # definim functia si ii punem parametrul numar
    if numar % 2 == 0:  # verificam prin modulo daca este par
        return True
    else:
        return False


print(par_impar(84))
print(par_impar(75))

'''3. Functie care returneaza numarul total de caractere din numele tau complet.
(nume, prenume, nume_mijlociu) 
'''


def total_caractere(nume, prenume1, prenume2):
    return len(nume + prenume1 + prenume2)


print(total_caractere('Popescu', 'George', 'Dan'))

'''4. Functie care returneaza aria dreptunghiului'''


def aria_dreptunghi(lungime, latime):
    aria = lungime * latime
    return aria


print(aria_dreptunghi(8, 5))
print(aria_dreptunghi(10, 45))

'''5. Functie care returneaza aria cercului'''


def aria_cercului(raza):
    aria = raza * raza * 3.14
    return aria


print(aria_cercului(6))
print(aria_cercului(10))

'''6. Functie care returneaza True daca un caracter x se gaseste intr-un string dat. Fasle daca nu'''


def cautare_caracter(string, x):
    if x in string:
        return True
    else:
        return False


print(cautare_caracter('abc', 'a'))
print(cautare_caracter('abc', 'd'))

'''7. Functie fara return, primeste un string si printeaza pe ecran:
Nr de caractere lower case este x
Nr de caractere upper case exte y '''


def lower_upper(string):
    char_upper = 0
    char_lower = 0
    for char in string:
        if char.isupper():
            char_upper = char_upper + 1
        elif char.islower():
            char_lower = char_lower + 1
    print(f'Numarul de caractere mari este: {char_upper}')
    print(f'Numarul de caractere mici este: {char_lower}')


lower_upper('abc1ABCD!')

'''9. Functie care nu returneaza nimic. Primeste 2 numere si PRINTEAZA
Primul numar x este mai mare decat al doilea nr y
Al doilea nr y este mai mare decat primul nr x
Numerele sunt egale. '''


def doua_numere(x, y):
    if x == y:
        print(f'Numerele sunt egale')
    elif x > y:
        print(f'Primul numar {x} este mai mare decat al doilea nr {y}')
    else:
        print(f'Al doilea nr {y} este mai mare decat primul nr {x}')


doua_numere(89, -5)
doua_numere(7, 46)

'''10. Functie care primeste un numar si un set de numere.
Printeaza ‘am adaugat numarul nou in set’ + returneaza True
Sau Printeaza ‘nu am adaugat numarul in set. Acesta exista deja’ + returneaza False'''

set_numere_input = {2, 5, 8, 78, -8, 45}
set_numere_input = {2, 5, 8, 78, -8, 45}


def adaugare_numar(set_numere, numar_nou):
    if numar_nou in set_numere:
        print(f'nu am adaugat numarul {numar_nou} in set, exista deja')
        return False
    else:
        set_numere.add(numar_nou)
        print(f'am adaugat numarul {numar_nou} in set')
        return True


print(adaugare_numar(set_numere_input, 78))
print(adaugare_numar(set_numere_input, 75))