from commandEnum import Commands

def runCommand(args):
	if (args.command == Commands.WASHSALES.value):
		if (args.info):
			print("The washsale command allows you to see any washsales")
			print("There are no optional parameters")
		else: 
			print("run the washsale function")
	elif (args.command == Commands.HELP.value):
		if (args.info):
			pass	
		print("run the help function")
	# add more commands here (step 2)
	else:
		print(args.command + " has not been implemented yet")
		
