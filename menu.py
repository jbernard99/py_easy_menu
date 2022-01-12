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

	def clear(self):
		 if name == 'nt':
		 	system('cls')
		 else:
		 	system('clear')

	def print_error(self, error):
		self.clear()
		print(self.colors['bold'] + self.colors['red'] + "ERROR: " + self.colors['endc'] + error)

	def print_menu(self, txt, choice_list=["\n"]):
		self.clear()
		print(self.colors['cyan'] + txt + "\n\n")
		i = 1
		for choice in choice_list:
			print(self.colors['cyan'] + str(i) + " - " + self.colors['green'] + choice)
			i += 1
		print("\n\n")
		choice = self.get_input("int", end=len(choice_list))
		return choice

	def get_input(self, rule , end=0):
		uinput = input(" : ")
		if rule == "int":
			if self.verif_nmbr(uinput, rule, end):
				return int(uinput)
			else:
				self.print_error("Wrong input!")
				return False

	def verif_nmbr(self, uinput, rule, end):
		if rule == "int":
			if ui-nput.isdigit():
				if int(uinput) <= end:
					return True
		else:
			self.print_error("Wrong input!")
			return False

	def print_result(self, result_title, result_list):
		self.clear()
		print(self.colors['cyan'] + "Results for" + self.colors['bold'] + result_title + "\n")
		i = 1
		for result in result_list:
			print(self.colors['cyan'] + str(i) + " - " + self.colors['green'] + str(result))
			i += 1
		input("Press enter to continue...")