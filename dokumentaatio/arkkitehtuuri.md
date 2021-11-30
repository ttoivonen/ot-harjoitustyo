# **Arkkitehtuuri**

### **Rakenne**

Alla on kuvattuna ohjelman luokka- ja pakkauskaavio.

![..](/dokumentaatio/kuvat/pakkausjaluokkakaavio.png)


### **Sovelluslogiikka**

![Kuvaus sovelluslogiikasta](/dokumentaatio/kuvat/sovelluslogiikka.png)
Ohjelman logiikka perustuu luokkiin, jotka kuvaavat projektin (Project) rakennetta projektisuunnitelman tasolla:
- projektilla on tiimijäseniä (TeamMember)
- projekti koostuu useista vaiheista (Phase)
- jokaisessa vaihessaa on tehtäviä (Task), joita tiimijäsenet suorittavat

Aluksi määritellään projekti. Projektille tehdään sen jälkeen tiimijäseniä ja vaiheita. Jotta tehtävän voi lisätä on oltava vähintään yksi vaihe ja vähintään yksi tiimijäsen suorittamaan tehtävä.
Kun sovelluksella on määritelty projektin eri vaiheet ja vaiheiden eri tehtävät sekä kuka tiimijäsen suorittaa minkäkin tehtävän, lopulta muodostuu tietorakenne, jossa on seuraavat elementit:
- projektin kiinteä tuntihinta
- kuinka monta tuntia projektin tekeminen vie (tiimijäsenten eri vaiheiden tehtävien suorittamiseen arvioitu tuntimäärä yhteensä)
- tiimijäsenten hinta (kustannus) palveluntarjoajalle, eli projektin suorittavalle organisaatiolle (oletuksena, että tiimii kostuu eri kokemuksella ja taidoilla varustetuista tiimijäsenistä, joista taitavimmat ovat kalliimpia palveluntarjoajalle).
Edellämainittujen tietojen perusteella voidaan laskea projektin arvioitu kustannus asiakkaalle (tunnit yhteensä * projektin kiinteä tuntihinta) ja projektin kannattavuus (projektin hinta asiakkaalle - (tiimijäsenkohtainen tuntihinta x tiimijäsenen tunnit) sekä miten kustannukset jakautuvat vaiheittain. 
