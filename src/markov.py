"""Luo lauseen annetun lauseen tai sanan perusteella
"""

import konfiguraatio

def luo_lause(data, lause):
    """Luo lauseen käyttämällä SanaRakenne-luokan metodeja

    Args:
        data (dictionary): sisältää sanaparit ja SanaRakenne luokat
        lause (string): lause, josta aloitetaan ketjun muodostaminen
    """
    i = 0
    if not lause:
        return ""
    sana2 = lause[-1].lower()
    sana1 = None
    if len(lause) > 1:
        sana1 = lause[len(lause)-1].lower()
    while i < konfiguraatio.MAX_PITUUS:
        try:
            if sana1:
                seuraava = data[(sana1, sana2)].anna_sana()
            else:
                seuraava = data[sana2].anna_sana()
        except KeyError:
            break
        except Exception as ex:
            print("virhe: " + ex)
            break
        if not seuraava:
            break
        sana1 = sana2
        sana2 = seuraava
        lause.append(seuraava)
        i += 1
    return' '.join(lause)

def luo_lause_trie(juuri, lause):
    """Luo lauseen trie-rakenteesta pohjalta käyttämällä SanaRakenne-luokan metodia

    Args:
        juuri (TrieNode): Sisältää käytettävän datan
        lause (string): Sisältää lauseen, jonka pohjalta lause kasataan

    Returns:
        string: Markovin ketjulla luotu lause
    """
    i = 0
    if not lause:
        return ""

    while i < konfiguraatio.MAX_PITUUS:
        try:
            if len(lause) <= konfiguraatio.ASTE:
                seuraava = juuri.anna_sana(" ".join(lause[:]))
            else:
                #print(" ".join(lause[(len(lause)-konfiguraatio.ASTE):]))
                seuraava = juuri.anna_sana(" ".join(lause[(len(lause)-konfiguraatio.ASTE):]))
        except KeyError:
            break
        except Exception as ex:
            print(ex)
            break
        lause.append(seuraava)
        i += 1
    return ' '.join(lause)
