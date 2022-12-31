# ProgettoGuarrasi
## Come si muovono i taxi a New York?

In questo progetto svolgiamo un'analisi dei taxi a New York. In particolare, siamo curiosi di rispondere ad alcune specifiche Research Questions (RQ) che possono aiutare i tassisti a pianificare i loro spostamenti in città e ai clienti ad avere suggerimenti sulla convenienza dell’utilizzo di questo servizio.
Per questo progetto utilizziamo i dati pubblici delle rotte dei Taxi a NYC disponibili su https://www1.nyc.gov/site/tlc/about/tlc-trip-record-data.page. 
Di default il programma utilizzera dei dati relativi ai Yellow Taxi per l'anno 2022.

## Prima di cominciare

Per preparare il programma al suo corretto utilizzo strutturare la directory, con i dati scaricabili al link sopra, come segue

[Primo link][link1] Vanno scaricati tutti i file relativi ai "yellow trip data" con estenzione  .parquet che andranno inseriti nella cartella ./dati/anni e nell'opportuno anno. 
**Esempio** quelli del 2022 andranno inseriti nella directory ./dati/anni/2022

[Secondo link][link1] Dal seguente link dovrete scaricare il file "taxi+_zone_lookup.csv" che dovra essere inserito nella directry ./dati/tabelle_di_conversione

## Tipica struttura della directory del programma

    .
    ├── dati
    │   ├── anni
    │       ├── 2022
    │           ├── yellow_tripdata_2022-01.parquet    #scaricare i file dal link sopra
    │           ├── yellow_tripdata_2022-02.parquet    #mantenendo la struttura del nome,
    │           └── ...                                #in caso fosse aggiunto ..(1).parquet 
    │                                                  #"(1)"deve essere eliminato
    │       ├── 2021
    │           └── ...
    │       ├── 2020
    │           └── ...
    │   ├── tabelle_di_conversione
    │       ├── taxi+_zone_lookup.csv
    ├── output
    ├── .gitignore
    ├── requirements.txt
    ├── main.py
    ├── ... *.py 
    ├── ... *.py 
    └── README.md
## Input e Output

Il programma viene avviato da riga di comando eseguendo il seguente comando, inserendo un anno parametro obbligatorio 
```sh
python main.py 2022
```

Il programma accetta da riga di comando i seguenti input e restituisce dei grafici da terminale, ogni risultato viene poi salvato nella cartella ./output insime ad un **PDF** riepilogativo

| Input |Input opzionali | Output |
| ------ | ------ | ------ |
| anno| mese, borough(quartiere) | file, grafico |

**NOTA**
Per l'anno 2022 saranno disponibili sono i primi 10 mesi 
L'elenco dei quartieri è il seguente :
- Bronx
- Brooklyn
- EWR
- Manhattan
- Queens
- Staten Island
- Unknown

Per maggiori informazioni consultare help da riga di comando

```sh
python main.py help
```

## Conclusione
Verra cosi illustrata la mondalità di pagamento piu comune e la meno comune e per ogni **Quartiere** verra mostrato l'utilizzo per ogni metodo di pagamento. Il risultato verra stampato da riga di comando a cui seguiranno due grafici che illustrano nel dettaglio il risultato oppure tutti i risultati saranno poi consultabili da **Risultati.pdf** nella cartella **output**
 

   [link1]: https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page
   [link2]: https://d37ci6vzurychx.cloudfront.net/misc/taxi+_zone_lookup.csv