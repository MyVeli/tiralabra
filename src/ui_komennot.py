import os
from random import randint
from time import time

from tiedostonkasittely import load_data_dict, load_data_trie_telegram, load_data_trie_text
from konfiguraatio import mode_enum
from markov import luo_lause_trie, luo_lause_dict

def help():
    print("Mahdollisia komentoja ovat:")
    print("konfiguraatio - mahdollistaa konfiguraation muuttamisen")
    print("lataa - lataa datan konfiguraation mukaan data kansiosta")
    print("markov - tekstin luomiseen datan perusteella")
    print("peli - aloittaa dataan perustuvan arvailupelin")
    print("tyhjä lopettaa")

def muuta_konfiguraatiota(konfiguraatio):
    while True:
        aste = input("Uusi ketjun aste (tyhjä pitää nykyisen):")
        if aste.isnumeric() and int(aste) > 1:
            konfiguraatio.aste = int(aste)
            break
        elif not aste:
            break
        else:
            print("Anna kokonaisluku, jonka arvo on vähintään 2.")
    while True:
        print("Tallennusasetuksia ovat:")
        print("'dictionary' - käyttää aina 2. asteen ketjua")
        print("'text' - tallentaa trie-rakenteeseen data/teksti-kansion tekstitiedostojen sisällön")
        print("'telegram' - tallentaa trie-rakenteeseen data/telegram-kansion tiedostojen sisällön")
        print("'molemmat' - tallentaa trie rakenteeseen sekä telegram-, että tekstitiedostot")
        mode = input("Valitse uusi tallennusasetus (tyhjä pitää nykyisen): ")
        if not mode:
            break
        elif mode == "dictionary":
            konfiguraatio.mode = mode_enum.DICT
            break
        elif mode == "text":
            konfiguraatio.mode = mode_enum.TEXT
            break
        elif mode == "telegram":
            konfiguraatio.mode = mode_enum.TRIE
            break
        elif mode == "molemmat":
            konfiguraatio.mode = mode_enum.MOLEMMAT
            break
    while True:
        pituus = input("Anna uusi luodun tekstin maksimipituus sanojen määränä: ")
        if pituus.isnumeric() and int(pituus) > 0:
            konfiguraatio.max_pituus = pituus

def peli(data, konfiguraatio):
    tiedostot = ""
    if konfiguraatio.mode == mode_enum.TEXT:
        tiedostot = os.listdir(os.getcwd() + '/src/data/text')
    elif konfiguraatio.mode == mode_enum.DICT:
        tiedostot = os.listdir(os.getcwd() + '/src/data/telegram')
    elif konfiguraatio.mode == mode_enum.MOLEMMAT:
        tiedostot = os.listdir(os.getcwd() + '/src/data/telegram')+os.listdir(os.getcwd() + '/src/data/text')
    else:
        print("Käytä text, telegram, tai molemmat konfiguraatiota jos haluat pelata.")
        return

    tiedosto_nro = randint(0, len(tiedostot)-1)
    lause = input("Anna jatkettava lause tai sana (tyhjä luo satunnaisen): ").split()
    print(luo_lause_trie(data, lause, konfiguraatio, tiedostot[tiedosto_nro]))
    arvaus = input("Mihin tiedostoon lause kuului? Vaihtoehdot: \n"+"\n".join(tiedostot)+"\n")
    if arvaus == tiedostot[tiedosto_nro]:
        print("Oikein!")
    else:
        print("Väärin, oikea tiedosto oli "+str(tiedostot[tiedosto_nro]))


def markov(data, konfiguraatio):
    lause = input("Anna jatkettava lause tai sana (tyhjä luo satunnaisen): ").split()
    if konfiguraatio.mode == mode_enum.TEXT:
        print(luo_lause_trie(data, lause, konfiguraatio))
    elif konfiguraatio.mode == mode_enum.DICT:
        print(luo_lause_dict(data, lause, konfiguraatio))
    elif konfiguraatio.mode == mode_enum.TRIE:
        print(luo_lause_trie(data, lause, konfiguraatio))
    elif konfiguraatio.mode == mode_enum.MOLEMMAT:
        print(luo_lause_trie(data, lause, konfiguraatio))

def lataa(konfiguraatio):
    data = None
    if konfiguraatio.mode == mode_enum.MOLEMMAT:
        data = load_data_trie_text(konfiguraatio)
        data = load_data_trie_telegram(konfiguraatio, data)
    elif konfiguraatio.mode == mode_enum.TEXT:
        data = load_data_trie_text(konfiguraatio)
    elif konfiguraatio.mode == mode_enum.TRIE:
        data = load_data_trie_telegram(konfiguraatio)
    elif konfiguraatio.mode == mode_enum.DICT:
        data = load_data_dict()
    if data is not None:
        print("Data ladattu.")
        return data
    else:
        print("Virhe konfiguraation kanssa.")
        return None

def test(konfiguraatio):
    alku = time()
    data_dictionary = load_data_dict()
    loppu = time()
    print("Dictionary lataus: "+str(loppu-alku))
    alku = time()
    data_trie = load_data_trie_telegram(konfiguraatio)
    loppu = time()
    print("Trie lataus: "+str(loppu-alku))
    alku = time()
    for i in range(konfiguraatio.hakuja):
        luo_lause_dict(data_dictionary, "on".split(), konfiguraatio)
    loppu = time()
    print("Dictionary "+str(konfiguraatio.hakuja)+ " hakua kesti: "+str(loppu-alku))
    alku = time()
    for i in range(konfiguraatio.hakuja):
        luo_lause_trie(data_trie, "on".split(), konfiguraatio)
    loppu = time()
    print("Trie "+str(konfiguraatio.hakuja)+ " hakua kesti: "+str(loppu-alku))
