# Testausdokumentti

## Testauksen suorittaminen
Yksikkötestit voi ajaa käskyllä `invoke test` </br>
Kattavuusraportin saa käskyllä `invoke coverage`. 
Käsky luo raportin kansioon htmlcov, josta sen saa auki avaamalla index.html selaimessa.

## Yksikkötestaus
Jokaiselle kooditiedostolle on oma yksikkötestitiedosto, joka sisältää siihen liittyvän yksikkötestit. Kaikki toiminnallisuus on mahdollisuuksien mukaan pyritty testaamaan. </br>
Tällä hetkellä ohjelman toimintaa yksikkötestataan lisäämällä trie-rakenteeseen yksinkertainen aineisto, ja hakemalla sanaa suuri määrä kertoja. Tämän jälkeen jakaumaa verrataan siihen, mikä sen pitäisi olla. Tässä huonona puolena on, että satunnaisuuden takia testillä on pieni mahdollisuus epäonnistua, vaikka toiminnallisuus olisi kunnossa.

## Tehokkuuden testaaminen
Tiedostossa src/konfiguraatio.py on enum tyyppinen muuttuja MODE. Vaihtamalla sen arvon arvoksi TEST, ohjelma (src/main.py) ajaa normaalin toiminnan sijaan hakuja silmukassa ja raportoi kuinka kauan rakenteiden luominen ja hakujen tekeminen kesti. Hakujen määrän voi asettaa konfiguraatiossa vaihtamalla muuttujan HAKUJA arvoa.

sarja	latausaika (s)	hakuaika (s/10k hakua)
Trie 10 pieni	0.21	3.38
Trie 50 pieni	0.11	2.12
Trie 10 keskikokoinen	0.21	6.27
Trie 50 keskikokoinen	0.11	3.07
Trie 10 suuri	2.21	7
Trie 50 suuri	1.11	7.01
Dictionary 10 pieni	2.21	9.78
Dictionary 50 pieni	1.11	7.93
Dictionary 10 keskikokoinen	7.38	9.06
Dictionary 50 keskikokoinen	4.29	11.17
Dictionary 10 suuri	7.38	14.39
Dictionary 50 suuri	4.29	13.39

sarja	latausaika (s) - Trie	latausaika (s) - Dictionary	hakuaika (s/10k hakua) - Trie	hakuaika (s/10k hakua) - Dictionary
10 pieni	0.21	0.11	3.38	2.12
50 pieni	0.21	0.11	6.27	3.07
10 keskikokoinen	2.21	1.11	6.62	7.01
50 keskikokoinen	2.21	1.11	9.78	7.93
10 suuri	7.38	4.29	9.06	11.17
50 suuri	7.38	4.29	14.39	13.39


## Testiraportit
### Tämän hetkinen kattavuus:
![Testikattavuus](https://github.com/MyVeli/tiralabra/blob/master/dokumentaatio/kuvat/testikattavuus.PNG)
