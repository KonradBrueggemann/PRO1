from lebewesen import Lebewesen
from lebewesen import Tier
from lebewesen import Mensch
from lebewesen import Pflanze

Katze = Lebewesen(alter= 25, groesse= 80, gewicht= 3, maxLebensdauer=20, verbreitungsgebiet="Mein Haus", lebendig= True)

Gorilla = Tier(alter= 18, groesse= 200, gewicht= 300, maxLebensdauer= 50, verbreitungsgebiet= "Zoo", anzahlglieder= 4, nahrung= "Affig", lebendig= True, satt= False)

Konrad = Mensch(alter= 19, groesse= 180, gewicht= 83, maxLebensdauer= 80, verbreitungsgebiet= "Babelsberg", anzahlglieder= 4, nahrung= "Mischmasch", lebendig= True, arm= False)

Kaktus = Pflanze(alter= 25, groesse= 120, gewicht= 20, maxLebensdauer= 200, verbreitungsgebiet= "Wüste", lebendig= False, wasserstand= 80)

if __name__ == "__main__":
    #print(Katze.alter)
    #Katze.altern(21)
    #print(Katze.alter)
    #print(Katze.lebendig)
    #print(Gorilla.satt)
    #Gorilla.fuettern(10)
    #print(Gorilla.satt)
    #print(Konrad.arm)
    #Konrad.arbeiten(10)
    #print(Konrad.arm)
    #print(Kaktus.lebendig)
    #Kaktus.gießen(5)
    #Kaktus.gießen(20)
    #print(Kaktus.lebendig)