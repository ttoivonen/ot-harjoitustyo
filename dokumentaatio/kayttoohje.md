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


## **Projektin luominen**

Ohjelma alkaa projektin luomisella. Ohjelman myöhemmät komponentit tehdään luotavalle projektille.

Anna syötteet terminaalissa ja paina enter jokaisen kohdan jälkeen. Ohjelma ilmoittaa, kun uusi projekti on luotu onnistuneesti.

![Projektin luominen](/dokumentaatio/kuvat/ko_luoprojekti.PNG)

Kun projekti on luotu, seuraavaksi projektille on luotava tiimijäsenet, projektivaihe/-vaiheita ja tehtävä/tehtäviä. Huom., että tehtävän luominen on riippuvainen siitä, että on olemassa vähintään yksi projektivaihe (johon tehtävä kiinnitetään) ja vähintään yksi tiimijäsen (joka suorittaa tehtävän).


## **Tiimijäsenen luominen**

Valitse "1 add team members to the project team" syöttämällä "1" kohtaan "select activity" ja paina enter.

Syötä seuraavaksi tiimijäsenen tiedot ja paina enter edetäksesi. Taitojen kohdalla voit syöttää taitoja 0:n ja äärettömän väliltä. Syöttämällä "x" pääset etenemään taitojen syöttämisestä eteenpäin. Kun tiimijäsen on luotu, ohjelma ilmoittaa tapahtuman onnistumisesta. Kuvassa keltaisella esimerkkisyötteet.

![Luo tiimijasen1](/dokumentaatio/kuvat/ko_luotiimijasen.PNG)


## **Projektivaiheen luominen**

Valitse aktiviteettivalikosta numero 2 syötteellä "2" ja paina enter. Anna sen jälkeen syötteenä projektivaiheen kuvaus ja paina enter. Ohjelma ilmoittaa, kun projektivaihe on luotu onnistuneesti. Kuvassa esimerkkisyötteet keltaisella.

![Projektivaiheen luonti](/dokumentaatio/kuvat/ko_luovaihe.PNG)


## **Tehtävän luominen**

Valitse aktiviteettivalikosta numero 3 syötteellä "3" ja paina enter. Valitse sen jälkeen, mihin projektivaiheeseen tehtävä asetetaan - valitse projektivaihe numerosyötteenä. Esimerkkikuvassa tehtävä luodaan vaiheelle "Preparation" syötteellä "1". Seuraavaksi valitse numerosyötteellä, kuka tiimijäsen suorittaa tehtävän; esimerkissä valitaan tiimijäsen "Aaron" syötteellä "1". Anna sen jälkeen syötteenä tehtävän kuvaus sekä arvio tehtävän tuntimäärästä. Ohjelma ilmoittaa jälleen onnistuneesta luontiprosessista. Kuvassa esimerkkisyötteet ovat keltaisella.

![Luo tehtävä](/dokumentaatio/kuvat/ko_luotask.PNG)


## **Näkymävalikko ja näkymien generointi**

Kun ohjelmassa on määritelty vähintään yksi tiimijäsen, yksi projektivaihe ja yksi tehtävä, on mahdollista alkaa generoimaan eri näkymiä projektin rakenteesta sekä tunneista ja kustannuksista. Pääset siirtymään näkymien valikkoon syötteellä "7" aktiviteettivalikosta ja painamalla enter. Näkymävalikko ilmestyy.

Näkymien valikossa on saatavilla neljä eri vaihtoehtoa, joista voi generoida projektin tietoja.
1. näytä tiimijäsenet (display team members)
2. näytä projektivaiheet (display project phases)
3. näytä tehtävät (display tasks)
4. näytä projektin arviot vaiheiden mukaan (display project estimates on phase level)
5. näytä projektin kokonaisarviot (display total estimates of the project)

![Näkymät](/dokumentaatio/kuvat/ko_nakymat.PNG)

Näkymät valitaan antamalla syötteeksi näkymän numero, kuten "4" esimerkkikuvassa, jos haluaan nähdä projektin kustannus- ja tuntiarviot projektivaiheiden mukaan. Numeron syöttämisen jälkeen paina enter ja näkymä generoituu.

Pääset siirtymään näkymävalikosta takaisin aktiviteettivalikkoon syötteellä "x" ("return") ja painamalla enter.


## **Projektivaiheen ja tehtävän poistaminen**

Aktiviteettivalikossa projektivaiheen voi poistaa syötteen "4" kautta ja tehtävän voi poistaa syötteen "5" kautta. Molemmat toimivat samalla periaatteella: ohjelma printtaa olemassa olevat vaiheet/tehtävät, joilla on indeksinumero, jonka käyttäjä syöttää osoittaakseen, mistä indeksistä projektivaihe/tehtävä poistetaan. Esimerkkikuvassa poistetaan tehtävä, joka on indeksissä 1.2 ("Research" tiimijäsenellä "Aaron").

![Poisto](/dokumentaatio/kuvat/ko_deletetask.PNG)


## **Excel-tiedostoon tallennus**

Aktiviteettivalikon "save project to Excel file" (syöte "6") käyttäjä voi tallettaa luodun projektin tiedot Excel-tiedostoon. Ohjelma pyytää käyttäjää nimeämään tiedoston. Ohjelma ilmoittaa onnistuneesta tallennuksesta.

![tiedosto1](/dokumentaatio/kuvat/ko_tallennaxlsx.PNG)

Excel-tiedosto tallennetaan src-hakemiston sisällä olevaan saved_project_files-alihakemistoon.
![tiedosto2](/dokumentaatio/kuvat/ko_tallennaxlsx2.PNG)

Tiedostoon tallentuvat projektin arvioidut tunnit ja kustannukset tehtävätasolla (välilehti "Phase and Tasks") sekä yhteenveto projektin tiedoista (välilehti "Totals").

![tiedosto3](/dokumentaatio/kuvat/ko_tallennaxlsx3.PNG)
