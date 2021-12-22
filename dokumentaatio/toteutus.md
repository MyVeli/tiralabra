# Toteutusdokumentti

## Yleisrakenne
Ohjelma koostuu seuraavista tiedostoista:
* main.py
* markov.py
* sanarakenne.py
* tiedostonkäsittely.py
* tiedostonkäsittely_text.py
* trie.py
* ui_komennot.py
* konfiguraatio.py
Ohjelman suoritus alkaa mainista. Main kutsuu konfiguraation määrittely mukaan oikeaa tiedostonkäsittelymetodia. Tiedostonkäsittely avaa tiedoston ja parsii sen sisällön, tallentaen sen trie-rakenteeseen (joskin konfiguraation muutoksella myös puhdasta dictionary toteutusta voi käyttää.) Trien toteutus on trie.py tiedoston TrieNode luokassa, jota tiedostonkäsittely käyttää. TrieNode käyttää seuraavien sanojen tallentamiseen sanarakenne.py tiedoston SanaRakenne luokkaa, joka pitää kirjaa seuraavista sanoista ja niiden esiintymisestä, sekä pystyy arpomaan seuraavan sanan, jolla jatkaa ketjua. Tiedostonkäsittely palauttaa mainille Trien juuren. Main pyytää tämän jälkeen käyttäjältä silmukassa sanoja tai lauseita joita jatkaa. Ketjun luomiseen se käyttää markov.py tiedostosta löytyvää luo_lause metodia. luo_lause käyttää SanaRakenne luokan metodia seuraavien sanojen valitsemiseen. Se muodostaa näistä ketjun, joka on enintään konfiguraatiossa määritellyn mittainen ja palauttaa lopputuloksen mainille joka tulostaa sen komentoriville.

### Trie-rakenne
![Trie-rakenne](https://github.com/MyVeli/tiralabra/blob/master/dokumentaatio/kuvat/trie.png)

## Saavutetut aika- ja tilavaativuudet
Ohjelma on toteutettu Trie-rakenteella, jossa jokaisessa solmussa on yksi kirjain. Puun syvyys riippuu käytetystä Markovin ketjun asteesta, jonka pystyy määrittämään konfiguraatiossa. Triessä olevien sanojen päässä on sanarakenne-luokan olio, jossa on tallennettuna seuraavat mahdolliset sanat ja niiden esiintymiskerrat pythonin dictionary-rakenteeseen. Triessä seuraavat mahdolliset kirjaimet on myös tallennettu dictionary-rakenteisiin. Triestä sanan tai lauseen hakeminen riippuu etsittävän merkkijonon pituudesta, jolloin aikavaativuus on o(n), missä n on merkkijonon pituus.

ToDo: pseudokoodista tilavaativuudet
ToDo: aikavaativuuksien mittaus suorittamalla ohjelmaa erikokoisilla syötteillä

## Puutteet, parannusehdotukset

## Lähteet
Seuraavia lähteitä on tässä vaiheessa käytetty tutkimaan Trie rakenteita:
* [towardsdatascience: implementing trie](https://towardsdatascience.com/implementing-a-trie-data-structure-in-python-in-less-than-100-lines-of-code-a877ea23c1a1)
* [wikipedia](https://en.wikipedia.org/wiki/Trie)
* [medium: trie from theory to practice](https://medium.com/@makhmud.islamov/trie-from-theory-to-practice-ab070d6b539c)
 </br>
 
Markov:
* [towardsdatascience: simulating text with Markov chains](https://towardsdatascience.com/simulating-text-with-markov-chains-in-python-1a27e6d13fc6)
* [wikipedia](https://en.wikipedia.org/wiki/Markov_chain)
