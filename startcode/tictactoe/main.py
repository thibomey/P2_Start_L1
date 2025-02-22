# Maak een functie tic_tac_toe(), die ons hele hoofdprogramma bevat
from startcode.tictactoe.mytictactoe import initialiseer_bord
from startcode.tictactoe.mytictactoe import print_bord
from startcode.tictactoe.mytictactoe import zet

def tic_tac_toe():
    bord = initialiseer_bord()
    huidige_speler = "x"
    einde_spel = False
    winnar = ""
    teller = 0
    while not einde_spel:
        print_bord(bord)
        rij = int(input("Kies een rij (1,2,3) "))
        kolom =int(input("Kies een kolom (1,2,3) "))

        bord = zet(bord, rij, kolom, huidige_speler)

        if huidige_speler == "x"
            huidige_speler = "o"
        else:
            huidige_speler = "x"

tic_tac_toe()