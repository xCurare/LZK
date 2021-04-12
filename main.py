import datetime


class Artikel:
    def __init__(self, name, preis, anzahl):
        self.name = name
        self.preis = preis
        self.anzahl = anzahl


class Inventar:
    def __init__(self):
        self.artikelliste = []

    def add_artikel(self, name, preis, anzahl):
        a = self.finde_artikel(name)
        if a is None:
            self.artikelliste.append(Artikel(name=name, preis=preis, anzahl=anzahl))
        else:
            a.preis = preis
            a.anzahl += anzahl

    def finde_artikel(self, name):
        for artikel in self.artikelliste:
            if artikel.name == name:
                return artikel
        return None  # falls Artikel nicht gefunden wurde

    def check_inventar(self, limit=5):
        for artikel in self.artikelliste:
            if artikel.anzahl <= limit:
                print(
                    '>> Artikel {} : Stückzahl = {} <= 5, Nachbestellung erforderlich!'.format(artikel.name,
                                                                                               artikel.anzahl))

    def liste_inventar(self):
        print('--- Vorhandenes Inventar ---')
        for artikel in self.artikelliste:
            print(artikel.name, artikel.anzahl)
        print('-----------------')
        self.check_inventar()
        print('\n')

    def return_Rechnung(self, artikel: list, stk: list, rabatt=None, mwst=0.16):
        global rechnungsnummer  # sollte irgendwie anders gemacht werden
        rechnungsnummer += 1

        print('-----------------')
        print('Rechnung')
        print('-----------------')
        print('Dennis Vinke')
        print('Nilay-Benli-Straße in 30489 Niklashausen')
        print('Steuernummer 123123123')
        print('-----------------')
        print('Rechnungsnummer:', rechnungsnummer)
        print('-----------------')
        print('Artikel Stk Preis')
        summe = 0
        summe_s = 0

        for a, s in zip(artikel, stk):
            a_i = self.finde_artikel(a)
            teilsumme = a_i.preis * s
            summe += a_i.preis * s
            a_i.anzahl -= s
            summe_s += s
            print(a, s, '{:.2f} €'.format(teilsumme))
        print('-----------------')

        if summe_s >= 3 and rabatt is None:
            rabatt = 0.03
        if rabatt is not None:
            print('Rabatt {:.0f}%: {:.2f} €'.format(rabatt * 100, -summe * rabatt))
            summe = summe * (1 - rabatt)

        print('Summe: {:.2f} €'.format(summe))
        print('Enthaltene MwSt.: {:.2f} € \n'.format(summe * mwst))
        print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        print('\n See you soon ಠ_ಠ \n')

        self.check_inventar()
        print('\n')


# import
namen = [
    'New Silvans Turbo (DVD)',
    'Afrim und Bashkim (DVD)',
    'Daniel allein zu Haus (DVD)',
    'Call of Duty – Phillips War (PC)',
    'Call of Duty – Phillips War (PS4)',
    'Cybernico 2077  (PC)',
    'Cybernico 2077 (PS4)']

preise_netto = [
    7.50,
    6.00,
    4.50,
    30.00,
    40.00,
    40.00,
    50.00, ]

anzahl = [20] * len(preise_netto)  # weil faul

# Stelle Inventar zusammen
inventar = Inventar()
for i in range(len(namen)):
    inventar.add_artikel(name=namen[i], preis=preise_netto[i],
                         anzahl=anzahl[i])  # loop könnte auch in der Klassenmoethode stattfinden

rechnungsnummer=0
# Rechnung Nr 1
inventar.return_Rechnung(
    artikel=['Afrim und Bashkim (DVD)', 'Call of Duty – Phillips War (PS4)', 'Cybernico 2077  (PC)'],
    stk=[1, 1, 2])

# Rechnung Nr 2
inventar.return_Rechnung(
    artikel=['Afrim und Bashkim (DVD)'],
    stk=[15])

# check Inventar
inventar.liste_inventar()
