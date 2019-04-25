# Käyttötapaukset

#### Käyttöliittymästä yleisesti

Käyttöliittymän komponentit on järkevää toteuttaa taulukkomuotoisesti, sillä se on sovelluksen käsittelemille tiedoille luontainen esitystapa. Jotta vältytään jatkuvalta sivujen päivittämiseltä, niin lomakkeet lähetetään javascriptillä. Palvelin vastaa yksikertaisella tekstillä tai HTML:llä, jonka perusteella sivua päivitetään. Siispä sovelluksen nimen mukaisesti myös toimintojen suorittaminen pyritään pitämään mahdollisimman yksinkertaisena.

<br>

#### Käyttäjä haluaa tehdä ruokavalion

- Käyttäjä rekisteröityy sovellukseen ja koostaa itselleen ruokavalion aterioista. Käyttäjä muodostaa aterian valitsemalla siihen perusruoka-aineita valmiista listasta, sekä antamalla ruokien määrät ateriassa.

```diff
+ Rekisteröinti ja kirjautuminen on toteutettu
+ Päänäkymä ruokavalioiden luomiselle on toteutettu
+ Ruokavalioon voi lisätä aterioita ja niitä voi poistaa
+ Aterioihin voi lisätä ruokia ja niitä voi poistaa
```
Ruokien valitseminen listasta on haastavaa toteuttaa käyttäjäystävällisesti. Toimivaa voisi olla käyttää jonkinlaista autocomplete-ominaisuutta ruoan nimeä kirjoitettaessa. Sovellus luo käynnistymisen yhteydessä valmiiksi listan ruoka-aineita.

SQL esimerkki uuden ruokavalion koostamisesta tietokantaan:

<pre><code>INSERT INTO Diet (account_id, name, edited) VALUES (?, ?, ?);
INSERT INTO Meal (diet_id, order_num) VALUES (?, ?);
INSERT INTO Meal_food (meal_id, food_id, food_name, amount, order_num) VALUES (?, ?, ?, ?, ?);
</code></pre>

SQL esimerkki ruokavalion ja kaikkien sen aterioiden sekä ruokien poistamiseksi tietokannasta:

<pre><code>DELETE FROM Diet WHERE Diet.id = :diet_id;
DELETE FROM Meal WHERE Meal.diet_id = :diet_id;
DELETE FROM Meal_food WHERE Meal_food.id IN (
  SELECT Meal_food.id FROM Meal_food 
  JOIN Meal ON Meal_food.meal_id = Meal.id 
  WHERE Meal.diet_id = :diet_id
);</code></pre>
<br>

#### Käyttäjä haluaa perustietoa ruokavalion koostumuksesta

- Käyttäjä näkee makroravinnekoostumuksen ja energiamäärän koostaessaan ruokavaliota.

```diff
+ Toteutettu: käyttäjä näkee jokaisen aterian makroravinnekoostumuksen
+ Toteutettu: käyttäjä näkee koko ruokavalion makroravinnekoostumuksen
```

SQL esimerkki dieetin makroravinnekoostumuksen selvittämiseksi:

<pre><code>SELECT SUM(energy * amount / 100) AS energy, SUM(protein * amount / 100) AS protein, 
SUM(carb * amount / 100) AS carb, SUM(fat * amount / 100) AS fat FROM food
JOIN Meal_food ON Food.id = Meal_food.food_id
JOIN Meal ON Meal_food.meal_id = Meal.id
JOIN Diet ON Meal.diet_id = Diet.id
WHERE diet_id = 1</code></pre>

<br>

#### Käyttäjä haluaa käyttää mitä tahansa ruoka-ainetta ruokavaliossaan tai muokata ruoka-aineen tietoja

- Käyttäjä syöttää haluamansa ruoan nimen ja ravintoainekoostumuksen ruoka-ainetaulukkoon, minkä jälkeen sitä voidaan käyttää ruokavalion osana.

```diff
+ Ruoka-aineille on toteutettu täysi CRUD-toiminnallisuus
+ Ruokataulukosta on tehty käyttäjäkohtainen
```

SQL esimerkki ruoka-aineen päivittämisestä:

<pre><code>UPDATE Food SET name = ?, energy = ?, protein = ?, carb = ?, fat = ? WHERE id = ?</code></pre>

<br>

#### Käyttäjä haluaa yhteenvetotietoja luomistaan ruokavalioista

- Käyttäjä näkee yhteenvedon luomistaan ruokavalioista

```diff
+ Yhteenvetosivu on toteutettu
```

SQL kysely, joka kertoo kuinka monta ruokaa on keskimäärin käyttäjän ruokavalioissa:

<pre><code>SELECT (SELECT COUNT(*) FROM Meal_food) /
(SELECT COUNT(*) AS diet_count FROM Diet)</code></pre>

SQL-kysely, joka kertoo kuinka monta ruoka-ainetta on keskimäärin yhdessä ateriassa:

<pre><code>SELECT AVG(mf_count) FROM (
    SELECT COUNT(*) AS mf_count FROM Meal_food
    GROUP BY Meal_food.meal_id
)</code></pre>

SQL-kysely, joka kertoo eniten käytetyn ruoan ruokavalioissa:

<pre><code>SELECT Food.name, SUM(Meal_food.amount) AS total FROM Meal_food
JOIN Food ON Meal_food.food_id = Food.id
GROUP BY Food.name
ORDER BY total DESC
LIMIT 1</code></pre>