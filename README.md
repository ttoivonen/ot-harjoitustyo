
# **Project estimating application**

Kuvaus tulossa, kts. sillä välin vaatimusmäärittely.

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
