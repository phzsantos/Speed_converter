"""
This is a little project for starting to learn Python and Logic.
Start: 21/02/2021
Name: Paulo Henrique
Country: Brazil
"""

#--------------------------------------Import Stage--------------------------------------#

import functions
import calculators



#--------------------------------------Menu--------------------------------------#

functions.clear()

print('MENU')

print('\n0 - Exit')

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
	calculators.MpsToKmph()



elif eWhichOneConversion == 2:
	calculators.KmphToMps()



#--------------------------------------m/h--------------------------------------#

elif eWhichOneConversion == 3:
	calculators.MphToKmph()



elif eWhichOneConversion == 4:
	calculators.KmphToMph()



#--------------------------------------Fps--------------------------------------#

elif eWhichOneConversion == 5:
	calculators.MpsToFPS()



elif eWhichOneConversion == 6:
	calculators.FPSToMps()



#--------------------------------------knot--------------------------------------#

elif eWhichOneConversion == 7:
	calculators.KnotToKmph()



elif eWhichOneConversion == 8:
	calculators.KmphToKnot()



#--------------------------------------End--------------------------------------#

elif eWhichOneConversion == 0:
	functions.clear()



else:
	functions.MissClick()
		