"""Main tiedosto, joka kutsuu ensin tiedostonlukijaa ja sitten markov.py
tiedoston lauseen luontia."""
from time import time
from tiedostonkasittely import load_data_dict, load_data_trie, load_data_trie_text
from markov import luo_lause, luo_lause_trie
import konfiguraatio
#import psutil

if __name__ == "__main__":

    if konfiguraatio.MODE == konfiguraatio.mode_enum.TEXT:
        data = load_data_trie_text()
        while True:
            lause = input("Anna jatkettava lause tai sana (tyhjä lopettaa): ").split()
            if lause:
                print(luo_lause_trie(data, lause))
            else:
                break

    elif konfiguraatio.MODE == konfiguraatio.mode_enum.DICT:
        data = load_data_dict()
        #print(str(psutil.Process().memory_info().rss/1024))
        while True:
            lause = input("Anna jatkettava lause tai sana (tyhjä lopettaa): ").split()
            if lause:
                print(luo_lause(data, lause))
            else:
                break

    elif konfiguraatio.MODE == konfiguraatio.mode_enum.TRIE:
        data = load_data_trie()
        #print(str(psutil.Process().memory_info().rss/1024))
        while True:
            lause = input("Anna jatkettava lause tai sana (tyhjä lopettaa): ").split()
            if lause:
                print(luo_lause_trie(data, lause))
            else:
                break

    elif konfiguraatio.MODE == konfiguraatio.mode_enum.TEST:
        alku = time()
        data_dictionary = load_data_dict()
        loppu = time()
        print("Dictionary lataus: "+str(loppu-alku))
        alku = time()
        data_trie = load_data_trie()
        loppu = time()
        print("Trie lataus: "+str(loppu-alku))
        alku = time()
        for i in range(konfiguraatio.HAKUJA):
            luo_lause(data_dictionary, "on".split())
        loppu = time()
        print("Dictionary "+str(konfiguraatio.HAKUJA)+ " hakua kesti: "+str(loppu-alku))
        alku = time()
        for i in range(konfiguraatio.HAKUJA):
            luo_lause_trie(data_trie, "on".split())
        loppu = time()
        print("Trie "+str(konfiguraatio.HAKUJA)+ " hakua kesti: "+str(loppu-alku))
