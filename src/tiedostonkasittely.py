"""Tästä tiedostosta löytyvät metodit datan käsittelyyn telegrammista otettuun
.json tiedostoihin."""

import json
import os
import string
from dict_sanarakenne import SanaRakenne


def load_data_dict():
    """Lataa data kansiossa olevan .json tiedoston dictionaryyn

    Returns:
        dictionary: palauttaa parsitut sanayhdistelmät SanaRakenne muodossa
    """
    path = '/src/data/tkoaly.json'
    path = os.getcwd() + path
    try:
        file = open(path, "r", encoding="utf8")
    #ToDo: Paremmat poikkeukset
    except Exception:
        print("Ongelmia tiedoston avaamisessa.")
        raise Exception("Ongelmia tiedoston avaamisessa.")
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
