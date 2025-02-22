# Schrijf een functie is_getal_geraden die op basis van een gok en een geheim_nummer controleert of de gok correct was.
# Print hier een boodschap, en return de juiste waarde.
from random import randint


def is_getal_geraden (gok, geheim_nummer):
    if gok == geheim_nummer:
        print("correct")
        return True
    else:
        print("incorrect")
        return False

# Schrijf een functie raad_het_getal, die op basis van een bovengrens het raadspel zal spelen.
def raad_het_getal(bovengrens):
    geheim_nummer = randint(1, bovengrens)
    einde_spel = False
    while not einde_spel:
        gok = int(input("Geef een getal "))
        geraden = is_getal_geraden(gok, geheim_nummer)
        if geraden == True:
            einde_spel = True
raad_het_getal(10)