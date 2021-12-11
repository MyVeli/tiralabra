"""Tästä tiedostosta löytyvät metodit datan käsittelyyn telegrammista otettuun
.json tiedostoihin."""

import json
import os
import string
import konfiguraatio
from sanarakenne import SanaRakenne
from trie import TrieNode


def load_data_dict():
    """Lataa data kansiossa olevan .json tiedoston dictionaryyn

    Returns:
        dictionary: palauttaa parsitut sanayhdistelmät SanaRakenne muodossa
    """

    data = {}

    def parse_sentence(lause):
        """Parsii yksittäisen lauseen dictionaryyn. Käyttää dict_sanarakenne luokkaa.

        Args:
            lause (string): sisältää tekstin yhdestä lauseesta
        """
        lause = lause.split()
        edellinen1 = ""
        edellinen2 = ""

        for i in lause:
            i = i.lower().translate(str.maketrans('', '', string.punctuation))
            if edellinen1 == "":
                edellinen1 = i
                continue
            if edellinen2 == "":
                edellinen2 = edellinen1
                edellinen1 = i
                continue
            if (edellinen2,edellinen1) in data:
                data[(edellinen2,edellinen1)].lisaa_sana(i)
            else:
                data[(edellinen2,edellinen1)] = SanaRakenne(i)
            if edellinen1 in data:
                data[edellinen1].lisaa_sana(i)
            else:
                data[edellinen1] = SanaRakenne(i)
            edellinen2 = edellinen1
            edellinen1 = i

    polku = os.getcwd() + '/src/data/telegram'
    for tiedosto in os.listdir(polku):
        file = __avaa_tiedosto(polku+'/'+tiedosto)
        for rivi in json.loads(file.read())['messages']:
            parse_sentence(str(rivi['text']))
    return data

def load_data_trie_telegram():
    """Lataa datan data-kansiosta trie-rakenteeseen

    Returns:
        TrieNode: sanat ja sanayhteydet trie-rakenteessa
    """
    juuri = TrieNode(sanat=None)
    polku = os.getcwd() + '/src/data/telegram'
    for tiedosto in os.listdir(polku):
        file = __avaa_tiedosto(polku+'/'+tiedosto)
        for rivi in json.loads(file.read())['messages']:
            rivi = str(rivi['text']).lower()\
                .translate(str.maketrans('', '', string.punctuation)).split()
            for i in range(len(rivi)-(konfiguraatio.ASTE+1)):
                j = konfiguraatio.ASTE
                while j >= 0:
                    temp = []
                    temp.append(rivi[int(i):int(i)+j])
                    temp.append(rivi[int(i)+j])
                    juuri.lisaa(temp)
                    j -= 1
    return juuri

def load_data_trie_text():
    """Lataa datan data-kansiosta trie-rakenteeseen

    Returns:
        TrieNode: sanat ja sanayhteydet trie-rakenteessa
    """
    juuri = TrieNode(sanat=None)
    polku = os.getcwd() + '/src/data/text'
    for tiedosto in os.listdir(polku):
        file = __avaa_tiedosto(polku+'/'+tiedosto)
        rivi = file.read().lower().split()
        for i in range(len(rivi)-(konfiguraatio.ASTE+1)):
            j = konfiguraatio.ASTE
            while j >= 0:
                temp = []
                temp.append(rivi[int(i):int(i)+j])
                temp.append(rivi[int(i)+j])
                juuri.lisaa(temp)
                j -= 1
                """ temp = []
                temp.append(' '.join(rivi[int(i):int(i)+j]))
                temp.append(rivi[int(i)+j])
                juuri.lisaa(temp)
                j -= 1"""
    return juuri

def __avaa_tiedosto(polku):
    """Avaa tiedoston

    Raises:
        Exception: Nostaa virheen, mikäli avaaminen ei onnistunut

    Returns:
        connection: palauttaa tiedostoyhteyden
    """
    try:
        file = open(polku, "r", encoding="utf8")
    #ToDo: Paremmat poikkeukset
    except Exception:
        raise Exception("Ongelmia tiedoston avaamisessa.")
    return file
