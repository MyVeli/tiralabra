"""Luo lauseen annetun lauseen tai sanan perusteella
"""

def luo_lause_dict(data, lause, konfiguraatio):
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
    while i < konfiguraatio.max_pituus:
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

def luo_lause_trie(juuri, lause, konfiguraatio, tiedosto="Any"):
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

    while i < konfiguraatio.max_pituus:
        try:
            if len(lause) <= konfiguraatio.aste:
                seuraava = juuri.anna_sana(lause, tiedosto)
            else:
                #print(" ".join(lause[(len(lause)-konfiguraatio.ASTE):]))
                seuraava = juuri.anna_sana(lause[(len(lause)-konfiguraatio.aste):], tiedosto)
        except KeyError:
            break
        except Exception as ex:
            print(ex)
            break
        lause.append(seuraava)
        i += 1
    return ' '.join(lause)
