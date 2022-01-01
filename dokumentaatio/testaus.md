# Testausdokumentti

## Testauksen suorittaminen
Yksikkötestit voi ajaa käskyllä `invoke test` </br>
Kattavuusraportin saa käskyllä `invoke coverage`. 
Käsky luo raportin kansioon htmlcov, josta sen saa auki avaamalla index.html selaimessa.<br>
Käskyllä `invoke lint` voi suorittaa koodinlaatuanalyysin.

## Yksikkötestaus
Jokaiselle kooditiedostolle on oma yksikkötestitiedosto, joka sisältää siihen liittyvän yksikkötestit. Kaikki toiminnallisuus on mahdollisuuksien mukaan pyritty testaamaan. </br>
Ohjelman toimintaa yksikkötestataan myös niin, että yhden luokan testit kattavat usein myös muiden luokkien tai tiedostojen käyttöä niiden välisten riippuvuuksien kautta. Tekstin generointia on testattu niin, että on yksikkötesteissä varmistetaan, että sanat löytyvät oikeasta kohdasta Trietä, ja että niitä käytetään tekstin muodostuksessa. Lisäksi on testattu, että luotujen tekstien sanayhdistelmät löytyvät alkuperäistekstistä. Dictionary-toteutuksen testaus on kevyempää, koska se ei ole ohjelman päätarkoitus, vaan lähinnä mukana vertailusyistä.

## Manuaalinen testaus
Kaikkia ohjelman toimintoja on testattu erilaisilla ja kokoisilla datalähteillä ja syötteillä myös manuaalisesti. Lisäksi Tehokkuus on testattu käyttämällä ohjelmaan sisäänrakennettua testitoiminnallisuutta.

## Tehokkuuden testaaminen
Ohjelman suorituksessa yksi mahdollinen käsky on 'test'. Se ajaa normaalin toiminnan sijaan hakuja silmukassa ja raportoi kuinka kauan rakenteiden luominen ja hakujen tekeminen kesti sekä dictionary-, että trie-rakenteille. Hakujen määrän voi asettaa konfiguraatiossa vaihtamalla muuttujan 'hakuja' arvoa. Tehokkuuden osalta tein vertailun trien ja dictionaryn välillä ja testasin myös ketjun asteen vaikutusta tehokkuuteen. Nämä kaksi testisarjaa on tehty eri aikoihin eri tietokoneilla, joten ne eivät ole keskenään täysin vertailukelpoisia.

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
<th> sarja (tekstin pituus / data)</th>	<th> latausaika (s) - Trie </th> <th> latausaika (s) - Dictionary </th> <th>hakuaika (s/100k hakua) - Trie </th> <th>hakuaika (s/100k hakua) - Dictionary</th>
</tr>
<tr> <td>10 / pieni</td>	<td>0.21</td>	<td>0.11</td>	<td>3.38</td>	<td>2.12</td> </tr>
<tr> <td>50 / pieni</td>	<td>0.21</td>	<td>0.11</td>	<td>6.27</td>	<td>3.07</td> </tr>
<tr> <td>10 / keskikokoinen</td>	<td>2.21</td>	<td>1.11</td>	<td>6.62</td>	<td>7.01</td> </tr>
<tr> <td>50 / keskikokoinen</td>	<td>2.21</td>	<td>1.11</td>	<td>9.78</td>	<td>7.93</td> </tr>
<tr> <td>10 / suuri</td>	<td>7.38</td>	<td>4.29</td>	<td>9.06</td>	<td>11.17</td> </tr>
<tr> <td>50 / suuri</td>	<td>7.38</td>	<td>4.29</td>	<td>14.39</td>	<td>13.39</td> </tr>
</table>

### Ketjun asteen vaikutuksen testaus
Testauksessa on käytetty ohjelman test-komentoa aikojen mittaamiseen. Tekstin maksimipituudeksi on valittu 5, jotta ketjun asteen muuttuminen vaikuttaisi mahdollisimman vähän generoidun tekstin pituuteen ja sitä kautta suoritusaikaan. Taulukon tulosarvo on kolmen testikerran mediaani.
![Suorituskykyvertailu - latausajat](https://github.com/MyVeli/tiralabra/blob/master/dokumentaatio/kuvat/suorituskyky_aste_latausajat.png)
![Suorituskykyvertailu - hakuajat](https://github.com/MyVeli/tiralabra/blob/master/dokumentaatio/kuvat/suorituskyky_aste_hakuajat.png)
<table>
<tr>
<th> sarja (tekstin pituus / data)</th>	<th> latausaika (s) </th> <th>hakuaika (s/100k hakua)</th></tr>
<tr> <td>1 / pieni</td>	<td>0.087</td>	<td>1.88</td>	</tr>
<tr> <td>3 / pieni</td>	<td>0.26</td>	<td>1.62</td>	</tr>
<tr> <td>5 / pieni</td>	<td>0.43</td>	<td>1.53</td>	</tr>
<tr> <td>1 / keskikokoinen</td>	<td>0.85</td>	<td>7.80</td>	</tr>
<tr> <td>3 / keskikokoinen</td>	<td>2.73</td>	<td>4.36</td>	</tr>
<tr> <td>5 / keskikokoinen</td>	<td>4.49</td>	<td>3.27</td>	</tr>
<tr> <td>1 / suuri</td>	<td>3.24</td>	<td>10.20</td>	</tr>
<tr> <td>3 / suuri</td>	<td>8.79</td>	<td>5.57</td>	</tr>
<tr> <td>5 / suuri</td>	<td>14.74</td>	<td>4.32</td>	</tr>
</table>

Enemmän analyysiä tuloksista löytyy toteutusdokumentista.

## Testikattavuus
![Testikattavuus](https://github.com/MyVeli/tiralabra/blob/master/dokumentaatio/kuvat/testikattavuus.PNG)
Kokonaiskattavuutta tiputtaa hieman tiedostonlukemisen testaaminen, koska poikkeuksille ei ole siellä testausta, vaan ne on testattu manuaalisesti.
