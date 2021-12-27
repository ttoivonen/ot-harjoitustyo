# **Arkkitehtuuri**

## **Rakenne**

Alla on kuvattuna ohjelman luokka- ja pakkauskaavio.

![..](/dokumentaatio/kuvat/pakkausjaluokkakaavio.png)

## **Käyttöliittymä**

Käyttöliittymästä vastaan ProjectManagement-luokka. Luokka vastaa käyttäjän syötteiden vastaanottamisesta ja niiden toimittamisesta sovelluslogiikan luokkaan ProjectService. Käyttöliittymän kautta käyttäjällä kaksi eri päävalikkoa.
1. Aktiviteettivalikko, josta voi lisätä tai poistaa projektin tietorakenteita (esim. uuden projektivaiheen luominen)
2. Näkymävalikko, josta käyttäjä pääsee näkemään tietoja projektista (esim. projektin kustannusarviot projektivaiheittain)

Ohjelma alkaa aktiviteettivalikolla, jonka kautta on mahdollista siirtyä näkymävalikkoon. Näkymävalikosta pääsee siirtymään takaisin aktiviteettivalikkoon.

## **Sovelluslogiikka**

Alla on kuvattuna ohjelman sovelluslogiiikka.

![Kuvaus sovelluslogiikasta](/dokumentaatio/kuvat/sovelluslogiikka.png)

Ohjelman toiminnallisuuksista ja sovelluslogiikasta vastaa ProjectService-luokka, jonka vastuulla on toimenpiteiden järjestäminen siten, että käyttäjä saa muodostettua projektia vastaavan tietomallin alla esiteltävistä kolmesta projektia kuvaavasta luokasta (Phase, Task ja TeamMember). ProjectService vastaa myös tietomallien avulla generoitujen näkymien ("raporttien") muodostamisesta. ProjectServicessä on metodit käyttöliittymästä annettaville käskyille.

Ohjelman logiikka ja tietomalli perustuu luokkiin, jotka kuvaavat projektin (Project) rakennetta projektisuunnitelman tasolla:
- projektilla on tiimijäseniä (TeamMember)
- projekti koostuu useista vaiheista (Phase)
- jokaisessa vaihessaa on tehtäviä (Task), joita tiimijäsenet suorittavat

Aluksi määritellään projekti. Projektille tehdään sen jälkeen tiimijäseniä ja vaiheita. Jotta tehtävän voi lisätä on oltava vähintään yksi vaihe ja vähintään yksi tiimijäsen suorittamaan tehtävä.
Kun sovelluksella on määritelty projektin eri vaiheet ja vaiheiden eri tehtävät sekä kuka tiimijäsen suorittaa minkäkin tehtävän, lopulta muodostuu tietorakenne, jossa on seuraavat elementit:
- projektin kiinteä tuntihinta
- kuinka monta tuntia projektin tekeminen vie (tiimijäsenten eri vaiheiden tehtävien suorittamiseen arvioitu tuntimäärä yhteensä)
- tiimijäsenten hinta (kustannus) palveluntarjoajalle, eli projektin suorittavalle organisaatiolle (oletuksena, että tiimii kostuu eri kokemuksella ja taidoilla varustetuista tiimijäsenistä, joista taitavimmat ovat kalliimpia palveluntarjoajalle).
Edellämainittujen tietojen perusteella voidaan laskea projektin arvioitu kustannus asiakkaalle (tunnit yhteensä * projektin kiinteä tuntihinta) ja projektin kannattavuus (projektin hinta asiakkaalle - (tiimijäsenkohtainen tuntihinta x tiimijäsenen tunnit) sekä miten kustannukset jakautuvat vaiheittain. 

## **Tietojen tallennus**

Käyttäjän luoma projekti voidaan tallentaa Excel-tiedostoon (xlsx-formaatti) aktiviteettivalikon "6 save project to a Excel file" -ominaisuudella. Käyttäjä antaa tiedoston nimen, ja ohjelma hakee sen jälkeen projektin tiedot tehtävä-tasolta sekä yhteenvedon kannattavuudesta, kuluista ja tunneista. Excel-tiedostoon tallentaminen tapahtuu Pythonin Xlsxwriter-moodulilla, joka on ohjelman riippuvuus.


## **Päätoiminnallisuudet**

#### **Projektin luominen**

Projekti luodaan siten, että käyttöliittymä (ProjectManagement-luokka) pyytää käyttäjää antamaan syötteinä projektin tiedot, kuten esim. nimi ja asiakas. Sen jälkeen käyttöliittymä kutsuu sovelluslogiikkaa (ProjectService-luokka) ja syöttää sovelluslogiikalla luotavan projektin tiedot. Sovelluslogiikka kutsuu sen jälkeen projekin luokkaa (Project-luokka), joka luo "new_project"-olion. Olio asetetaan aktiiviseksi projektiksi sovelluslogiikkaan (sekä tallennetaan listaan, jonka on tarkoitus myöhemmin auttaa sovelluksen laajentamisessa). Sovelluslogiikkaa palauttaa vielä käyttöliittymällä ja käyttäjälle viestin "True" merkiksi, että projektin luominen on onnistunut. Alla on kuvaus projektin luominsen prosessista sekvenssikaavion muodossa.

![Projektin luominen](/dokumentaatio/kuvat/projektin_luonti.png)

#### **Tiimijäsenen luominen**

Käyttäjä syöttää komennon "1" aktiviteettivalikkossa, jonka jälkeen käyttöliittymä pyytää käyttäjää syöttämään tiimijäsenen tiedot. Sen jälkeen käyttölittymä kutsuu sovelluslogiikkaa, ProjectService-luokkaa, joka saa parametreina tiimijäsenen tiedot. Sovelluslogiikka luo TeamMember-olion ja sen jälkeen lisää uuden tiimijäsenen olion Project-oliossa olevaan team_members-listaan.

![tiimijäsen](/dokumentaatio/kuvat/create_tm_arkkitehtuuri.PNG)

#### **Näkymien generointi**

Näkymien generoinnilla tarkoitetaan projektin rakenteen perusteella printattavia näkymiä, jotka perustuvat käyttäjän luomaan projektiin. Näkymistä selviää esim. asiakkaan arvioidut kustannukset, palveluntarjoajan sisäiset kustannukset, projektin vaiheet ja tehtävät sekä kannattavuus. 

Näkymän generointi alkaa käyttöliittymästä, jossa käyttäjä antaa syötteen sen mukaan, mikä näkymä halutaan generoida. Käyttölittyymä kutsuu sovellusloogiikkaa, joka kutsuu luokkia sen mukaan, mitä tietoa tarvitaan. Esim. alla sovelluslogiikan luokka ProjectService voi kutsua Phase-luokkaa antamaan tiedot projektivaiheen sisäisistä kustannuksista. Phase-luokkaa suorittaa laskennan palauttaa tulokset. Sovelluslogiikka voi vielä yhdistellä ja muokata tietoja ennen printtausta. Kun operaatiot on suoritettu onnistuneesti, sovelluslogiikka palauttaa vielä sitä kutsuneelle käyttöliittymälle True-boolean-arvon merkiksi onnistuneesta suorituksesta.

Alla kuvattuna yleisellä tasolla näkymien generointi sekvenssikaaviolla.
![makymien generointi](/dokumentaatio/kuvat/generoi_nakyma.PNG)

