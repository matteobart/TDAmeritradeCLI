import argparse
import commandEnum

class Parser:

	def __init__(self):
		commands = commandEnum.Commands.list()

		self.parser = argparse.ArgumentParser(exit_on_error=False)
		self.parser.add_argument("command", choices=commands)
		self.parser.add_argument("--info", action="store_true", help="Will give more information on a function. Supported by all commands.")
		self.parser.add_argument("--daysFrom", "-df", nargs=1, type=int, help="The number of days before. Supported by washsales, ")
		# add/update optional parameters here (step 3)

	def parse(self, string):
		try:
			args = self.parser.parse_args(string.split(" "))
			return args

		# most errors come here
		except argparse.ArgumentError as error:
			print(error)
			return None

		# given a bad type, expected an int but got a string
		except argparse.ArgumentTypeError as error:
			return None

		# missing the command, but given an optional parameter
		except:
			return None
