def strategy(history, memory):

	offsetAverage = 0.01
	cooperateDetection = 1.1


	numberOfRound = history.shape[1]
#	print()
#	print("round number: " + str(numberOfRound))

	x = 0
	averageOfOpponent = 0
	dOfOpponent = 0
	cOfOpponent = 0

	while x < numberOfRound:									#create statistics of opponent
		#print (history[1, -x])
		averageOfOpponent += history[1, -x]

		if history[1, -x] == 0:
			dOfOpponent += 1
		else:
			cOfOpponent += 1

		x += 1

	if numberOfRound > 0:
		averageOfOpponent = averageOfOpponent / numberOfRound

	
	choice = round(averageOfOpponent + offsetAverage)			#choice is average of opponent history. offset by 0.01 so choice is more likely to cooperate, dont know why, seems to work

	if cOfOpponent > (cooperateDetection * dOfOpponent):		#except opponent is 1.1x more likely to cooperate --> defect
		choice = 0

#	print("average: " + str(averageOfOpponent))
#	print("dOfOpponent: " + str(dOfOpponent))
#	print("cOfOpponent: " + str(cOfOpponent))
#	print("choice: " + str(choice))
	
	return choice, None
