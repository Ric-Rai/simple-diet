## Tietokanta

Tietokannassa on viisi taulua, joista jokaisella on uniikki id -tunniste. Kaikki taulut ovat normaalimuodossa.e

### Käyttäjät

Account -niminen taulu sisältää käyttäjien tiedot.

###  Ruoat

Food -tauluun on tallennettu kaikki ruoat makroravinnetietoineen. Lisäksi ruokiin liittyy käyttäjä, joka on ruoan järjestelmään syöttänyt. Ruoan account_id voi olla myös null, jos ruoka ns. yleinen ruoka järjestelmässä. Yleistä ruokaa voi käyttää osana ruokavaliota, mutta käyttäjillä ei ole oikeuksia niiden muokkaamiseen.

### Ruokavaliot

Diet -taulu sisältää ruokavalion nimen, sekä tiedon käyttäjästä, jolle se kuuluu. Lisäksi Ruokavaliossa on aikaleima, joka kertoo, milloin sitä on viimeksi muokattu.

### Ateriat

Meal -taulussa on kaikki ateriat. Jokaisesta ateriasta tallennetaan tieto ruokavaliosta, johon se kuuluu, sekä sen järjestys ruokavaliossa.

### Aterioiden ruoat

MealFood -taulu on liitostaulu, joka liittää ateriat ja ruoat yhteen. Taulu toteutettiin niin, että se mahdollistaa myös Food-taululle tuntemattomien ruokien lisäämisen. Tällöin ateriaan voi vapaasti lisätä ruokien nimiä ja määriä, ja käydä vasta myöhemmin lisäämässä ne Food-tauluun. Jokaisesta ruoasta tallennetaan myös sen määrä ateriassa, sekä sen järjestys listauksessa.

 <br>

## Tietokantakaavio
![Database](db-diagram.png)

<br>

## Create table -lauseet

### Account
<pre><code>CREATE TABLE Account (
    id SERIAL,
    name VARCHAR(100),
    email VARCHAR(100),
    username VARCHAR (60),
    password VARCHAR(60),
    PRIMARY KEY (id)
);
</code></pre>

### Food

<pre><code>CREATE TABLE Food (
    id SERIAL,
    account_id INTEGER,
    name VARCHAR(100),
    energy INTEGER,
    protein NUMERIC,
    carb NUMERIC,
    fat NUMERIC,
    PRIMARY KEY (id),
    FOREIGN KEY (account_id) REFERENCES Account(id)
);
</code></pre>

### Diet

<pre><code>CREATE TABLE Diet (
    id SERIAL,
    account_id INTEGER,
    name VARCHAR(100),
    edited DATE,
    PRIMARY KEY (id),
    FOREIGN KEY (account_id) REFERENCES Account(id)
);
</code></pre>

### Meal

<pre><code>CREATE TABLE Meal (
    id SERIAL,
    diet_id INTEGER,
    order_num INTEGER,
    PRIMARY KEY (id),
    FOREIGN KEY (diet_id) REFERENCES Diet(id)
);
</code></pre>

### MealFood

<pre><code>CREATE TABLE MealFood (
    id SERIAL,
    meal_id INTEGER,
    food_id INTEGER,
    food_name VARCHAR(100),
    amount INTEGER,
    order_num INTEGER,
    PRIMARY KEY (id),
    FOREIGN KEY (meal_id) REFERENCES Meal(id),
    FOREIGN KEY (food_id) REFERENCES Food(id)
);
</code></pre>