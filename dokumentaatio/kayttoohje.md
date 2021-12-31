# Kayttöohje
## Asentaminen
Ohjelma käyttää riippuvuuksien hallintaan poetrya, jonka voi asentaa käskyllä `pip install poetry`. Tämän jälkeen riippuvuudet voi asentaa käskyllä `poetry install`. Tämän jälkeen invoken käyttäminen vaatii joko `poetry run invoke <komento>` käyttämistä tai `poetry shell` komennon käyttämistä. Käskyt tulee ajaa projektin juuressa.

## Testien ajaminen
Yksikkötestit voi ajaa komennolla `invoke test` projektin juuressa. Testikattavuuden taas saa komennolla `invoke coverage`, joka myös luo sivun index.html kansioon htmlcov. Lisäksi `invoke lint` ajaa pylint toiminnon src kansioon.

## Käynnistäminen
Ohjelman voi avata joko komennolla `python src/python.py` tai `invoke start` projektin juuresta.

## Komennot ohjelman sisällä
Ohjelmassa on 5 eri komentoa, joiden kuvaukset alla.

### Konfiguraatio
Mahdollistaa konfiguraation muuttamisen. Muutettavia arvoja ovat tietorakenteeseen ja datan lataamiseen liittyvät arvo, muodostetun tekstin maksimipituus ja Markovin-ketjun aste. Konfiguraation muuttamisen jälkeen data ladataan uudestaan.

### Lataa
Lataa datan konfiguraation mukaan. 
* Konfiguraation arvolla "DICT" lataa kansion data/telegram sisältämät tiedostot dictionary rakenteeseen
* Konfiguraation arvolla "TEXT" lataa data/text kansion sisältämät tiedostot trie-rakenteeseen
* Konfiguraation arvolla "TELEGRAM" lataa data/text kansion sisältämät tiedostot trie-rakenteeseen
* Konfiguraation arvolla "MOLEMMAT" lataa molempien kansioiden sisältämät tiedostot trie-rakenteeseen

#### Datakansio
Lataa käsky lataa tiedostoja datakansiosta. Data/telegram kansion pitää sisältää vain telegram-ohjelmasta exportattuja .json tiedostoja. Data/text kansion taas pitää sisältää vain .txt muotoista tekstiä sisältävää dataa. Uusia tiedostoja voi lisätä vaikka kesken ohjelman ajon ja datan voi ladata uudelle materiaalille lataa käskyllä.

### Test
Lataa datan sekä dictionary, että trie-rakenteisiin, generoi konfiguraatiossa määritellyn (hakuja arvo) määrän tekstejä ja raportoi kuluneet ajat.

### Markov
Generoi tekstiä ladatun datan ja konfiguraation perusteella. Dictionary-toteutus vaatii aloitussanan

### Peli
Generoi tekstiä satunnaisesta tiedostosta ja pyytää pelaajaa arvaamaan mistä tiedostosta sana on. Dictionary-toteutus vaatii aloitussanan.
