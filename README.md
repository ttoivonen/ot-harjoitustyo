
# **Project effort and cost estimate application**

Sovelluksen tarkoitus on auttaa käyttäjää kasaamaan projektin eri vaiheet ja tehtävät sekä näiden perusteella laskemaan projektiin arvioitu tuntimäärän ja taloudelliset luvut (hinta asiakkaalle ja kannattavuus palveluntarjoajalle). Sovelluksen käyttäjä edustaa palveluntarjoajaa. Sovelluksen käyttötarkoitus on projektin tarjousvaihe, jolloin asiakasneuvotteluissa on tärkeää tietää arvioitu hinta asiakkaalle; taas palveluntarjoajan on hyvä tietää, minkälainen tiimi tarvitaan ja mitä tiimin koostumus tarkoittaa projektin kannattavuudelle (esim. kokeneiden tiimijäsenten kustannus palveluntarjoajalle on korkeampi kuin nuorempien tiimijäsenten).

Sovelluksen pääkomponentti on projekti (luokka Project). Projektille luodaan yksi tai useampi tiimijäsen (luokka TeamMember). Projektille luodaan yksi tai useampi projektivaiheita (luokka Phase). Jokaiseen projektivaiheeseen liitetään yksi tai useampi tehtävä-olio (luokka Task), johon kiinnitetään tiimijäsen, jonka on tarkoitus suorittaa tehtävä. Tehtävälle annetaan arvioitu tuntiarvio. Lopulta annetut tehtäväkohtaiset tuntiarvioit, tiimijäsenten sisäiset tuntihinnat sekä projektin kiinteä tuntihinta asiakkaalle muodostavat laskelman.

Kun käyttäjä on luonnut projektin sovelluksessa, pystyy käyttäjä generoimaan eri näkymiä, jotka sisältävät tietoa projektin rakenteesta, arvioidusta kustannuksesta, arvioiduista tuntimääristä ja arvioidusta kannattavuudesta.

Sovellus on kirjoitettu Pythonilla ja sen riippuvuudeksi on määritelty Python-versio 3.8 tai korkeampi.

## **Julkaisut**

[Release 1 (2021-12-07)](https://github.com/ttoivonen/ot-harjoitustyo/releases/tag/viikko5)

[Release 2 (2021-12-14)](https://github.com/ttoivonen/ot-harjoitustyo/releases/tag/viikko6)

[Loppupalautus (2021-12-27)](https://github.com/ttoivonen/ot-harjoitustyo/releases/tag/loppupalautus)


## **Dokumentaatio**

[Vaatimusmäärittely](https://github.com/ttoivonen/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)

[Arkkitehtuuri](https://github.com/ttoivonen/ot-harjoitustyo/blob/master/dokumentaatio/arkkitehtuuri.md)

[Tuntikirjanpito](https://github.com/ttoivonen/ot-harjoitustyo/blob/master/dokumentaatio/tuntikirjanpito.md)

[Testausdokumentti](https://github.com/ttoivonen/ot-harjoitustyo/blob/master/dokumentaatio/testaus.md)

[Käyttöohje](https://github.com/ttoivonen/ot-harjoitustyo/blob/master/dokumentaatio/kayttoohje.md)


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
