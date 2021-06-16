# RailNL

Voor de case RailNl moesten wij lijnvoeringen maken voor treinen. Bij een lijnvoering kijk je welke trajecten er mogelijk zijn waar treinen gedurende de dag heen en weer over kunnen rijden. Bij een traject heb je bijvoorbeeld een start station en een tijdsframe, bijv. 2 uur, en dan kijk je dus waar een trein vanaf dat start station in 2 uur heen kan. Hieronder zie je op de afbeelding een voorbeeld van een lijnvoering met 7 trajecten, elk traject/trein heeft een eigen kleur. 
<img width="500" alt="Plot of route" src="https://user-images.githubusercontent.com/58465462/122235804-487a1300-cebe-11eb-9a86-a57b5b5f1eb0.png">

Bij deze case hadden wij 2 opdrachten: allereerst moesten wij een lijnvoering maken voor Noord- en Zuid-Holland, waarbij wij 22 stations hadden en daarvoor binnen 2 uur maximaal 7 trajecten moesten maken. Voor de 2e opdracht moesten wij een lijnvoering maken voor heel Nederland, daarbij hadden we 62 stations en moesten we in een tijdsframe van 3 uur maximaal 20 trajecten maken.


## Aanpak
Wij hebben verschillende algoritmes geprobeerd om een zo hoog mogelijk scorende lijnvoering te maken tussen intercity stations in Noord- en Zuid-Holland en Nederland. Deze zullen wij hieronder even uitleggen:


### Random algoritme
Wij zijn begonnen met een random algoritme. Hierbij pakte wij telkens een random begin station, daarvoor pakte wij een random connectie. Die connectie werd weer het nieuwe station waar je een random connectie voor moest pakken etc. Dit herhaalde wij tot elk traject kleiner was dan 2 uur en er max 7 trajecten waren ontstaan.


### Hill climber
Bij Hill climber heb je een random route en deze vergelijk je steeds met een andere random route. Degene met de hoogste score houd je vast. Dit herhaal je steeds tot een gegeven aantal keer.


## Aan de slag 

1. Instaleer python en Pip

2. clone de repository (in terminal) of download het als zip bestand (klik op groene button rechts bovenin):
```
$ git clone https://github.com/Lauraa2/brein-trein.git
```

3. instaleer requirements.txt
```
$ pip install requirements.txt
```


### Runnen in terminal
Nu de code op je computer staat en je alle requirements gedownload hebt, kun je de code runnen. Je kunt onze code op verschillende manieren runnen, omdat wij verschillende bestanden en algoritmes gebruiken. De volgende mogelijkheden bestaan er:

1. trajecten voor Noord- en Zuid-Holland met Hill climber algoritme:
```
$ python3 main.py Holland
```

2. trajecten voor Nederland met Hill climber algoritme:
```
$ python3 main.py Nationaal
```