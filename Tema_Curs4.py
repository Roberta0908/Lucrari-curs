# #1 b:Faceti acelasi lucru cu un for each
# masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
# for masina in masini:
#     print(f'Masina mea preferata este {masina}')
#
# '''2 a:Folositi un for ca sa iterati prin toata lista si sa afisati
# ‘Masina mea preferata este x’'''
#
# for i in range(len(masini)):
#     print(f'Masina mea preferata este {masini[i]}' );
#
# #1 c:Faceti acelasi lucru cu un while
# i=0
# while i < len(masini):
#     print(f'Masina mea preferata este {masini[i]}' );
#     i = i+1
#
# '''2:Aceeasi lista
# Folositi un for
# In for
#    Modificati elementele din lista astfel incat sa fie scrie cu majuscule, exceptand primul si ultimul
# Printati varianta finala a listei'''
#
# masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
# for i in range(1,len(masini)-1):
#     masini[i] = masini[i].upper()
# print(masini)
#
# masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
# for i in range(0, len(masini)):
#     if i == 0 or i == len(masini)-1:
#         continue
#     masini[i] = masini[i].upper()
# print(masini)
#
# '''3:Aceeasi lista,
# Vine un cumparator care doreste sa cumpere un Mercedes
# Iterati prin ea prin for each
# Daca masina e mercedes (if)
#    Printam ‘am gasit masina dorita de dvs’
#    Iesim din ciclu folosind un cuvant cheie care face acest lucru
#    Printam Am gasit masina X. Mai cautam	'''
#
# masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
# for masina in masini:
#     if masina == 'Mercedes':
#         print('Am gasit masina dorita');
#         break
#     else:
#         print(f'Am gasit masina {masina}. Mai cautam');
#
# '''4:Aceasi lista
# Vine un cumparator bogat dar indecis. Ii vom prezenta toate masinile cu exceptia Trabant si Lastun.
# Daca masina e Trabant sau Lastun
#    Folositi un cuvant cheie care sa dea skip la ce urmeaza
# Printati S-ar putea sa va placa masina x'''
#
# masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
# for masina in masini:
#     if masina == 'Trabant' or masina == 'Lastun':
#         continue
#     print(f'S-ar putea sa va placa masina {masina}');
#
# '''5: Modernizati parcul de masini
# Creati o lista goala, masini_vechi
# Iterati prin masini
# Cand gasiti Lastun sau Trabant:
# Salvati aceste masini in masini_vechi
# Suprascrieti-le cu ‘Tesla’ (in lista initiala de masini)
# Printati Modele vechi: x
# Modele noi: x'''
#
# masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
# masini_vechi = []
# for masina in masini:
#     if masina == 'Trabant' or masina == 'Lastun':
#         masini_vechi.append(masina)
#         index = masini.index(masina)
#         masini[index] = 'Tesla'
# print(f'Modele vechi: {masini_vechi}')
# print(f'Modele noi: {masini}')
#
# '''6: Avand dict
# pret_masini = {
#     'Dacia': 6800,
#     'Lastun': 500,
#     'Opel': 1100,
#     'Audi': 19000,
#     'BMW': 23000
# }
#
# Vine un client cu un buget de 15000 euro
# Prezentati doar masinile care se incadreaza in acest buget
# Iterati prin dict.items() si accesati masina si pretul
# Printati Pentru un buget de sub 15000 euro puteti alege masina x
# Iterati prin lista'''
#
# pret_masini = {
#     'Dacia': 6800,
#     'Lastun': 500,
#     'Opel': 1100,
#     'Audi': 19000,
#     'BMW': 23000}
# buget = 15000
# for masina, pret in pret_masini.items():
#     if pret <= buget:
#         print(f'Pentru un buget de sub 15000 euro puteti alege masina {masina} ')

'''7: Avand lista
numere = numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
Iterati prin ea
Afisati de cate ori apare 3
(nu aveti voie sa folositi count)'''

numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
x = 0
for numar in numere:
    if numar == 3:
        x = x + 1
    print(f'Numarul 3 apare de {x} ori in lista de numere')

'''8: Aceeasi lista
Iterati prin ea
Calculati si afisati suma numerelor
(nu aveti voie sa folositi sum)'''

numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
sum = 0
for numar in numere:
    sum = sum + numar;
print(f'Suma nr este {sum}')

'''9: Aceeasi lista
Iterati prin ea
Afisati cel mai mare numar
(nu aveti voie sa folositi max)'''

numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
max = numere[0]
for numar in numere:
    if numar > max:
        max = numar
print(f'Cel mai mare numar din lista este: {max}')

'''10: Aceeasi lista
Iterati prin ea
Daca numarul e pozitiv, inlocuiti-l cu valoarea lui negativa
Ex: daca e 3, sa devina -3
Afisati noua lista'''

numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
lista_neg = []
for numar in numere:
    if numar > 0:
        numar = numar - numar*2
    lista_neg.append(numar)
print(f'Lista a devenit: {lista_neg}')


