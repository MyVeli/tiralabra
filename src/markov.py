"""Luo lauseen annetun lauseen tai sanan perusteella
"""
def luo_lause(data, lause):
    """Luo lauseen käyttämällä SanaRakenne-luokan metodeja

    Args:
        data (dictionary): sisältää sanaparit ja SanaRakenne luokat
        lause (string): lause, josta aloitetaan ketjun muodostaminen
    """
    lauseenpituus = 30
    i = 0
    if not lause:
        return
    sana2 = lause[-1].lower()
    sana1 = None
    if len(lause) > 1:
        sana1 = lause[len(lause)-1].lower()
    while i < lauseenpituus:
        try:
            if sana1:
                seuraava = data[(sana1, sana2)].anna_sana()
            else:
                seuraava = data[sana2].anna_sana()
        except KeyError:
            break
        except Exception as ex:
            #print("virhe: " + ex)
            break
        if not seuraava:
            break
        sana1 = sana2
        sana2 = seuraava
        lause.append(seuraava)
        i += 1
    return' '.join(lause)

def luo_lause_trie(juuri, lause):
    lauseenpituus = 30
    i = 0
    ASTE = 2
    if not lause:
        return

    while i < lauseenpituus:
        try:
            if len(lause) < ASTE:
                seuraava = juuri.anna_sana("".join(lause[i:]))
            else:
                seuraava = juuri.anna_sana("".join(lause[i-ASTE+1:]))
        except Exception as e:
            #print(e)
            break
        lause.append(seuraava)
        i += 1
    return ' '.join(lause)
