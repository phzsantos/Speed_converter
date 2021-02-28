"""
This is a little project for starting to learn Python and Logic.
Start: 21/02/2021
Name: Paulo Henrique
Country: Brazil
"""

#--------------------------------------Import Stage--------------------------------------#

import functions



#--------------------------------------Menu--------------------------------------#

functions.clear()

print('MENU')

print('\n1 - m/s to km/h')

print('\n2 - km/h to m/s')

print('\n3 - m/h to km/h')

print('\n4 - km/h to m/h')

print('\n5 - m/s to fps')

print('\n6 - fps to m/s')

print('\n7 - knot to km/h')

print('\n8 - km/h to knot')

eWhichOneConversion = int(input('\nSelect from 1 - 8 or [0] to exit: '))


functions.clear()



#--------------------------------------m/s--------------------------------------#

if eWhichOneConversion == 1:
	eMps = float(input('How much m/s do you wanna convert to km/h? '))

	vKmph = (eMps * 3.6)

	print(f'This is how much {eMps:5.2f} mps is in km/h: {vKmph:5.2f} km/h')
	

	functions.eBackToMenuOrExit()



elif eWhichOneConversion == 2:
	eKmph = float(input('How much km/h do you wanna convert to m/s? '))

	vMps = (eKmph / 3.6)

	print(f'This is how much {eKmph:5.2f} km/h is in m/s: {vMps:5.2f} m/s')


	functions.eBackToMenuOrExit()



#--------------------------------------m/h--------------------------------------#

elif eWhichOneConversion == 3:
	eMph = float(input('How much m/h do you wanna convert to km/h? '))

	vKmph = (eMph * 1.6)

	print(f'This is how much {eMph:5.2f} m/h is in km/h: {vKmph:5.2f} km/h')


	functions.eBackToMenuOrExit()



elif eWhichOneConversion == 4:
	eKmph = float(input('How much km/h do you wanna convert to m/h? '))

	vMph = (eKmph / 1.6)

	print(f'This is how much {eKmph:5.2f} km/h is in m/h: {vMph:5.2f} m/h')


	functions.eBackToMenuOrExit()



#--------------------------------------Fps--------------------------------------#

elif eWhichOneConversion == 5:
	eMps = float(input('How much m/s do you wanna convert to FPS? '))

	vFps = (eMps * 3.2)

	print(f'This is how much {eMps:5.2f} m/s is in FPS: {vFps:5.2f} FPS')


	functions.eBackToMenuOrExit()



elif eWhichOneConversion == 6:
	eFps = float(input('How much FPS do you wanna convert to m/s? '))

	vMps = (eFps / 3.2)

	print(f'This is how much {eFps:5.2f} FPS is in m/s: {vMps:5.2f} m/s')


	functions.eBackToMenuOrExit()



#--------------------------------------knot--------------------------------------#

elif eWhichOneConversion == 7:
	eKnot = float(input('How much Knots do you wanna convert to km/h? '))

	vKmph = (eKnot * 1.852)

	print(f'This is how much {eKnot:5.2f} knots is in km/h: {vKmph:5.2f} km/h')


	functions.eBackToMenuOrExit()



elif eWhichOneConversion == 8:
	eKmph = float(input('How much km/h do you wanna convert to Knots? '))

	vKnot = (eKmph / 1.852)

	print(f'This is how much {eKmph:5.2f} km/h is in knots: {vKnot:5.2f} knots')


	functions.eBackToMenuOrExit()



#--------------------------------------End--------------------------------------#

elif eWhichOneConversion == 0:
	functions.clear()



else:
	print('You choose an option that not exists. You can try again.')


	functions.eBackToMenuOrExit()
		