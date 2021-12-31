"""Luo lauseen annetun lauseen tai sanan perusteella
"""

def luo_lause_dict(data, lause, konfiguraatio):
    """Luo lauseen käyttämällä SanaRakenne-luokan metodeja

    Args:
        data (dictionary): sisältää sanaparit ja SanaRakenne luokat
        lause (list): lause, josta aloitetaan ketjun muodostaminen
    """
    i = 0
    # Dictionary toteutus tarvitsee aloitussanan tai lauseen
    if not lause or len(lause) == 0:
        return " "
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
            print(ex)
            return " "
        if not seuraava:
            break
        sana1 = sana2
        sana2 = seuraava
        lause.append(seuraava)
        i += 1
    if len(lause) == 1:
        return lause[0]
    return' '.join(lause)

def luo_lause_trie(juuri, lause, konfiguraatio, tiedosto="Any"):
    """Luo lauseen trie-rakenteesta pohjalta käyttämällä SanaRakenne-luokan metodia

    Args:
        juuri (TrieNode): Sisältää käytettävän datan
        lause (list): Sisältää lauseen, jonka pohjalta lause kasataan

    Returns:
        string: Markovin ketjulla luotu lause
    """

    i = 0
    while i < konfiguraatio.max_pituus:
        try:
            if len(lause) <= konfiguraatio.aste:
                seuraava = juuri.anna_sana(lause, tiedosto)
            else:
                seuraava = juuri.anna_sana(lause[(len(lause)-konfiguraatio.aste):], tiedosto)
        except KeyError:
            break
        except Exception as ex:
            print(ex)
            return " "
        lause.append(seuraava)
        i += 1
    if len(lause) == 1:
        return lause[0]
    return ' '.join(lause)
