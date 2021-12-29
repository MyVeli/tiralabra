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

![Suorituskykyvertailu](https://github.com/MyVeli/tiralabra/blob/master/dokumentaatio/kuvat/suorituskyky_trie_ja_dictionary.png)
<table>
<tr>
<th> sarja </th>	<th> latausaika (s) - Trie </th> <th> latausaika (s) - Dictionary </th> <th>hakuaika (s/10k hakua) - Trie </th> <th>hakuaika (s/10k hakua) - Dictionary</th>
</tr>
<tr> <td>10 / pieni</td>	<td>0.21</td>	<td>0.11</td>	<td>3.38</td>	<td>2.12</td> </tr>
<tr> <td>50 / pieni</td>	<td>0.21</td>	<td>0.11</td>	<td>6.27</td>	<td>3.07</td> </tr>
<tr> <td>10 / keskikokoinen</td>	<td>2.21</td>	<td>1.11</td>	<td>6.62</td>	<td>7.01</td> </tr>
<tr> <td>50 / keskikokoinen</td>	<td>2.21</td>	<td>1.11</td>	<td>9.78</td>	<td>7.93</td> </tr>
<tr> <td>10 / suuri</td>	<td>7.38</td>	<td>4.29</td>	<td>9.06</td>	<td>11.17</td> </tr>
<tr> <td>50 / suuri</td>	<td>7.38</td>	<td>4.29</td>	<td>14.39</td>	<td>13.39</td> </tr>
</table>

## Testiraportit
### Tämän hetkinen kattavuus:
![Testikattavuus](https://github.com/MyVeli/tiralabra/blob/master/dokumentaatio/kuvat/testikattavuus.PNG)
