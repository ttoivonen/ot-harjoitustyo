# **Arkkitehtuuri**

### **Rakenne**

Alla on kuvattuna ohjelman luokka- ja pakkauskaavio.

![..](/dokumentaatio/kuvat/pakkausjaluokkakaavio.png)


### **Sovelluslogiikka**

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


### **Päätoiminnallisuudet**

#### **Projektin luominen**

Projekti luodaan siten, että käyttöliittymä (ProjectManagement-luokka) pyytää käyttäjää antamaan syötteinä projektin tiedot, kuten esim. nimi ja asiakas. Sen jälkeen käyttöliittymä kutsuu sovelluslogiikkaa (ProjectService-luokka) ja syöttää sovelluslogiikalla luotavan projektin tiedot. Sovelluslogiikka kutsuu sen jälkeen projekin luokkaa (Project-luokka), joka luo "new_project"-olion. Olio asetetaan aktiiviseksi projektiksi sovelluslogiikkaan (sekä tallennetaan listaan, jonka on tarkoitus myöhemmin auttaa sovelluksen laajentamisessa). Sovelluslogiikkaa palauttaa vielä käyttöliittymällä ja käyttäjälle viestin "True" merkiksi, että projektin luominen on onnistunut. Alla on kuvaus projektin luominsen prosessista sekvenssikaavion muodossa.

![Projektin luominen](/dokumentaatio/kuvat/projektin_luonti.png)
