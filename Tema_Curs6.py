'''1: '''
class Cerc:
    raza = ''
    culoare = ''

    def __init__(self, raza, culoare):
        self.raza = raza
        self.culoare = culoare

    def descrie_cerc(self):
        print(f'Cercul are raza {self.raza} si culoarea {self.culoare} ')

    def aria(self):
        return self.raza * self.raza * 3.14

    def diametru(self):
        return self.raza * self.raza

    def circumferinta(self):
        return 2 * 3.14 * self.raza


cerc1 = Cerc(6, 'Rosu')
cerc2 = Cerc(15, 'Verde')
cerc1.descrie_cerc()
cerc2.descrie_cerc()
cerc1.aria()
print(f'Aria este {cerc1.aria()}')
cerc2.aria()
print(f'Aria este {cerc2.aria()}')
cerc1.diametru()
print(f'Diametrul cercului este {cerc1.diametru()}')
cerc2.diametru()
print(f'Diametrul cercului este {cerc2.diametru()}')
cerc1.circumferinta()
print(f'Circumferinta cercului este {cerc1.circumferinta()}')
cerc2.circumferinta()
print(f'Circumferinta cercului este {cerc2.circumferinta()}')

'''2: '''
class Dreptunghi:
    lungime = ''
    latime = ''
    culoare = ''

    def __init__(self, lungime, latime, culoare):
        self.lungime = lungime
        self.latime = latime
        self.culoare = culoare

    def descrie(self):
        print(f'Dreptunghiul are lungimea {self.lungime}, latimea {self.latime} si culoarea {self.culoare}')

    def aria(self):
        return self.latime * self.lungime

    def perimetrul(self):
        return 2 * (self.latime + self.lungime)

    def schimba_culoarea(self, noua_culoare):
        self.culoare = noua_culoare


drep1 = Dreptunghi(3, 10, "Alb")
drep2 = Dreptunghi(12, 5, "rosu")
drep1.descrie()
drep2.descrie()
print(f'Aria este {drep1.aria()}')
print(f'Aria este {drep2.aria()}')
print(f'Perimetrul este {drep1.perimetrul()}')
print(f'Perimetrul este {drep2.perimetrul()}')
drep1.schimba_culoarea('Verde')
drep2.schimba_culoarea('Albastru')
drep1.descrie()
drep2.descrie()

'''3: '''
class Angajat:
    nume = ''
    prenume = ''
    salariu = ''

    def __init__(self, nume, prenume, salariu):
        self.nume = nume
        self.prenume = prenume
        self.salariu = salariu

    def descrie(self):
        print(f'Angajatul cu numele {self.nume} {self.prenume} are salariul de {self.salariu} lei')

    def nume_complet(self):
        return f'{self.nume} {self.prenume}'

    def salariu_lunar(self):
        return self.salariu

    def salariu_anual(self):
        return self.salariu * 12

    def marire_salariu(self, procent):
        print(f'Angajatul cu numele {self.nume} {self.prenume} are o marire de {procent}%')

angajat1 = Angajat('Vasilache', 'Marcel', 3000)
angajat2 = Angajat('Tudor', 'Maria', 4500)
angajat1.descrie()
angajat2.descrie()
print(f'Salariul lunar este {angajat1.salariu_lunar()}' )
print(f'Salariul lunar este {angajat2.salariu_lunar()}' )
print(f'Salariul anual este {angajat1.salariu_anual()}')
print(f'Salariul anual este {angajat2.salariu_anual()}')
angajat1.marire_salariu(12)
angajat2.marire_salariu(15)

'''4: '''
class Cont:
    iban = ""
    titular_cont = ""
    sold = ""

    def __init__(self, iban, titular_cont, sold):
        self.iban = iban
        self.titular_cont = titular_cont
        self.sold = sold

    def afisare_sold(self):
        print(f'Titularul {self.titular_cont} are in contul {self.iban} suma de {self.sold} lei.')

    def debitare_cont(self, suma):
        self.sold = self.sold - suma
        print(f'Soldul dupa debitare: {self.sold}')

    def creditare_cont(self, suma):
        self.sold = self.sold + suma
        print(f'Soldul dupa crebitare: {self.sold}')

sold1 = Cont("Diaconu Andrei", "IB5236", 100000)
sold2 = Cont('Mirica Ana', 'IB4586', 200000)
sold1.afisare_sold()
sold2.afisare_sold()
sold1.debitare_cont(25000)
sold2.debitare_cont(35000)
sold1.creditare_cont(70000)
sold2.creditare_cont(12000)




