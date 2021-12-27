# **Testausdokumentti**

Automatisoituja testauksia on sovelluksessa yksikkö- sekä integraatiotasolla Pythonin unittest-moduulilla. Integraatiotestausta on myös tehty paljon manuaalisestii kokeilemalla erilaisia skenaarioita ohjelmaa käyttäessä.

## **Yksikkö- ja integraatiotestaus**


### **Sovelluslogiikka**

Sovelluslogiikasta vastaa ProjectService-luokka, jota on testattu alustamalla projektin rakentaminen eri vaiheisiin ja sitten kutsumalla sovelluslogiikan metodeja. Metodit, jotka toimivat pääosin tulostustarkoituksessa on testattu automaatisesti sillä tasolla, että ne toimivat ilman virheitä. Tulostuksen oikeellisuus on varmistettu manuaalisesti.

Sovelluslogiikan testit sisälsivät lähestulkoon vain integraatiotestejä, joissa sovelluksen eri luokat toimivat yhdessä.

### **Entities-luokat**

Luokkien Project, Phase ja Task yksikkötestaus on suoritettu automaattisin testein (unittest). Integraatiotestausta on myös suoritettu automaattisin testein. Tulostukseen perustuvia metodeja on testattu manuaalisesti ajamalla ohjelmaa eri skenaarioin ja syöttein.

Jokaiselle edellä mainitulle entities-hakemiston luokalla on oma testiluokkansa automaattisille testeille.

## **Testikattavuus**

Testikattavuus on 86 prosenttia. Käyttöliittymä on jätetty testikattavuusraportin ulkopuolelle. Sovelluslogiikasta testikattavuus ei kata paria tulostusmetodia, jotka on varmistettu manuaalisesti katsomalla tulostus sekä tulostusmetodin käyttämät metodit on testattu luokissaan (esim. Project-luokan calculate_total_profitability()).

![testikattavuusraportti](/dokumentaatio/kuvat/testikattavuus_2021-12-27.PNG)

## **Järjestelmätestaus**

Järjestelmätestaaminen on tehty manuaalisesti.

## **Toiminnallisuudet**

[Määrittelydokumentin](/dokumentaatio/vaatimusmaarittely.md) toiminnallisuudet, jotka on merkitty toteutuneiksi/tehdyiksi, on testattu sekä yksikkö- että integraatiotestauksessa. Manuaalinen testaus ajamalla ohjelmaa eri syötteillä on myös ollut suuressa osassa.

Huom. puutteita on voinut jäädä testaamalla vääriä syötteitä.
