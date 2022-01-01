"""Tästä tiedostosta löytyvät metodit datan käsittelyyn telegrammista otettuun
.json tiedostoihin."""

import json
import os
import string
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
        try:
            file = __avaa_tiedosto(polku+'/'+tiedosto)
        except:
            print("Ongelmia tiedoston "+str(tiedosto)+" avaamisessa")
            continue
        try:
            for rivi in json.loads(file.read())['messages']:
                parse_sentence(str(rivi['text']))
        except:
            print(tiedosto+" ei ole oikean muotoinen."
                +"Tarkista kansion data/telegram sisältö ja lataa uudestaan.")
    return data

def load_data_trie_telegram(konfiguraatio, juuri=None):
    """Lataa datan data-kansiosta trie-rakenteeseen

    Returns:
        TrieNode: sanat ja sanayhteydet trie-rakenteessa
    """
    if juuri is None:
        juuri = TrieNode(sanat=None)
    polku = os.getcwd() + '/src/data/telegram'
    for tiedosto in os.listdir(polku):
        try:
            file = __avaa_tiedosto(polku+'/'+tiedosto)
        except:
            print("Ongelmia tiedoston "+str(tiedosto)+" avaamisessa")
            continue
        # Vain .json tiedostot kelpaavat telegrammista
        if tiedosto.split(".")[1] != "json":
            print("Ohitetaan "+tiedosto+", koska se ei ole .json muotoinen")
            continue
        for rivi in json.loads(file.read())['messages']:
            try:
                # Vain tekstikentän sisältö halutaan mukaan. Jos sitä ei löydy,
                # tiedosto on väärän mallinen.
                rivi = str(rivi['text']).lower()\
                .translate(str.maketrans('', '', string.punctuation)).split()
            except:
                print(tiedosto+" ei ole oikean muotoinen."
                    +"Tarkista kansion data/telegram sisältö ja lataa uudestaan.")
                return None
            for i in range(len(rivi)-(konfiguraatio.aste+1)):
                j = konfiguraatio.aste
                while j >= 0:
                    temp = []
                    temp.append(rivi[int(i):int(i)+j])
                    temp.append(rivi[int(i)+j])
                    juuri.lisaa(temp, alkupera=str(tiedosto))
                    j -= 1
    return juuri

def load_data_trie_text(konfiguraatio, juuri=None):
    """Lataa datan data-kansiosta trie-rakenteeseen

    Returns:
        TrieNode: sanat ja sanayhteydet trie-rakenteessa
    """
    if juuri is None:
        juuri = TrieNode(sanat=None)
    polku = os.getcwd() + '/src/data/text'
    for tiedosto in os.listdir(polku):
        try:
            file = __avaa_tiedosto(polku+'/'+tiedosto)
        except:
            print("Ongelmia tiedoston "+str(tiedosto)+" avaamisessa")
            continue
        # Luetaan vain .txt tiedostoja
        if tiedosto.split(".")[1] != "txt":
            print("Ohitetaan "+tiedosto+", koska se ei ole .txt muotoinen")
            continue
        teksti = file.read().lower().split()
        for i in range(len(teksti)-(konfiguraatio.aste+1)):
            j = konfiguraatio.aste
            while j >= 0:
                temp = []
                temp.append(teksti[int(i):int(i)+j])
                temp.append(teksti[int(i)+j])
                juuri.lisaa(temp, alkupera=tiedosto)
                j -= 1
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
    except Exception:
        raise Exception("Ongelmia tiedoston avaamisessa.")
    return file
