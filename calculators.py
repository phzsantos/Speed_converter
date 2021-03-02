import functions



def MpsToKmph():
	eMps = float(input('How much m/s do you wanna convert to km/h? '))

	vKmph = (eMps * 3.6)

	print(f'This is how much {eMps:5.2f} mps is in km/h: {vKmph:5.2f} km/h')
	

	functions.eBackToMenuOrExit()



def KmphToMps():
	eKmph = float(input('How much km/h do you wanna convert to m/s? '))

	vMps = (eKmph / 3.6)

	print(f'This is how much {eKmph:5.2f} km/h is in m/s: {vMps:5.2f} m/s')


	functions.eBackToMenuOrExit()



def MphToKmph():
	eMph = float(input('How much m/h do you wanna convert to km/h? '))

	vKmph = (eMph * 1.6)

	print(f'This is how much {eMph:5.2f} m/h is in km/h: {vKmph:5.2f} km/h')


	functions.eBackToMenuOrExit()



def KmphToMph():
	eKmph = float(input('How much km/h do you wanna convert to m/h? '))

	vMph = (eKmph / 1.6)

	print(f'This is how much {eKmph:5.2f} km/h is in m/h: {vMph:5.2f} m/h')


	functions.eBackToMenuOrExit()



def MpsToFPS():
	eMps = float(input('How much m/s do you wanna convert to FPS? '))

	vFps = (eMps * 3.281)

	print(f'This is how much {eMps:5.2f} m/s is in FPS: {vFps:5.2f} FPS')


	functions.eBackToMenuOrExit()



def FPSToMps():
	eFps = float(input('How much FPS do you wanna convert to m/s? '))

	vMps = (eFps / 3.281)

	print(f'This is how much {eFps:5.2f} FPS is in m/s: {vMps:5.2f} m/s')


	functions.eBackToMenuOrExit()



def KnotToKmph():
	eKnot = float(input('How much Knots do you wanna convert to km/h? '))

	vKmph = (eKnot * 1.852)

	print(f'This is how much {eKnot:5.2f} knots is in km/h: {vKmph:5.2f} km/h')


	functions.eBackToMenuOrExit()



def KmphToKnot():
	eKmph = float(input('How much km/h do you wanna convert to Knots? '))

	vKnot = (eKmph / 1.852)

	print(f'This is how much {eKmph:5.2f} km/h is in knots: {vKnot:5.2f} knots')


	functions.eBackToMenuOrExit()

