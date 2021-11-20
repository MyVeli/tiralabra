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

## Testiraportit
### Tämän hetkinen kattavuus:
![Testikattavuus](https://github.com/MyVeli/tiralabra/blob/master/dokumentaatio/kuvat/testikattavuus.PNG)
