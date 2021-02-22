"""
This is a little project for starting to learn Python and Logic.
Start: 21/02/2021
Name: Paulo Henrique
Country: Brazil
"""

#--------------------------------------Import Stage--------------------------------------#

import os



#--------------------------------------Menu--------------------------------------#

os.system('clear')

print('MENU')

print('\n1 - m/s to km/h')

print('\n2 - km/h to m/s')

print('\n3 - m/h to km/h')

print('\n4 - km/h to m/h')

print('\n5 - m/s to fps')

print('\n6 - fps to m/s')

eWhichOneConversion = int(input('\nSelect from 1 - 6: '))



os.system('clear')



#--------------------------------------m/s--------------------------------------#

if eWhichOneConversion == 1:
	eMps = float(input('How much m/s do you wanna convert to km/h? '))

	vKmph = (eMps * 3.6)

	print(f'This is how much {eMps:5.2f} mps is in km/h: {vKmph:5.2f}')

	
	eBackToMenuOrExit = input('\nDo you wanna [E]exit or [M]back to Menu? ').upper()

	if eBackToMenuOrExit == 'M':
		os.system('python3 Converter.py')

	else:
		os.system('clear')



elif eWhichOneConversion == 2:
	eKmph = float(input('How much km/h do you wanna convert to m/s? '))

	vMps = (eKmph / 3.6)

	print(f'This is how much {eKmph:5.2f} km/h is in m/s: {vMps:5.2f} m/s')


	eBackToMenuOrExit = input('\nDo you wanna [E]exit or [M]back to Menu? ').upper()

	if eBackToMenuOrExit == 'M':
		os.system('python3 Converter.py')

	else:
		os.system('clear')



#--------------------------------------m/h--------------------------------------#

elif eWhichOneConversion == 3:
	eMph = float(input('How much m/h do you wanna convert to km/h? '))

	eKmph = (eMph * 1.6)

	print(f'This is how much {eMph:5.2f} m/h is in km/h: {eKmph:5.2f} km/h')


	eBackToMenuOrExit = input('\nDo you wanna [E]exit or [M]back to Menu? ').upper()

	if eBackToMenuOrExit == 'M':
		os.system('python3 Converter.py')

	else:
		os.system('clear')
