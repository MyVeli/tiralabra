# Testausdokumentti

## Testauksen suorittaminen
Yksikkötestit voi ajaa käskyllä `invoke test` </br>
Kattavuusraportin saa käskyllä `invoke coverage`. 
Käsky luo raportin kansioon htmlcov, josta sen saa auki avaamalla index.html selaimessa.

## Yksikkötestaus
Jokaiselle kooditiedostolle on oma yksikkötestitiedosto, joka sisältää siihen liittyvän yksikkötestit. Kaikki toiminnallisuus on mahdollisuuksien mukaan pyritty testaamaan. </br>
Ohjelman toimintaa yksikkötestataan lisäämällä trie-rakenteeseen yksinkertainen aineisto, ja hakemalla sanaa suuri määrä kertoja. Tämän jälkeen jakaumaa verrataan siihen, mikä sen pitäisi olla. Tässä huonona puolena on, että satunnaisuuden takia testillä on pieni mahdollisuus epäonnistua, vaikka toiminnallisuus olisi kunnossa.

## Tehokkuuden testaaminen
Ohjelman suorituksessa yksi mahdollinen käsky on 'test'. Se ajaa normaalin toiminnan sijaan hakuja silmukassa ja raportoi kuinka kauan rakenteiden luominen ja hakujen tekeminen kesti sekä dictionary-, että trie-rakenteille. Hakujen määrän voi asettaa konfiguraatiossa vaihtamalla muuttujan 'hakuja' arvoa. 

### Datasetit
Pieni: [tiralabra.json](https://github.com/MyVeli/tiralabra/blob/master/src/data/telegram/tiralabra.json) tiedoston sisältö. Tiedosto sisältää 23 851 riviä telegram-logeja tiralabra-kanavalta.
<br>
Keskikokoinen: pienen datasetin sisältö + [tkoaly.json](https://github.com/MyVeli/tiralabra/blob/master/src/data/telegram/tkoaly.json). tkoaly.json sisältää 168 058 riviä telegram-logeja tkoaly-kanavalta.
<br>
Suuri: keskikokoisen datasetin sisältö + [tira.json](https://github.com/MyVeli/tiralabra/blob/master/src/data/telegram/tira.json). tira.json sisältää 476 923 riviä telegram-logeja tira-kanavalta.
<br>

### Trien ja dictionaryn vertailu
Ohjelmasta vertailun vuoksi löytyvä dictionary on rakennettu niin, että se tukee vain 2. asteen Markovin-ketjuja ja lataa vain telegram-tiedostossa olevan datan. Tämän vuoksi alla oleva vertailu tietorakenteiden välillä on tehty niin, että trien konfiguraatioksi on asetettu 'telegram' ja ketjun asteeksi 2.
<br><br>
Alla olevissa testeissä sarja-kenttä sisältää tiedon tekstin maksimipituudesta ja koulutusdatan koosta. Esim. 10 / pieni on sarja, jossa tekstin maksimipituus on 10 ja datasetti on pieni. Datasettien kuvaukset yllä.
<br><br>
![Suorituskykyvertailu](https://github.com/MyVeli/tiralabra/blob/master/dokumentaatio/kuvat/suorituskyky_trie_ja_dictionary.png)
<table>
<tr>
<th> sarja (tekstin pituus / data)</th>	<th> latausaika (s) - Trie </th> <th> latausaika (s) - Dictionary </th> <th>hakuaika (s/10k hakua) - Trie </th> <th>hakuaika (s/10k hakua) - Dictionary</th>
</tr>
<tr> <td>10 / pieni</td>	<td>0.21</td>	<td>0.11</td>	<td>3.38</td>	<td>2.12</td> </tr>
<tr> <td>50 / pieni</td>	<td>0.21</td>	<td>0.11</td>	<td>6.27</td>	<td>3.07</td> </tr>
<tr> <td>10 / keskikokoinen</td>	<td>2.21</td>	<td>1.11</td>	<td>6.62</td>	<td>7.01</td> </tr>
<tr> <td>50 / keskikokoinen</td>	<td>2.21</td>	<td>1.11</td>	<td>9.78</td>	<td>7.93</td> </tr>
<tr> <td>10 / suuri</td>	<td>7.38</td>	<td>4.29</td>	<td>9.06</td>	<td>11.17</td> </tr>
<tr> <td>50 / suuri</td>	<td>7.38</td>	<td>4.29</td>	<td>14.39</td>	<td>13.39</td> </tr>
</table>


## Testiraportit
![Testikattavuus](https://github.com/MyVeli/tiralabra/blob/master/dokumentaatio/kuvat/testikattavuus.PNG)
