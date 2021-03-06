
import os
import calculators



#--------------------------------------Menu--------------------------------------#

def Menu():
	clear()

	print("""MENU
		\n0 - Exit
		\n1 - m/s to km/h
		\n2 - km/h to m/s
		\n3 - m/h to km/h
		\n4 - km/h to m/h
		\n5 - m/s to fps
		\n6 - fps to m/s
		\n7 - knot to km/h
		\n8 - km/h to knot
		""")



#--------------------------------------eWichOneConversion--------------------------------------#

FunctionsCalculators = [calculators.MpsToKmph, calculators.KmphToMps, calculators.MphToKmph, calculators.KmphToMph, calculators.MpsToFPS, calculators.FPSToMps, calculators.KnotToKmph, calculators.KmphToKnot]
 
def eWhichOneConversion(question):
	FunctionsCalculators[question+1]()
	clear()




#--------------------------------------Clear--------------------------------------#

def clear():
	os.system('clear')



#--------------------------------------eBackToMenu--------------------------------------#

def eBackToMenuOrExit():
	eBackToMenuOrExit = input('\nDo you wanna [E]exit or [B]back to Menu? ').upper()

	if eBackToMenuOrExit == 'B':
		os.system('python3 Converter.py')

	else:
		clear()



#--------------------------------------MissClick--------------------------------------#

def MissClick():
	print('You choose an option that not exists. You can try again.')


	eBackToMenuOrExit()



#--------------------------------------ValueError--------------------------------------#




"""def IfError(answer):
	try: 




def menu(input):
	try:
		calculators.input

	except ValueError as erro:
		print('Você usou numeros com ",", o programa aceita apenas numeros com "."')
		MissClick()
"""

	
		

