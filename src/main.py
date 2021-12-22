"""Main tiedosto, joka kutsuu ensin tiedostonlukijaa ja sitten markov.py
tiedoston lauseen luontia."""
from time import time
from tiedostonkasittely import load_data_dict, load_data_trie_telegram, load_data_trie_text
from markov import luo_lause_dict, luo_lause_trie
import ui_komennot
import konfiguraatio

if __name__ == "__main__":

    konf = konfiguraatio.Konfiguraatio()
    data = None
    print("Tervetuloa Velin markov-ohjelmaan!")
    ui_komennot.help()
    while True:
        komento = input("Anna komento: ")
        if len(komento) == 0:
            break
        elif komento == "help":
            ui_komennot.help()
        elif komento == "konfiguraatio":
            ui_komennot.muuta_konfiguraatiota(konf)
        elif komento == "lataa":
            data = None
            if konf.mode == konfiguraatio.mode_enum.MOLEMMAT:
                data = load_data_trie_text(konf)
                data = load_data_trie_telegram(konf, data)
            elif konf.mode == konfiguraatio.mode_enum.TEXT:
                data = load_data_trie_text(konf)
            elif konf.mode == konfiguraatio.mode_enum.TRIE:
                data = load_data_trie_telegram(konf)
            elif konf.mode == konfiguraatio.mode_enum.DICT:
                data = load_data_dict()
            if data is not None:
                print("Data ladattu.")
            else:
                print("Virhe konfiguraation kanssa.")
        elif komento == "markov":
            if data is None:
                print("Lataa ensin dataa.")
                continue
            ui_komennot.markov(data, konf)
        elif komento == "peli":
            if data is None:
                print("Lataa ensin dataa")
            ui_komennot.peli(data, konf)
        elif komento == "test":
            break
        else:
            print("Tuntematon komento.")
    
    # Lataa datan sekä trie, että dictionary -rakenteisiin ja vertaa niiden suoritusnopeutta
    if konf.mode == konfiguraatio.mode_enum.TEST:
        alku = time()
        data_dictionary = load_data_dict()
        loppu = time()
        print("Dictionary lataus: "+str(loppu-alku))
        alku = time()
        data_trie = load_data_trie_telegram()
        loppu = time()
        print("Trie lataus: "+str(loppu-alku))
        alku = time()
        for i in range(konfiguraatio.hakuja):
            luo_lause_dict(data_dictionary, "on".split())
        loppu = time()
        print("Dictionary "+str(konfiguraatio.HAKUJA)+ " hakua kesti: "+str(loppu-alku))
        alku = time()
        for i in range(konfiguraatio.HAKUJA):
            luo_lause_trie(data_trie, "on".split())
        loppu = time()
        print("Trie "+str(konfiguraatio.HAKUJA)+ " hakua kesti: "+str(loppu-alku))
