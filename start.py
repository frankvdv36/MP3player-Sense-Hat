# https://projects.raspberrypi.org/en/projects/getting-started-with-the-sense-hat/9
from sense_hat import SenseHat
sense = SenseHat()
import pygame
import os, random
import time

path = '/home/pi/Music/'		# intern geheugen
#path = '/media/pi/USB2/'		# USB stick (naam moet wel kloppen
mp3files = []					# lijst van de mp3 tracks in map
mp3list = []					# kopie van de mp3 namen, is werklijst 
tracknum = 0					# tracknummer die is gekozen
key = 0							# gedrukte functie op joystick 0=stop 1=play 2=pause 3= einde
volume = 0.5			        # Volmue werkt tussen 0-2 of 1.5 
e = (0, 0, 0)
#w = (255, 255, 255)
w = (150, 150, 150)
e = (0, 0, 0)
r = (255, 0, 0)
g = (0, 255, 0)
b = (0, 0, 255)

########################################################################

def mp3check():								# Hoeveel mp3 files zijn er + kopie lijst
	global mp3list
	for f in os.listdir(path):
		if f[len(f)-4:]=='.mp3':
			mp3files.append(f)
	mp3list = mp3files
	print(mp3list)							# print alle tracks

def starttrack():							# start mp3 + wis deze mp3 uit de lijst
	global key
	global mp3list
	global track
	track = random.choice(mp3list)			# selecteert willekeurige track
	tracknum = mp3list.index(track)			# bepaal track nummer van de lijstr
	print('')
	print('Play: ',track, ' = Tracknum: ',tracknum)
	pygame.mixer.init()
	pygame.mixer.music.load(path+track)		# path toegevoegd aan track anders werkt het niet
	pygame.mixer.music.set_volume(0.5)
	pygame.mixer.music.play()				# (0)/() = once (1) 2x etc  (-1) for infinetely 
	key = 1												# in play mode
	print ('Tracks to go: ',len(mp3list))				# Aantal tracks in list
	print ('Index track: ',mp3list.index(track))		# onthoudt index track
	del mp3list[tracknum]								# wis deze track uit de lijst
	
	
def displaymp3():
	global track
	sense.set_rotation(0)
	kleur = (0, 150, 150)								# RGB 0-255
	sense.show_message(track, text_colour=kleur)

		
def stoptrack():
	global key
	pygame.mixer.music.stop()
	key = 0
	print('Stop key: ',key)
	
def volumeH():
	global volume
	print('Volume hoger')
	print ('Volume: ',volume)
	if volume <= 1.1:			# max. volume is 1
		volume = volume + 0.1
		pygame.mixer.music.set_volume(volume)
	
def volumeL():
	global volume
	print('Volume lager')
	print ('Volume: ',volume)
	if volume >= 0.2:
		volume = volume - 0.1	# min. volume is 0.1
		pygame.mixer.music.set_volume(volume)
	
  
def toggleMusic():
	global key
	if pygame.mixer.music.get_busy():		# bij pause is busy == 0
		pygame.mixer.music.pause()
		key = 2
		print('Pause key: ',key)
		sense.set_pixels(image3)
		
	else:									# van pause naar play mode
		pygame.mixer.music.unpause()
		key = 1
		sense.set_pixels(image1)
		print('Unpause key: ',key)
		displaymp3()						# display song
		
        
        
image1 = [                  # Play >
e,e,g,e,e,e,e,e,
e,e,e,g,e,e,e,e,
e,e,e,e,g,e,e,e,
e,e,e,e,e,g,e,e,
e,e,e,e,g,e,e,e,
e,e,e,g,e,e,e,e,
e,e,g,e,e,e,e,e,
e,e,e,e,e,e,e,e
]

image2 = [                   # Stop
e,e,e,e,e,e,e,e,
e,r,r,r,r,r,r,e,
e,r,e,e,e,e,r,e,
e,r,e,e,e,e,r,e,
e,r,e,e,e,e,r,e,
e,r,e,e,e,e,r,e,
e,r,r,r,r,r,r,e,
e,e,e,e,e,e,e,e
]

image3 = [                  # Pause ||
e,e,e,e,e,e,e,e,
e,e,b,e,e,b,e,e,
e,e,b,e,e,b,e,e,
e,e,b,e,e,b,e,e,
e,e,b,e,e,b,e,e,
e,e,b,e,e,b,e,e,
e,e,b,e,e,b,e,e,
e,e,e,e,e,e,e,e
] 

image4 = [                  # Volume +
e,e,e,e,e,e,e,e,
e,e,e,w,w,e,e,e,
e,e,e,w,w,e,e,e,
e,w,w,w,w,w,w,e,
e,w,w,w,w,w,w,e,
e,e,e,w,w,e,e,e,
e,e,e,w,w,e,e,e,
e,e,e,e,e,e,e,e
]

image5 = [                  # Volume -
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,w,w,w,w,w,w,e,
e,w,w,w,w,w,w,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e
] 

image6 = [                   # Startup 1
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,r,r,e,e,e,
e,e,e,r,r,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e
]

image7 = [                   # Startup 2
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,r,r,r,r,e,e,
e,e,r,e,e,r,e,e,
e,e,r,e,e,r,e,e,
e,e,r,r,r,r,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e
]

image8 = [                   # Startup 3
e,e,e,e,e,e,e,e,
e,r,r,r,r,r,r,e,
e,r,e,e,e,e,r,e,
e,r,e,e,e,e,r,e,
e,r,e,e,e,e,r,e,
e,r,e,e,e,e,r,e,
e,r,r,r,r,r,r,e,
e,e,e,e,e,e,e,e
]

image9 = [                   # Startup 4
r,r,r,r,r,r,r,r,
r,e,e,e,e,e,e,r,
r,e,e,e,e,e,e,r,
r,e,e,e,e,e,e,r,
r,e,e,e,e,e,e,r,
r,e,e,e,e,e,e,r,
r,e,e,e,e,e,e,r,
r,r,r,r,r,r,r,r
]

  
#-----------------------------------------------------------------------

def checkstick():
	#global key
	for event in sense.stick.get_events():
		# Check if the joystick was pressed
		if event.action == "pressed":
			# Check which direction
			if event.direction == "up":			# Up arrow = Volume+
				volumeH()
				sense.set_pixels(image4)

			elif event.direction == "down":		# Down arrow = Volume-
				volumeL()
				sense.set_pixels(image5)

			elif event.direction == "left": 	# Left arrow = Stop
				stoptrack()
				sense.set_pixels(image2)

			elif event.direction == "right":	# Play / Next
				starttrack()
				sense.set_pixels(image1)

			elif event.direction == "middle":	# Pause / Play
				toggleMusic()
				
			time.sleep(0.5)
			sense.clear()

########################################################################
sense.clear()									# alle RGB leds uit
sense.set_pixels(image6)
time.sleep(0.5)
sense.set_pixels(image7)
time.sleep(0.5)
sense.set_pixels(image8)
time.sleep(0.5)
sense.set_pixels(image9)
time.sleep(1)
sense.set_pixels(image1)
time.sleep(1)
sense.clear()									# alle RGB leds uit
mp3check()										# hoeveel mp3 files?

starttrack()									# start eerste track
time.sleep(1)
key = 1											# play 

while True:
	
	checkstick()								# key 0-1-2 == Stop-Play-Pause
	if pygame.mixer.music.get_busy() != True and key == 1: 
		if len(mp3list) != 0:
			starttrack()
			print('Restart play')
		else:
			print ('Einde ')					# dit verloop nog niet correct
