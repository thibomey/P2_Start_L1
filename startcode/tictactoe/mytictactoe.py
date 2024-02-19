def initialiseer_bord():
    # bord = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    bord = []
    for rij in range(3):
        rij_inhoud = []
        for kolom in range(3):
            rij_inhoud.append(' ')
        bord.append(rij_inhoud)
    return bord

# Maak een functie zet.  Die functie geeft het bord terug, waarop de nieuwe zet werd geplaatst.
def zet():


# Print eerst een nieuwe (lege) lijn
# Print voor elke rij in het bord, de elementen van die rij met telkens een ‘’|' ertussen.
#   Tip: Zoek op internet naar: python string join()
# tussen elke rij zet je 5 keer een ‘-’
def print_bord(bord):

# Het spel moet ook kunnen controleren of de input van de gebruiker wel geldig is.
# Dat betekent: de positie moet in het veld liggen, én het vakje moet nog vrij zijn.
# Valsspelen mag dus(uiteraard) niet.
# Maak een functie controleer_input met als parameters: bord, rij, kolom
# - Ga na of de positie in het veld ligt, op basis van de rij en de kolom
# - Ga na of het vakje nog vrij is
# - Return True of False
def controleer_input(bord, rij, kolom):


# Maak een functie controleer_winnaar(bord)
# - Dat de volgende functies oproept
#     - controleer_horizontaal(bord)
#     - controleer_verticaal(bord)
#     - controleer_diagonaal(bord)
# - True of False returnt
def controleer_winnaar(bord):


# Maak een functie controleer_horizontaal(bord) die:
# - Voor elke rij van het bord controleert op een winnaar
#     - Hiervoor moeten drie vakjes aan elkaar gelijk zijn maar niet leeg (gelijk aan ‘ ’)
#     - Je kan vergelijkingen schakelen in Python. Bijvoorbeeld:
#     - volgorde_juist = a < b < c   of if a == b != c
# - True of False teruggeeft
def controleer_horizontaal(bord):


# Maak een functie controleer_verticaal(bord) dat:
# - Voor elke kolom van het bord controleert op een winnaar
#     - Gelijkaardig als bij de vorige functie
# - True of False returnt
def controleer_verticaal(bord):


# Maak een functie controleer_diagonaal(bord) dat:
# - Voor de twee diagonalen van het bord controleert op een winnaar
# - True of False teruggeeft
def controleer_diagonaal(bord):