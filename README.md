
# **Project effort and cost estimate application**

Sovelluksen tarkoitus on auttaa käyttäjää kasaamaan projektin eri vaiheet ja tehtävät sekä näiden perusteella laskemaan projektiin arvioitu tuntimäärän ja taloudelliset luvut (hinta asiakkaalle ja kannattavuus palveluntarjoajalle). Sovelluksen käyttäjä edustaa palveluntarjoajaa. Sovelluksen käyttötarkoitus on projektin tarjousvaihe, jolloin asiakasneuvotteluissa on tärkeää tietää arvioitu hinta asiakkaalle; taas palveluntarjoajan on hyvä tietää, minkälainen tiimi tarvitaan ja mitä tiimin koostumus tarkoittaa projektin kannattavuudelle (esim. kokeneiden tiimijäsenten kustannus palveluntarjoajalle on korkeampi kuin nuorempien tiimijäsenten).

Sovelluksen pääkomponentti on projekti (luokka Project). Projektille luodaan yksi tai useampi tiimijäsen (luokka TeamMember) Projektille luodaan yksi tai useampi projektivaiheita (luokka Phase). Jokaiseen projektivaiheeseen liitetään yksi tai useampi tehtävä-olioi (luokka Task), johon kiinnitetään tiimijäsen, jonka on tarkoitus suorittaa tehtävä.

Projektille annetaan kiinteä tuntihinta, joka on kustannus asiakkaalle.

## **Dokumentaatio**

[Vaatimusmäärittely](https://github.com/ttoivonen/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)

[Arkkitehtuuri](https://github.com/ttoivonen/ot-harjoitustyo/blob/master/dokumentaatio/arkkitehtuuri.md)

[Tuntikirjanpito](https://github.com/ttoivonen/ot-harjoitustyo/blob/master/dokumentaatio/tuntikirjanpito.md)


## **Asennus**

1. Asenna riippuvuudet komennolla ```poetry install```
2. Käynnistä ohjelma komennolla ```poetry run invoke start```

## **Komentorivitoiminnot**


#### **Ohjelman suorittaminen**
Ohjelma suoritetaan komennolla:  ```poetry run invoke start```

#### **Testaus**
Testit suoritetaan komennolla: ```poetry run invoke test```

#### **Testikattavuus**
Testikattavuusraportti ajetaan komennolla: ```poetry run invoke coverage-report```

#### **Pylint**
Tiedostossa [.pylintrc](https://github.com/ttoivonen/ot-harjoitustyo/blob/master/.pylintrc) määritellyt koodin laatutarkastukset suoritetaan komennolla: ```poetry run invoke lint```
