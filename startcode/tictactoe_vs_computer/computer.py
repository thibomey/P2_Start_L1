# Laten we een programma schrijven dat tic-tac-toe tegen ons kan spelen.
#
# De redenering van de computer is als volgt:
# - Indien het mogelijk is voor de computer om te winnen met de volgende zet, moet de computer die zet spelen.
# - Als dat niet mogelijk is, controleert de computer of de tegenspeler zou kunnen winnen in diens volgende zet.
#   Want als dat het geval is, blokkeert de computer de speler.
# - Maar indien noch de computer, noch de speler kunnen winnen, zet dan een random zet.

# Een functie vind_beste_zet(bord, speler)
# - Nagaan of de speler in één zet kan winnen
# - Return de positie waarmee de speler kan winnen
#
# De logica die controleert of er in de huidige zet gewonnen kan worden:
#
# Overloop alle vakjes van het bord. Dat doe je door alle rijen te overlopen, en daarin alle kolommen (vakjes).
# Voor elk van die vakjes, kijk je of die nog leeg is. Als dat het geval is, zetten we onze speler daar.
# Met onze speler op die plaats, kijken we nu of dat bord een winnaar heeft, met de functie controleer_winnaar.
#
# Als dat zo is, hebben we onze ideale zet gevonden, en geven we de rij en kolom terug. Maar anders maken we het vakje wel terug leeg.
#
# Als we na het overlopen van alle vakjes nog geen winnaar hebben, geven we niets terug als rij en kolom.



# Een functie random_zet(bord)
# - Return een random locatie op het bord dat vrij is.
# Maak een oneindige lus met:
# - Random rij
# - Random kolom
# - Als de locatie vrij is deze returnt
# We blijven dus proberen tot de locatie vrij is.



# Een functie computer_zet(bord, speler, tegenspeler)
# - Nagaan of we in deze beurt kunnen winnen
# - Nagaan of de tegenspeler in de volgende beurt kan winnen en deze blokkeren
# - Anders op een random lege locatie plaatsen



# Pas nu de main aan:
# Zet rond de input een ‘if’ om te controleren of de speler aan de beurt is.
# Anders zet je rij en kolom gelijk aan de return van computer_zet(bord, huidige_speler)