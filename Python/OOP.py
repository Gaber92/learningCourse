class Zivila():
    ime = None
    kalorije = None
    priljubljenost = None

    def __init__(self, ime, kalorije, priljubljenost):
        self.ime = ime
        self.kalorije = kalorije
        self.priljubljenost = priljubljenost

    def addSugar(self):
        self.kalorije += 300
        self.priljubljenost -= 1


class Hrana(Zivila):
    teza = None

    def __init__(self, ime, teza, kalorije, priljubljenost):
        super().__init__(ime, kalorije, priljubljenost)
        self.teza = teza


class Pijaca(Zivila):
    volumen = None

    def __init__(self, ime, volumen, kalorije, priljubljenost):
        super().__init__(ime, kalorije, priljubljenost)
        self.volumen = volumen


caj = Pijaca("Planinski", 0.3, 0.1, 3)
pivo = Pijaca("Laško", 0.5, 350, 9)

krof = Hrana("trojanski krof", 0.25, 600, 5)
brokoli = Hrana("domač brokoli", 0.125, 45, 2)
snicl = Hrana("dunajski zrezek", 0.300, 500, 7)

print(krof.kalorije)
krof.addSugar()
print(krof.kalorije)
print(caj.volumen)
print(pivo.kalorije)

caj.addSugar()
print(caj.kalorije)
