import parse
import commandEnum
import commandRouter

def main_loop():
	parser = parse.Parser()

	print("Welcome to TD Ameritrade (unofficial) CLI")
	while(True):
		rawInput = input("> ")
		args = parser.parse(rawInput)
		# ensure we have a value
		if args is None: 
			continue

		if args.command == commandEnum.Commands.EXIT.value or args.command == commandEnum.Commands.QUIT.value:
			print("Goodbye")
			return
		else:
			commandRouter.runCommand(args)




if __name__ == "__main__":
	main_loop()