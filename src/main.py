"""Main tiedosto, joka kutsuu ensin tiedostonlukijaa ja sitten markov.py
tiedoston lauseen luontia."""
from tiedostonkasittely import load_data_dict
from markov import luo_lause

if __name__ == "__main__":
    DICTIONARY = True
    if DICTIONARY:
        data = load_data_dict()
        lause = input("Anna jatkettava lause tai sana: ").split()
        luo_lause(data, lause)
