# Kayttöohje
## Asentaminen
Ohjelma käyttää riippuvuuksien hallintaan poetrya, jonka voi asentaa käskyllä `pip install poetry`. Tämän jälkeen riippuvuudet voi asentaa käskyllä `poetry install`. Tämän jälkeen invoken käyttäminen vaatii joko `poetry run invoke <komento>` käyttämistä tai `poetry shell` komennon käyttämistä. Käskyt tulee ajaa projektin juuressa.

## Testien ajaminen
Yksikkötestit voi ajaa komennolla `invoke test` projektin juuressa. Testikattavuuden taas saa komennolla `invoke coverage`, joka myös luo sivun index.html kansioon htmlcov.

## Käynnistäminen
Ohjelman voi avata joko komennolla `python src/python.py` tai `invoke start` projektin juuresta.

## Komennot ohjelman sisällä
### Konfiguraatio

### Lataa

### Test

### Markov

### Peli
