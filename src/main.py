"""Main tiedosto, joka kutsuu ensin tiedostonlukijaa ja sitten markov.py
tiedoston lauseen luontia."""
import ui_komennot
import konfiguraatio

if __name__ == "__main__":
    konf = konfiguraatio.Konfiguraatio()
    data = None
    print("Tervetuloa Velin markov-ohjelmaan!")
    ui_komennot.tulosta_komennot()
    while True:
        komento = input("Anna komento (tyhjä lopettaa): ")
        if len(komento) == 0:
            break
        elif komento == "help":
            ui_komennot.tulosta_komennot()
        elif komento == "konfiguraatio":
            ui_komennot.muuta_konfiguraatiota(konf)
        elif komento == "lataa":
            data = ui_komennot.lataa(konf)
        elif komento == "markov":
            if data is None:
                print("Lataa ensin dataa.")
                continue
            ui_komennot.markov(data, konf)
        elif komento == "peli":
            if data is None:
                print("Lataa ensin dataa")
                continue
            ui_komennot.peli(data, konf)
        # Lataa datan sekä trie, että dictionary -rakenteisiin ja vertaa niiden suoritusnopeutta
        elif komento == "test":
            ui_komennot.test(konf)
        else:
            print("Tuntematon komento.")
