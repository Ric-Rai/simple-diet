# Käyttöohje

Lataa sovellus osoitteesta https://github.com/ric-rai/simple-diet


## Sovelluksen asentaminen

Mene sovelluksen juurihakemistoon ja luo Python-virtuaaliympäristö komennolla

```
python3 -m venv venv
```

Aktivoi virtuaaliympäristö komennolla

```
source venv/bin/activate
```

Asenna riippuvuudet komennolla

```
pip install -r requirements.txt
```

### Sovelluksen käynnistäminen

Sovellus käynnistetään juurihakemistosta komennolla

```
export FLASK_APP=application && flask run
```

### Sovelluksen asentaminen Herokuun

Asenna sovellus ensin paikallisesti ja luo tili Herokuun. Sovellus luodaan Herokuun komennolla:

```
heroku create sovelluksen-nimi
```

<br>

## Sovelluksen käyttö

Sovellusta on testattu tämän ohjeen kirjoittamisen aikaan uusimmmilla Firefox- ja Chrome-selainten versioilla työpöytäresoluutiolla.

### Kirjautuminen ja rekisteröityminen

Kirjautuminen onnistuu kirjoittamalla olemassaoleva käyttäjätunnus ja salasana syötekenttään ja painamalla oikean yläkulman _Kirjaudu_ -painiketta.

Rekisteröityminen tapahtuu painamalla oikean yläkulman _Rekisteröidy_ -painiketta ja täyttämällä rekisteröitymislomake.

### Ruokataulukko

Ruokataulukko avautuu painamalla _Ruokataulukko_ -linkkiä vasemmasta yläkulmasta. Ruokataulukossa on valmiina ns. yleisiä ruoka-aineita, joita voit käyttää normaalisti ruokavalioidesi osana. Et kuitenkaan voi muokata näitä yleisiä ruoka-aineita. Ruoka-aineella tulee olla nimi ja energiamäärä kilokaloreina sataa grammaa kohden, sekä makroravinteet grammoina sataa grammaa kohden.

Ruokataulukkoon syötetään uusi ruoka painamalla taulukon oikean yläkulman yläpuolella olevaa _Lisää uusi_ -painiketta. Ruoan tietoja voi muokata painamalla rivin oikeassa päädyssä olevaa keltaista kynä-ikonia. Voit tallentaa ruoan tiedot painamalla vihreää ikonia, jossa on listan ja plus-merkin kuva. Ruoan voi poistaa painamalla punaista roskakori-ikonia.

Uusien ja muokattujen rivien taustaväri muuttuu vihreäksi.

### Ruokavaliolista

Listaus ruokavalioista avautuu painamalla _Ruokavaliot_ -linkkiä vasemmasta yläkulmasta. Voit luoda uuden ruokavalion painamalla _Lisää uusi_ -painiketta. Anna ruokavaliolle nimi ja paina vihreää ikonia tallentaaksesi uuden ruokavalion.

Voit avata luomasi ruokavalion painamalla sen nimeä.

### Ruokavalionäkymä

Avaa ruokavalio painamalla sen nimeä ruokavaliolistassa. Aloita ruokavalion koostaminen painamalla _Uusi ateria_ -painiketta. Ateria poistetaan _Poista ateria_ -painikkeella.

Ateriaan voit lisätä ruoan painamalla _Lisää ruoka_ -painiketta. Aloita sitten kirjoittamaan haluamasi ruoka-aineen nimeä Ruoka-sarakkeen alla olevaan ensimmäiseen kenttään. Ohjelma ehdottaa sinulle ruokataulukossa olevien ruokien nimiä. Jos ruokaa ei ole vielä lisätty ruokataulukkoon, niin voit siitä huolimatta lisätä sen ruokavalioon ja käydä myöhemmin lisäämässä sen ruokataulukkoon. Ruoan nimen lisäksi tulee ruoalle syöttää sen määrä grammoina ateriassa. Voit poistaa ruoan punaisesta roskakori-ikonista tai muokata sitä keltaisesta kynä-ikonista.

Jokaisen aterian ylimmällä rivillä on lihavoidulla teksillä aterian sisältämät ravintoaineet. Koko ruokavalion sisältämät ravintoaineet näet taulukon ylimmältä riviltä.

### Yhteenveto

Kun olet luonut ruokavalioita itsellesi, niin näet vasemman yläkulman _Yhteenveto_ -linkistä yhteenvetosivun, joka kertoo tietoja syöttämistäsi ruokavalioista ja ruoista.