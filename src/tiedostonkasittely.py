"""Tästä tiedostosta löytyvät metodit datan käsittelyyn telegrammista otettuun
.json tiedostoihin."""

import json, os, string
import konfiguraatio
from sanarakenne import SanaRakenne
from trie import TrieNode


def load_data_dict():
    """Lataa data kansiossa olevan .json tiedoston dictionaryyn

    Returns:
        dictionary: palauttaa parsitut sanayhdistelmät SanaRakenne muodossa
    """
    file = avaa_tiedosto()
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

    for rivi in json.loads(file.read())['messages']:
        parse_sentence(str(rivi['text']))
    return data

def load_data_trie():
    juuri = TrieNode(sanat=None)
    file = avaa_tiedosto()
    for rivi in json.loads(file.read())['messages']:
        rivi = str(rivi['text']).lower().translate(str.maketrans('', '', string.punctuation)).split()
        for i in range(len(rivi)-(konfiguraatio.ASTE+1)):
            juuri.lisaa(rivi[int(i):int(i)+konfiguraatio.ASTE+1])
    return juuri

def avaa_tiedosto():
    path = '/src/data/tkoaly.json'
    path = os.getcwd() + path
    try:
        file = open(path, "r", encoding="utf8")
    #ToDo: Paremmat poikkeukset
    except Exception:
        raise Exception("Ongelmia tiedoston avaamisessa.")
    return file

if __name__ == "__main__":
    data = load_data_trie()
    sana = "asdf"
    while sana:
        sana = input("Anna sana: ")
        print(data.anna_sana(sana))
