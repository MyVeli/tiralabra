# Viikkoraportti 2
## Tehtyä
* Materiaalin hankkiminen telegrammista
* Tiedostonkäsittely
* Dictionary-toteutus sanaparien ja yhteyksien tallentamiseen
* Lauseiden muodostus dictionary datasta
* Koodin siivoaminen pylint avulla
* Koodin kommentointi
* Yksikkötestien alkua

## Opittua
* Erilaisia huonoja puolia siinä, että toteuttaa lauseita generoivan markovin-ketjun dictionarylla:
    * Hankalaa vaihtaa ketjun astetta
    * Aloittamiseen tarvitsee joko useamman dictionaryn tai käyttäjän pitää antaa täsmälleen niin monta sanaa kuin mikä ketjun aste on tai samaan dictionaryyn tarvitsee tallentaa sanat käyttäen eri mittaisia tupleja. Kaikissa näissä on omat hyvät ja huonot puolensa.
* Toisaalta tällainen toteutus oli nopea tehdä, mikä voisi olla joissain käytännön sovelluksissa hyödyllistä
* Markovin ketjun toteuttaminen
* note: importit on hankalaa saada toimimaan testeissä ja tiedostoissa ilman virtuaaliympäristö jne. -> poetry/venv seuraavaksi

## Kysymyksiä, ongelmia
* stokastisten algoritmien testaus

## Seuraavaksi
* trie rakenne
* testaamisen suunnittelu ja toteutus
* poetry tms. hallinta riippuvuuksille ja virtuaaliympäristö

## Tunnit
Tunteja käytin tällä viikolla n. 7
