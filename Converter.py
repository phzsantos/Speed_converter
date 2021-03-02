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

functions.Menu()

eWhichOneConversion = int(input('\nSelect from 0 - 8: '))

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


		