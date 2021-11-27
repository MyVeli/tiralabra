"""Tiedostonkäsittely tekstitiedostoja varten. 
"""

import os
import konfiguraatio
from trie import TrieNode

def load_data_trie():
    """Lataa datan data-kansiosta trie-rakenteeseen

    Returns:
        TrieNode: sanat ja sanayhteydet trie-rakenteessa
    """
    juuri = TrieNode(sanat=None)
    file = avaa_tiedosto()
    rivi = file.read().lower().split()
    for i in range(len(rivi)-(konfiguraatio.ASTE+1)):
        for j in range(konfiguraatio.ASTE):
            temp = []
            temp.append(' '.join(rivi[int(i)+int(j):int(i)+konfiguraatio.ASTE]))
            temp.append(rivi[int(i)+konfiguraatio.ASTE])
            juuri.lisaa(temp)
    return juuri

def avaa_tiedosto():
    """Avaa tiedoston

    Raises:
        Exception: Nostaa virheen, mikäli avaaminen ei onnistunut

    Returns:
        connection: palauttaa tiedostoyhteyden
    """
    path = '/src/data/vihr_ohjelma.txt'
    path = os.getcwd() + path
    try:
        file = open(path, "r", encoding="utf8")
    #ToDo: Paremmat poikkeukset
    except Exception:
        raise Exception("Ongelmia tiedoston avaamisessa.")
    return file

if __name__ == "__main__":
    load_data_trie()
