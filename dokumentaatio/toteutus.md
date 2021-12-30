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

Ohjelman suoritus alkaa main.py tiedostosta. Suorituksen alussa luodaan konfiguraatio-olio käyttäen sen default arvoja. Konfiguraatio on omassa luokassaan konfiguraatio.py tiedostossa. Main sisältää silmukan, jossa käyttäjältä pyydetään komentoja. Ohjelman suoritus loppuu, kun käyttäjä antaa tyhjän syötteen. Main kutsuu käyttäjän syötteen mukaan oikeaa ui_komennot.py tiedoston funktiota.

`Lataa-komento` kutsuu ui_komennot.py tiedoston lataa-funktiota. Funktio tarkistaa ensin konfiguraatiosta mihin rakenteeseen ja mitkä tiedostot ladataan. Sen jälkeen se kutsuu tiedostonkasittely.py tiedostosta konfiguraation mukaista funktiota. Tiedostonkasittely käy kaikki data/telegram ja/tai data/text kansioissa olevat tiedostot läpi ja tallentaa ne trie- tai dictionary-rakenteeseen. Trietä käytettäessä, sanat tallennetaan käyttäen trie.py tiedoston TrieNode-luokkaa. Luokka tallentaa seuraavat sanat dictionaryyn ja SanaRakenne-luokkaan. SanaRakenne luokka ylläpitää myös tietoa siitä, kuinka monta kertaa jokin sana on esiintynyt. Näiden toiminnasta tarkemmin myöhemmissä kappaleissa. Kun kaikki data on ladattu, ui_kommennot palauttaa mainille datan.

Dataa voi käyttää kolmella eri komennolla, jotka kaikki ohjautuvat ui_komennot.py tiedostossa eri funktioihin. Kaikki niistä käyttävät markov.py tiedoston lauseen generointia tekstin luomiseen. Funktiot generoivat tekstiä kunnes konfiguraatiossa oleva maksimipituus tulee täyteen tai seuraavaa jatkavaa sanaa ei löydy. Seuraava sana löytyy ensin etsimällä trie-rakenteesta oikea haara, jonka päässä oleva SanaRakenne arpoo seuraavan sanan jatkamaan tekstiä. Rakenteista ja algoritmeista enemmän alla.

### Trie-rakenne
Trie on rakennettu niin, että sen maksimisyvyys on ketjun aste. Jokainen node sisältää kaksi merkittävää osaa:
1. seuraavat mahdolliset sanat dictionaryssa, jossa avaimena on sana ja arvona seuraava TrieNode
2. SanaRakenne-luokan jokaista luettua datatiedostoa kohden
Näistä ensimmäistä käytetään Trie-rakenteessa liikkumiseen ja toista seuraavan sanan arpomiseen. Rakenteen periaate on kuvattuna alla olevassa kuvassa.
![Trie-rakenne](https://github.com/MyVeli/tiralabra/blob/master/dokumentaatio/kuvat/trie.png)
<br>
Luodun rakenteen heikkoutena on datan toisteellisuus ja sen kautta rakenteen käyttämä muisti. Kaikki seuraavat sanat löytyvät sekä ensimmäisestä, että toisesta osasta. Tämä on kuitenkin tietoinen kompromissi nopeuden ja toiminnallisuuden suhteen. Nyt trie-rakenteesta pystyy luomaan nopeasti tekstiä sekä kaikista datalähteistä, että vain yhdestä. Halusin ohjelmaan molemmat vaihtoehdot sen sisältämää peliä ja normaalia tekstin generointia varten.

### Tekstin generointi trie-rakenteen avulla
Teksti generoidaan Markovin-ketjujen avulla. 

## Saavutetut aika- ja tilavaativuudet

### Analyysi pseudokoodin perusteella
Analyysia varten n=sanojen määrä, m=ketjun aste ja k=tiedostojen määrä

#### Datan lataaminen rakenteeseen

`juuri = TrieNode()` <br>
`for i=0; i < sanoja tekstissä; i++:`<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
`for j=0; j < ketjun_aste; j++:`<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
`juuri.lisaa(teksti[i:i+j],teksti[i+j], tiedostonimi)` 
<br>
Datan lisäämisessä on siis kaksi silmukkaa, joista ensimmäinen käy läpi tekstin kaikki sanat, jolloin sen aikavaativuus on O(n) * silmukan sisällön aikavaativuus. Sisällä oleva silmukka taas on O(m) * juuri.lisaa funktion aikavaativuus. Tässä vaiheessa lisääminen on siis O(nm) * juuri.lisaa aikavaativuus. Tutkitaan seuraavaksi sitä.<br><br>
TrieNoden toteutuksesta:<br>
`def init(self, sanat=None, tiedostonimi=None):`<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
`self.seuraavat_sanat = new dictionary()` <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
`self.yhteydet = new dictionary()` <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
`self.yhteydet_koko = 0` <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
`if size(sanat) != 0:` <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
`self.lisaa(sanat, tiedostonimi)`
<br> <br>
`def lisaa(teksti, lisattava_sana, tiedostonimi):` <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
`if size(teksti) == 0:`<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
`if tiedostonimi not in self.yhteydet:` <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
`self.yhteydet[tiedostonimi]= new SanaRakenne(lisattava_sava)`<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
`else`:<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
`self.yhteydet[tiedostonimi]=SanaRakenne.lisaa(lisattava_sana)`<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
`else if teksti[0] in self.seuraavat_sanat:`<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
`self.seuraavat_sanat[teksti[0]].lisaa(teksti[1:],lisattava_sana,tiedosto_nimi)`<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
`else:`<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
`self.seuraavat_sanat[teksti[0]] = new TrieNode(teksti[1:],lisattava_sana,tiedosto_nimi)`
<br>
<br>
TrieNode käyttää siis kahta dictionarya, joista toisessa avaimina on tiedostojen nimet ja toisessa seuraavat sanat. Pythonin dictionaryn pahimman tapauksen aikavaativuus lisäämiselle on O(n) ja avaimen olemassaolon tarkistamiselle O(n). Keskiarvoinen on molemmille O(1). Tämän takia toteutuksen keskimääräinen ja pahin tapaus eroavat toisistaan huomattavasti. <br><br>
Luokan lisaa-metodi on rekursiivinen ja tapahtuu maksimissaan ketjun asteen verran. Rekursiivisesti tapahtuvan osan sisällä on yksi dictionaryn avaimen tarkastus tiedostoja avaimena sisältävästä dictionarysta, jonka pahin tapaus on siis O(k) ja keskiarvoinen O(1), ja joko uuden TrieNoden luominen tai dictionarysta haku. Molempien keskiarvoinen tapaus on O(1) ja haun huonoin tapaus on O(n). Tämän jälkeen ketjun viimeisessä vaiheessa tarkistetaan kerran dictionary jonka avaimina on tiedostojen nimiä ja sen jälkeen joko haetaan SanaRakenne-olio dictionarysta tai lisätään uusi sellainen. Nämä tapahtuvat sisäkkäin, joten pahin tapaus on O(n^2) * SanaRakenne-olion lisaa-metodin aikavaativuus ja keskimääräinen O(1) * SanaRakenne-olion lisaa-metodin aikavaativuus.<br><br>

SanaRakenne luokka on melko yksinkertainen, mutta se sisältää myöskin dictionaryn, jossa avaimena on sanoja ja arvoina niiden esiintymiskertoja. Myös siinä tarkistetaan ensin avaimen löytyminen, minkä jälkeen joko lisätään avain tai muutetaan arvon suuruutta. Näissäkin keskimääräinen tapaus on O(1) ja pahin O(n), eli sisäkkäisinä O(1) ja O(n^2). <br><br>
TrieNoden rekursiivisen osan pahin tapaus on siis O(mn^2) ja kerran tapahtuvan osuuden O(k^2 * n^2). Rekursiivisen osan keskimääräinen tapaus taas on O(m) ja kerran tapahtuvan osuuden O(1).
Kokonaisuutena TrieNoden lisaa-metodista siis tulee pahimmaksi tapaukseksi O(k^2 * n^2) ja keskimääräiseksi tapaukseksi O(m) rekursiosta johtuen. Tällöin lisäämisen aikavaativuus on pahimassa tapauksessa O(k^2 * n^3 * m) ja keskiarvoinen tapaus O(nm^2).
<br><br>

#### Tekstin generointi
Käytetään analyysiä varten merkintöjä n = sanojen määrä triessä, m = Markovin-ketjun aste, k = tiedostojen määrä ja l = generoitavan lauseen pituus. <br>
Tekstin generointi tapahtuu markov.py tiedoston luo_lause_trie funktiolla. Tässä sen aikavaativuuteen liittyvä pseudokoodiesitys:<br>
`i = 0`<br>
`lause = "max ketjun mittainen lause parametrina"`<br>
`while i < max_pituus`<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
`seuraava = juuri.anna_sana(lause)` #tässä juuri on ensimmäinen TrieNode <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
`i =  i + 1` <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
`lause.append(seuraava)` <br>
`return ' '.join(lause)` <br><br>
Koodissa on siis yksi silmukka, joka tapahtuu l kertaa. Listaan lisääminen on vakioaikaista. Tutkitaan seuraavaksi TrieNoden anna_sana metodia:<br>
`def anna_sana(self, haku, tiedosto='Any'):`<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
`if size(haku) == 0:`<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
`if tiedosto == 'Any':`<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
`satunnaisluku = randint(0,self.yhteydet_koko)`<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
`for i in self.yhteydet.values():`<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
`satunnaisluku = satunnaisluku-i.koko` <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
`if satunnaisluku <=0: return i.anna_sana()`<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
`else:`<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
`return self.yhteydet[tiedosto].anna_sana()`<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
`return self.seuraavat_sanat[haku[0]].anna_sana(haku[1:],tiedosto)`<br>


Funktion viimeinen parametri määrittelee siis haetaanko mistä vain tiedostosta peräisin olevia sanoja, vai voidaanko käyttää vain tietyn tiedoston sanastoa. Molemmissa tapauksissa rekursiolla siirrytään Trien päähän generoimaan seuraavaa sanaa. Tämä tapahtuu m kertaa, jossa m on Markovin-ketjun aste. Koska rekursiokutsussa käytetään dictionarya, on pahimman tapauksen aikavaativuus O(nm) ja keskimääräisen O(m). Rekursion päätteeksi arvotaan seuraava sana. Mikäli haetaan mistä vain tiedostosta, arvotaan ensin käytettävä tiedosto painottaen sanamäärillä. Tämä tapahtuu silmukassa, jossa käydään maksimissaan k kertaa, jossa k on tiedostojen määrä. <br><br>
Viimeinen tärkeä osa on SanaRakenne-luokan anna_sana() -metodi. Alla sen pseudokoodi.<br>
`self.sanat` on dictionary, jonka avaimina on sanoja ja arvoina niiden esiintymiskerrat. `self.koko` kertoo koko dictionaryn arvojen summan.<br>
`def anna_sana(self)`<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
`luku = randint(0, self.koko)` <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
`for sana, maara in self.sanat.items():`<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
`luku = luku - maara` <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
`if luku <= 0: return sana`<br>
Tässä muut operaatiot ovat vakioaikaisia, mutta uuden sanan arpominen on sekä pahimmassa, että keskimääräisessä tapauksessa O(n). Kuitenkin tässä vaiheessa n:n suuruus on ketjun viimeiseen sanaan liittyvien seuraavien sanojan suuruus, minkä takia tämä on käytännössä keskimäärin hyvin nopea operaatio. Pahimmassa tapauksessa kuitenkin kaikki sanat voivat seurata kaikista muista sanoista.<br><br>

Tämän perusteella koko tekstin generoinnin aikavaativuus on siis pahimmassa tapauksessa O(mkln^2) ja keskimääräisessä O(nmkl) kuitenkin niin, että n on sanamäärä, joka keskimäärin löytyy viimeisen TrieNoden päästä.

### Aikavaativuuden testaus


### Tilavaativuus
Sanat tallennetaan jokaiselle ketjun tasolle trie-rakenteeseen kaksi kertaa, kerran trie-rakenteessa liikkumista varten ja kerran SanaRakenne-luokkaan seuraavien sanojen arpomista varten. Sanat tallennetaan siis 2mn kertaa, jossa m=ketjun aste ja n=erilaisten sanojen määrä. Tilavaativuus on siis O(mn).

## Puutteet, parannusehdotukset
* Erikoismerkkien käyttöä varsinkin telegram-tekstin osalta voisi parantaa paljon. Ongelmana merkkien suhteen on se, että telegrammin käyttämä .json tiedosto sisältää erityisesti lainauksien osalta paljon omia merkkejä, joita ei kannata lisätä rakenteeseen, ja niiden erottaminen olisi kohtalaisen työlästä.
* Ilman aloitussanaa ei voi generoida lauseita. Tämän lisääminen olisi kohtalaisen helppoa, mutta se ei ollut tärkeää siihen toiminnallisuuteen jonka halusin tehdä.
* Graafinen käyttöliittymä olisi hauska, mutta ei myöskään tärkeä tämän kurssin asioiden osalta.


## Lähteet
Seuraavia lähteitä on käytetty tutkimaan Trie rakenteita:
* [towardsdatascience: implementing trie](https://towardsdatascience.com/implementing-a-trie-data-structure-in-python-in-less-than-100-lines-of-code-a877ea23c1a1)
* [wikipedia](https://en.wikipedia.org/wiki/Trie)
* [medium: trie from theory to practice](https://medium.com/@makhmud.islamov/trie-from-theory-to-practice-ab070d6b539c)
 </br>
 
Markov:
* [towardsdatascience: simulating text with Markov chains](https://towardsdatascience.com/simulating-text-with-markov-chains-in-python-1a27e6d13fc6)
* [wikipedia](https://en.wikipedia.org/wiki/Markov_chain)

Pythonin aikavaativuudet:
* [python wiki](https://wiki.python.org/moin/TimeComplexity)