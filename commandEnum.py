from enum import Enum
class Commands(Enum):
	WASHSALES = "washsales"
	QUIT="quit"
	EXIT="exit"
	HELP="help"
	# add more commands here (step 1)

	@staticmethod
	def list():
		return list(map(lambda c: c.value, Commands))