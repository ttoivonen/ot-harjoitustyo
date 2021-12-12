# **Käyttöohje**

Hae ohjelman [viimeisin release](https://github.com/ttoivonen/ot-harjoitustyo/releases) lataamalla lähdekoodi Assets-osiosta (_Source code_).

## **Projektin konseptuaalinen kuvaus**

Alla on kuvattu projektin rakenne konseptuaalisesti. Kuvaus voi auttaa hahmottamaan ohjelman toimintaa. Tärkeää on huomata, että ohjelman neljä komponenttia ovat:
- projekti (luokka Project)
- projektivaihe (luokka Phase)
- tehtävä (luokka Task)
- tiimijäsen (luokka TeamMember)

![konsepti](/dokumentaatio/kuvat/ko_projektikonsepti.png)

Projektin rakenteessa ja hierarkiassa projekti (Project) on ylin. Seuraavaksi on vaihe (Phase), ja alimpana tehtävä (Task). Projektilla on vaiheita, joissa taas on tehtäviä. Projektille luotuja tiimijäseniä liitetään tehtäviin.

Projektilla on yksi kiinteä tuntihinta (projektin asiakkaalle). Tiimijäsenillä on oma sisäinen kustannus (internal cost). Tehtäviin taas asetetaan arvioitu aika tehtävän suorittamiseen. Nämä määreet annetaan ohjelman suorituksessa ja määrittävät lopulta projektin arvioidun ulkoisen (asiakas-)kustannuksen, sisäisen kustannuksen sekä kannattavuuden.


## **Ohjelman käynnistäminen**

1. Asenna riippuvuudet komennolla ```poetry install```
2. Käynnistä ohjelma komennolla ```poetry run invoke start```


#### **Projektin luominen**

Ohjelma alkaa projektin luomisella. Ohjelman myöhemmät komponentit tehdään luotavalle projektille.

Anna syötteet terminaalissa ja paina enter jokaisen kohdan jälkeen. Ohjelma ilmoittaa, kun uusi projekti on luotu onnistuneesti.

![Projektin luominen](/dokumentaatio/kuvat/ko_luo_projekti.PNG)

Kun projekti on luotu, seuraavaksi projektille on luotava tiimijäsenet, projektivaihe/-vaiheita ja tehtävä/tehtäviä. Huom., että tehtävän luominen on riippuvainen siitä, että on olemassa vähintään yksi projektivaihe (johon tehtävä kiinnitetään) ja vähintään yksi tiimijäsen (joka suorittaa tehtävän).

#### **Tiimijäsenen luominen**

Valitse "1 add team members to the project team" syöttämällä "1" kohtaan "select activity" ja paina enter.

![Luo tiimijasen1](/dokumentaatio/kuvat/ko_luo_tiimijasen1.PNG)

Syötä seuraavaksi tiimijäsenen tiedot ja paina enter edetäksesi. Taitojen kohdalla voit syöttää taitoja 0:n ja äärettömän väliltä. Syöttämällä "x" pääset etenemään taitojen syöttämisestä eteenpäin. Kun tiimijäsen on luotu, ohjelma ilmoittaa tapahtuman onnistumisesta.

![Luo tiimijasen2](/dokumentaatio/kuvat/ko_luo_tiimijasen2.PNG)

#### **Projektivaiheen luominen**

Valitse aktiviteettivalikosta numero 2 syötteellä "2" ja paina enter. Anna sen jälkeen syötteenä projektivaiheen kuvaus ja paina enter. Ohjelma ilmoittaa, kun projektivaihe on luotu onnistuneesti. Kuvassa esimerkkisyötteet keltaisella.

![Projektivaiheen luonti](/dokumentaatio/kuvat/ko_luo_projektivaihe1.PNG)

#### **Tehtävän luominen**

Valitse aktiviteettivalikosta numero 3 syötteellä "3" ja paina enter. Valitse sen jälkeen, mihin projektivaiheeseen tehtävä asetetaan - valitse projektivaihe numerosyötteenä (kuvassa on vain yksi projektivaihe saatavilla numerolla "1", vaihe "preparation"). Seuraavaksi valitse numerosyötteellä, kuka tiimijäsen suorittaa tehtävän; esimerkissä valitaan tiimijäsen "Aaron" syötteellä "1". Anna sen jälkeen syötteenä tehtävän kuvaus sekä arvio tehtävän tuntimäärästä. Ohjelma ilmoittaa jälleen onnistuneesta luontiprosessista. Kuvassa esimerkkisyötteet ovat keltaisella.

![Luo tehtävä](/dokumentaatio/kuvat/ko_luo_tehtava.PNG)
