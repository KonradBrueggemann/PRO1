class Lebewesen:
    def __init__(self,alter, groesse, gewicht, maxLebensdauer, verbreitungsgebiet, lebendig):
        self.alter = alter
        self.groesse = groesse
        self.gewicht = gewicht
        self.maxLebensdauer = maxLebensdauer
        self.verbreitungsgebiet = verbreitungsgebiet
        self.lebendig = lebendig

    def altern(self, jahre):
        """

        Vorbedingung:
        alter < maxLebensdauer
        alter, maxLebensdauer müssen den Typ int haben.

        """
        assert self.alter < self.maxLebensdauer, "Das Lebewesen ist zu alt."
        assert type(self.alter) == int and type(self.maxLebensdauer) == int, "Die Werte sind im falschen Format"

        self.alter += jahre
        if self.alter > self.maxLebensdauer:
            self.lebendig = False

class Tier (Lebewesen):
    def __init__(self,alter, groesse, gewicht, maxLebensdauer, verbreitungsgebiet, anzahlglieder, nahrung, lebendig, satt):
        Lebewesen.__init__(self, alter, groesse, gewicht, maxLebensdauer, verbreitungsgebiet, lebendig)
        self.anzahlGlieder = anzahlglieder
        self.nahrung = nahrung
        self.satt = satt

    def fuettern(self, futter):
        """

        Vorbedingung:
        satt = False
        satt muss den Typ bool haben.
        futter muss den Typ int haben

        """
        assert self.satt == False, "Das Tier ist bereits gesättigt."
        assert type(futter) == int and type(self.satt) == bool

        if futter > 5:
            self.satt = True

class Mensch(Lebewesen):
    def __init__(self,alter, groesse, gewicht, maxLebensdauer, verbreitungsgebiet, anzahlglieder, nahrung, lebendig, arm):
        Lebewesen.__init__(self, alter, groesse, gewicht, maxLebensdauer, verbreitungsgebiet, lebendig)
        self.anzahlGlieder = anzahlglieder
        self.nahrung = nahrung
        self.arm = arm

    def arbeiten(self, stunden):
        """

        Vorbedingung:
        arm = True
        stunden muss den Typ int haben.
        arm muss den Typ bool haben.

        """
        assert self.arm == True, "Der Mensch ist reich und muss nicht arbeiten."
        assert type(stunden) == int and type(self.arm) == bool

        if stunden > 40:
            self.arm = False

class Pflanze(Lebewesen):
    def __init__(self,alter, groesse, gewicht, maxLebensdauer, verbreitungsgebiet, lebendig, wasserstand):
        Lebewesen.__init__(self, alter, groesse, gewicht, maxLebensdauer, verbreitungsgebiet, lebendig)
        self.wasserstand = wasserstand

    def gießen(self, wasser):
        """

        Vorbedingung:
         wasserstand, wasser müssen den Typ int haben.

        """
        assert type(self.wasserstand) == int and type(wasser) == int, "Die Werte sind im falschen Format"

        self.wasserstand += wasser
        if self.wasserstand > 100:
            self.lebendig = True