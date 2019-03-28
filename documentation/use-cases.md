# Käyttötapaukset

#### Käyttöliittymästä yleisesti

Käyttöliittymän komponentit on järkevää toteuttaa taulukkomuotoisesti, sillä se on sovelluksen käsittelemille tiedoille luontainen esitystapa. Jotta vältytään jatkuvalta sivujen päivittämiseltä, niin lomakkeet lähetetään javascriptillä. Palvelin vastaa yksikertaisella tekstillä tai HTML:llä, jonka perusteella sivua päivitetään. Siispä sovelluksen nimen mukaisesti myös toimintojen suorittaminen pyritään pitämään mahdollisimman yksinkertaisena.

<br>

#### Käyttäjä haluaa tehdä tehdä ruokavalion

- Käyttäjä rekisteröityy sovellukseen ja koostaa itselleen ruokavalion aterioista. Käyttäjä muodostaa aterian valitsemalla siihen perusruoka-aineita valmiista listasta, sekä antamalla ruokien määrät ateriassa.

```diff
+ Rekisteröinti ja kirjautuminen on toteutettu
- Päänäkymä ruokavalion luomiselle puuttuu
- Ruokien valitseminen listasta on haastavaa toteuttaa käyttäjäystävällisesti. Toimivaa voisi olla käyttää jonkinlaista autocomplete-ominaisuutta ruoan nimeä kirjoitettaessa.
- Sovellukselle pitäisi pystyä antamaan tiedosto, jonka sisältämistä riveistä ruokataulukkoon luodaan valmiit "perusruoka-aineet".
```

<br>

#### Käyttäjä haluaa perustietoa ruokavalion koostumuksesta

- Käyttäjä näkee makroravinnekoostumuksen ja energiamäärän reaaliajassa koostaessaan ruokavaliota.

```diff
- Todo: Joka kerta kun ateriaan lisätään ruoka ja määrää, niin ne lähetetään palvelimelle tallennettavaksi. Palvelin vastaa lähettämällä tiedon muuttuneista makroravinne- ja energiamääristä.
```

<br>

#### Käyttäjä haluaa käyttää mitä tahansa ruoka-ainetta ruokavaliossaan tai muokata ruoka-aineen tietoja

- Käyttäjä syöttää haluamansa ruoan nimen ja ravintoainekoostumuksen ruoka-ainetaulukkoon, minkä jälkeen sitä voidaan käyttää ruokavalion osana. Käyttäjä voi myös muokata minkä tahansa ruoan nimeä tai ravintoainekoostumusta, sekä halutessaan poistaa ruoan taulukosta.

```diff
+ Ruoka-aineille on toteutettu täysi CRUD-toiminnallisuus
- Ruokataulukon tulee olla käyttäjäkohtainen
- Ruokia tulisi voida etsiä nimen perusteella
```

<br>

#### Käyttäjä haluaa muuttaa aterioiden tai ruokien järjestystä ruokavaliossa

- Käyttäjä pystyy helposti yksinkertaisella ja intuitiivisellä tavalla muuttamaan näiden järjetystä.

```diff
- Jonkinlaiset ylös- ja alaspäin osoittavat nuolet, joita klikkaamalla ateria tai aterian sisältämä ruoka siirtyy taulukossa ylöspäin. Samalla palvelimelle lähetetään tieto muuttuneesta järjestyksestä. Tehokkainta olisi käyttää jotain näppäinyhdistelmää esim. <shift>+<up>/<down>. Tämä vaatisi kuitenkin mahdollisuuden valita rivejä taulukosta. 
```

<br>

#### Käyttäjä haluaa käyttää aterian osana reseptillä valmistettua ruokaa tai muuta useammasta ruoka-aineesta koostuvaa ruokaa

- Käyttäjä syöttää reseptitaulukkoon reseptin nimen ja sen sisältämät ruoka-aineet ja niiden määrät reseptissä. Reseptinä tallennettua ruokaa voidaan käyttää osana ruokavaliota, kuten mitä tahansa muuta ruoka-ainetaulukon ruokaa.

 ```diff
- Tämä on edityneempi ominaisuus, jonka toteuttamisessa on joitain haasteita. Jotta sovelluksen logiikka pysyy mahdollisimman yksinkertaisena, niin reseptille tulee laskea normaali ravintoainekoostumus 100 g kohden, ja tallentaa se ruoka-ainetaulukkoon, jossa se käyttäytyy kuten normaali ruoka. Eli ruokataulukon ja reseptitaulukon välille syntyy riippuvuus siten, että aina kun reseptitaulukkoa muutetaan, niin myös ruokataulukkoa muutetaan. Tämä tietysti myös denormalisoi tietokantaa. 
```

