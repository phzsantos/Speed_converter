import os

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