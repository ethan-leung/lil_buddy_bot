Welcome to our DandyHacks Project, UR Lil Buddy Bot (Ethan Leung, Kyle Chang, James Chen)

UR Lil Buddy Bot has multiple functions which have all been implemented for the sole purpose of automating the menial and mundane tasks of every day life, so that its user could fully focus on their work, while maintaining good physical and mental health.

These functions currently include:
- a discord bot that automatically sends you a list of the open dining halls on the University of Rochester campus at common meal times
	- the bot will prompt you to choose one of these open dining halls
	- and the bot will then output the menu of that specific dining halls
- a program (study_place.py) that will output a list of nearby study areas
	- allows for mental and environmental refresh whenever the user feels particularly tired from focused work
	- uses user current location to webscrape Yelp for nearby study locations
	- takes in user current location to webscrape weather to determine whether it is safe to go outside or not
- a program (close.py) that, with permission of the user, accesses the webcam to constantly make sure the user is not too close to the screen
	- if the distance gets too close for an extended period of time, the program will read that as a sign of bad posture and it will output a message telling you to fix your posture
- a program (night_light.py) that will gradually place a blue light filter on the user's screen at 9 pm
	- scientifically proven to decrease eye strain to encourage productivity in more healthy times
	- utilizes PowerShell through Python to change the system settings on a Windows computer
- a program (time.py) that tracks the time spent on different windows applications as well as on Google Chrome tabs
	- program provides an end of the day report of time spent on various tabs
	- the program also will warn you when you're on unproductive websites for too long such as YouTube, Twitch, or Discord

How to run:
- dining hall menus - use the link provided to join our discord and gain access to our discord bot, more information will be provided.
- study areas - study_places.exe or study_places.py
- blue light filter - night_light.exe or night_light.py
- time tracker - time.exe or time.py
- screen closeness - close.py (close.exe was too big to submit, but will be on our GitHub)
