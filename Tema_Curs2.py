# 1:Explica cu cuvintele tale in cadrul unui comentariu cum functioneaza un if else
# Structura if else este o propozitie de tip "cauza-efect", if punand cauza, iar else efectele.

# 2:Verifica si afiseaza daca x este numar natural sau nu (un numar se considera natural daca este numar intreg mai mare ca 0)
x = 5
if x > 0:
    print(f'Numar natural')
else:
    print(f'Alt tip de numar')

# 3:Verifica si afiseaza daca x este numar pozitiv, negativ sau neutru

if x > 0:
    print(f'Numar pozitiv')
elif x == 0:
    print(f'Numar neutru')
elif x < 0:
    print(f'Numar negativ')

# 4:Verifica si afiseaza daca x este intre -2 si 13 (incluzand captele de interval).

if -2 <= x <= 13:
    print(f'Numarul se afla in intergval')
else:
    print(f'Numarul nu se afla in nterval')

# 5:Verifica si afiseaza daca diferenta dintre x si y este mai mica de 5 (diferenta inseamna cate numere sunt intre x si y,
# nu rezultatul diferentei intre x si y). Hint: Se va folosi functia abs

x = 5
y = 8
dif = abs(x-y)
print(dif)
if  dif< 5:
    print(f'Adevarat')
else:
    print(f'Fals')

# 6:Verifica daca x NU este intre 5 si 27, incluzand capetele de interval. (a se folosi ‘not’)

x = 5
print(x)
if 5 <= x <=27:
    print(f'{not(x)}, nu este in interval')
else:
    print('x este in interval')

# 7:Declara o noua variabila y de tip int si apoi verifica si afiseaza daca x si y sunt egale, daca nu, afiseaza care din ele este mai mare
x = 5
y = 8
if x == y:
    print('Sunt egale')
elif x > y:
    print('x este mai mare')
else:
    print('y este mai mare')

# 8:Presupunand ca x, y, z (toate de tip int) - reprezinta laturile unui triunghi, afiseaza daca triunghiul este isoscel (doua laturi sunt egale), echilateral (toate laturile sunt egale) sau oarecare (nicio latura nu e egala).

x = int(input('1_latura:'))
y = int(input('2_latura:'))
z = int(input('3_latura:'))
if x == y == z :
    print('triunghi echilateral')
elif x == y or x == z or y == z:
    print('triunghi isoscel')
else:
    print('triunghi oarecare')

# 9:Citeste o litera de la tastatura apoi verifica si afiseaza daca este vocala sau nu. Atentie! Trebuie sa evaluati si cazurile uppercase si cazurile lowercase.

vocala = input('Introdu o litera:')
if vocala.upper() == 'A' or  vocala.upper() == 'E' or  vocala.upper() == 'I' or  vocala.upper() == 'O' or  vocala.upper() == 'U':
    print('Este vocala')
else:
    print('Nu este vocala')

# 10:Transforma si printeaza notele din sistem românesc in sistem american dupa cum urmeaza:

nota = int(input('Introdu nota:'))
if nota > 9:
    print('Nota A')
elif nota > 8:
    print('Nota B')
elif nota > 7:
    print('Nota C')
elif nota > 6:
    print('Nota D')
elif nota > 4:
    print('Nota E')
elif nota <= 4:
    print('Nota F')