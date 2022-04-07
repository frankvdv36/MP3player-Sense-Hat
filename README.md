# MP3player-Sense-Hat
## Beschrijving
De Raspberry Sense Hat heeft naast de sensoren ook een joystick en RGB leds.
Deze laatste worden gebruikt om van de combinatie een MP3 player te maken met bediening 
Mogelijkheden:
Een reeks MP3-files in shuffle-play afspelen zodat iedere track maar 1xafgespeeld wordt.
De mogelijkheden zijn: Play Pauze Stop Volume+ en Volume-  
Joystick:
UP: Volume+ 
DOWN: Volmue-
RIGHT: Play
LEFT: Stop
Push: Pause of Resume (verder spelen)

## Bronnen
https://github.com/astro-pi/python-sense-hat/blob/master/examples/pygame_joystick.py
Op deze site wordt de Sense Hat beschreven en we gebruiken de voorbeelden van de joystick als basis van de bediening.
https://github.com/astro-pi/python-sense-hat/blob/master/examples/text_scroll.py
Op deze pagina wordt als voorbeeld tekst zichtbaar gemaakt. Wordt gebruikt om de MP3 file op het scherm te plaatsen.
https://www.pygame.org/docs/ref/mixer.html
Op deze site gebruiken we de mixer van Pygame om de MP3 files af te spelen.
https://stackoverflow.com/questions/7746263/how-can-i-play-an-mp3-with-pygame
Met deze pagine was een snelle start mogelijk om het project aan te vatten
https://www.geeksforgeeks.org/python-playing-audio-file-in-pygame/

## Hardware
https://www.raspberrypi.com/products/sense-hat/

## Software
De symbolen van Stop, Play, Pauze, Volume + en - worden op het led-scherm getoond.
De naam van de song komt pas op de display na het drukken van de pauzeknop.
Om te voorkomen dat een liedje 2x voorkomt bij shuffleplay maken we een kopie van de liedjesnamen naar een afzonderlijke lijst.
Telekens een liedje start wordt deze gewist uit de lijst. Dit herhaalt zich tot de lijst leeg is. 
De software werkt behoorlijk. Enkel bij op het einde van de lijst wordt het programma plots afgebroken.

Autostart bij power-up: dit wordt verkregen door de volgende handelingen te doen. Zie ook in bijlage 'leesme.txt'
1. Maak een map aan 'autostart' onder /home/pi/
2. Plaats daarin het python programma 'start.py'
3. sudo nano /etc/xdg/autostart/start.desktop
4. Plaats de volgende regels in: 
 - [Desktop Entry] 
 - name=autostart  
 - Exec= /usr/bin/python /home/pi/autostart/tart.py 
6. Deze file opslaan

De uitgang is 3.5mm connector
### Eigen scripts en programma's
Zie in bijlagen.
