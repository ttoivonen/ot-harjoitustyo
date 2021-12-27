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

Testikattavuus on 86 prosenttia. Käyttöliittymä on jätetty testikattavuusraportin ulkopuolelle. 
