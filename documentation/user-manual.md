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


## Sovelluksen käynnistäminen

Sovellus käynnistetään juurihakemistosta komennolla

```
export FLASK_APP=application && flask run
```

## Kirjautuminen ja rekisteröityminen

Kirjautuminen onnistuu kirjoittamalla olemassaoleva käyttäjätunnus ja salasana syötekenttään ja painamalla _kirjaudu_.

Rekisteröityminen tapahtuu täyttämällä rekisteröitymislomake.

## Ruokataulukko

Ruokataulukkoon syötetään uusi ruoka painamalla _lisää uusi_ -painiketta. Ruoan tietoja voi muokata painamalla rivin oikeassa päädyssä olevaa _muokkaa_ -painiketta. Ruoan voi poistaa _poista_ -painikkeella.

## Ruokavaliot

Uusi ruokavalio luodaan painamalla _lisää uusi_ -painiketta ja antamalla ruokavaliolle nimi.
