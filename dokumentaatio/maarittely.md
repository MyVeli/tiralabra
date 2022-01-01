# Määrittelydokumentti

## Ohjelmointikielet
Ohjelma tehdään pythonilla. Vertaisarviointia varten osaan myös C, C++, C# ja Javaa.

## Opinto-ohjelma
Teen kurssia tietojenkäsittelytieteen kandidaatintutkintoa varten.

## Kieli
Työn dokumentaatio ja kommentointi on suomeksi.

## Ongelma
Tekstin muodostaminen telegram-chattien logien perusteella. Tekstin pitäisi olla sellaista, että se tyylillisesti ja asia-sisällöltään kuvaa lähdemateriaaliaan, vaikka muodostetut lauseet eivät vaikuttaisikaan järkeviltä. Lopputulos on siis ohjelma, joka pystyy tekemään (toivottavasti) hauskaa tekstitaidetta chattien perusteella.

Ohjelma pystyy lukemaan teksitiedostoja, jotka sisältävät chat-logeja. Tekstitiedoston lukemisen jälkeen ohjelma pystyy jatkamaan käyttämän antamia lauseita tai sanoja chat-logien perusteella. 

Ohjelmaa on myös helppoa muokata niin, että chat-logien sijaan sille annetaan muuta tekstiä. Tässä tapauksessa muokkausta vaatisi lähinnä tiedostojen käsittely ja parsiminen.

Laajuuden saamiseksi lisäsin ohjelmaan peli-toiminnallisuuden, jossa ohjelma arpoo jostain luetusta tiedostosta materiaalia ja pyytää käyttäjää arvaamaan tiedoston.

## Algoritmit ja tietorakenteet
### Algoritmit
Ohjelma käyttää Markovin-ketjua tekstin muodostamiseen. Markovin ketjua testataan usealla asteella, mutta lopulliseen ohjelmaan jää pienin aste jolla tekstistä tulee mielenkiintoista, jotta pienemmälläkin aineistolla saa generoitua suuren määrän erilaista tekstiä.

Markovin ketju on valittu toteutukseen, koska siihen tallennettujen tilasiirtymien avulla saa generoitua hyvin tekstiä, jonka tyyli on vastaava kuin lähdemateriaalin. Lisäksi se on tehokas tapa tuottaa uusia lauseita suuresta aineistoista.

### Tietorakenteet
Ohjelma käyttää itse toteutettua Trie-rakennetta ketjun tallentamiseen. Tämän lisäksi vertaan Trie-toteutusta pythonin dictionary-toteutukseen. Teen ensimmäisen toteutuksen myös dictionarylla, jonka jälkeen korvaan sen omalla Trie-toteutuksella. Dictionaryyn tallennan sanapareja, sekä niitä seuraavien sanojen esiintymiskertoja. 
</br>
Ohjelma saa käyttäjältä syötteeksi tekstitiedostoja, joiden perusteella tietorakenne muodostetaan. Trie on hyvä rakenne toteutukselle, koska siitä hakeminen on hyvin tehokasta, ja koska siihen pystyy tallentamaan sanojen välisiä suhteita. Dictionarysta hakeminen taas on tehokasta ja siihen pystyy myös hyvin tallentamaan sanapareja, sekä niiden suhteita muihin sanoihin.
<br>
Ohjelma pystyy myös tallentamaan datan niin, että siitä voi generoida tekstiä pelkästään yhdestä tiedostosta, tai kaikkien tiedostojen perusteella käyttämällä vain yhtä trie-rakennetta.

### Aikavaativuus
Markov-ketjun aikavaativuus riippuu käytetyistä tietorakenteista. Lauseen muodostaminen molemmista rakenteista on aikavaativuudelta O(m), jossa m on etsittävän ketjun pituus, mikäli dictionaryssa ei tule päällekäisiä hasheja sanapareille.

### Käyttäminen
Ohjelman käyttöliittymän on tekstipohjainen. Käyttäjä pystyy käyttöliittymän avulla:
* lataamaan ohjelmaan uuden tekstitiedoston, joka lisätään rakenteeseen
* pyytämään ohjelmaa generoimaan satunnaisia lauseita sille annetun materiaalin pohjalta
* pyytämään ohjelmaa generoimaan lauseen, joka alkaa käyttäjän ohjelmalle syötteenä antamasta sanasta tai jatkamaan käyttäjän syötteenä antamaa lausetta

## Lähteitä:
Seuraavia lähteitä on tässä vaiheessa käytetty tutkimaan Trie rakenteita:
* [towardsdatascience: implementing trie](https://towardsdatascience.com/implementing-a-trie-data-structure-in-python-in-less-than-100-lines-of-code-a877ea23c1a1)
* [wikipedia](https://en.wikipedia.org/wiki/Trie)
* [medium: trie from theory to practice](https://medium.com/@makhmud.islamov/trie-from-theory-to-practice-ab070d6b539c)
 </br>
 
Markov:
* [towardsdatascience: simulating text with Markov chains](https://towardsdatascience.com/simulating-text-with-markov-chains-in-python-1a27e6d13fc6)
* [wikipedia](https://en.wikipedia.org/wiki/Markov_chain)

