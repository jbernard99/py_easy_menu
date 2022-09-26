from os import system, name

class Menu:

	def __init__(self):
		self.colors = {
			'purple': '\033[95m',
			'light_blue': '\033[94m',
			'cyan': '\033[96m',
			'green': '\033[92m',
			'orange': '\033[93m',
			'red': '\033[91m',
			'endc': '\033[0m',
			'bold': '\033[1m',
			'unederline': '\033[4m'
		}

	def set_header(self, header):
		self.header = header

	def set_footer(self, footer):
		self.footer = footer

	def clear(self):
		if name == 'nt':
			system('cls')
		else:
			system('clear')

	def print_error(self, error):
		self.clear()
		print(self.colors['bold'] + self.colors['red'] + "ERROR: " + self.colors['endc'] + error)

	def print_menu(self, txt, type, choice_list=[]):
		self.clear()
		print(self.header)
		print(self.colors['cyan'] + txt + "\n\n")
		i = 1
		for choice in choice_list:
			print(self.colors['cyan'] + str(i) + " - " + self.colors['green'] + str(choice))
			i += 1
		print("\n\n")
		print(self.footer)
		choice = self.get_input(type, end=len(choice_list))
		return choice

	def print_transition(self, txt):
		self.clear()
		print(self.header)
		print(f"\n\n\n{txt}\n")
		print(self.footer)
		input("Press enter . . .")

	def get_input(self, rule, end=0):
		uinput = input(" : ")
		if rule == "int" and self.verif_int_input(uinput, end):
			return int(uinput)
		elif rule == "str" and self.verif_str_input(uinput):
			return uinput
		elif rule == "float" and self.verif_float_input(uinput):
			return float(uinput)
		else:
			self.print_error("Wrong input!")

	def verif_int_input(self, uinput, end):
		if uinput.isdigit():
			if int(uinput) <= end:
				return True
		return False

	def verif_str_input(self, uinput):
		if uinput.isalnum():
			return True
		return False

	def verif_float_input(self, uinput):
		if uinput.isnumeric():
			return True
		return False
