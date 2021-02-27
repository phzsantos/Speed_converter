import os

def clear():
	os.system('clear')



def eBackToMenuOrExit():
	eBackToMenuOrExit = input('\nDo you wanna [E]exit or [B]back to Menu? ').upper()

	if eBackToMenuOrExit == 'B':
		os.system('python3 Converter.py')

	else:
		clear()