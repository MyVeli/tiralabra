"""Main tiedosto, joka kutsuu ensin tiedostonlukijaa ja sitten markov.py
tiedoston lauseen luontia."""
from time import time
from tiedostonkasittely import load_data_dict, load_data_trie_telegram, load_data_trie_text
from markov import luo_lause_dict, luo_lause_trie
import konfiguraatio
#import psutil

if __name__ == "__main__":

    # Tämä lukee kaikki kansiossa text olevat tiedostot ja tallentaa niiden datan trie-rakenteeseen
    if konfiguraatio.MODE == konfiguraatio.mode_enum.TEXT:
        data = load_data_trie_text()
        while True:
            lause = input("Anna jatkettava lause tai sana (tyhjä lopettaa): ").split()
            if lause:
                print(luo_lause_trie(data, lause))
            else:
                break

    # Lukee kaikki kansion telegram tiedostot ja tallentaa niiden datan dictionary rakenteeseen
    elif konfiguraatio.MODE == konfiguraatio.mode_enum.DICT:
        data = load_data_dict()
        #print(str(psutil.Process().memory_info().rss/1024))
        while True:
            lause = input("Anna jatkettava lause tai sana (tyhjä lopettaa): ").split()
            if lause:
                print(luo_lause_dict(data, lause))
            else:
                break
    
    # Lukee kaikki kansion telegram tiedostot ja tallentaa niiden datan dictionary rakenteeseen
    elif konfiguraatio.MODE == konfiguraatio.mode_enum.TRIE:
        data = load_data_trie_telegram()
        #print(str(psutil.Process().memory_info().rss/1024))
        while True:
            lause = input("Anna jatkettava lause tai sana (tyhjä lopettaa): ").split()
            if lause:
                print(luo_lause_trie(data, lause))
            else:
                break

    # Lataa datan sekä trie, että dictionary -rakenteisiin ja vertaa niiden suoritusnopeutta
    elif konfiguraatio.MODE == konfiguraatio.mode_enum.TEST:
        alku = time()
        data_dictionary = load_data_dict()
        loppu = time()
        print("Dictionary lataus: "+str(loppu-alku))
        alku = time()
        data_trie = load_data_trie_telegram()
        loppu = time()
        print("Trie lataus: "+str(loppu-alku))
        alku = time()
        for i in range(konfiguraatio.HAKUJA):
            luo_lause_dict(data_dictionary, "on".split())
        loppu = time()
        print("Dictionary "+str(konfiguraatio.HAKUJA)+ " hakua kesti: "+str(loppu-alku))
        alku = time()
        for i in range(konfiguraatio.HAKUJA):
            luo_lause_trie(data_trie, "on".split())
        loppu = time()
        print("Trie "+str(konfiguraatio.HAKUJA)+ " hakua kesti: "+str(loppu-alku))
