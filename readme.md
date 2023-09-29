# - py_menu
### Installation:
Download and move menu.py in your working directory.

Import in your python project using:
```python
from menu import Menu
```

### Usage:
```python
from menu import Menu

menu = Menu()
menu.set_header("This will be the menu header")
menu.set_footer("This will be the menu footer")
result = menu.print_menu("Menu question", # The text at the top of the menu
	"int", # The type of answer you want from the user ("str", "int", "float")
	["Choice1", "Choice2", "Choice3"]) # The choices the user will have (Enumerated)
print(result) # Result will contain the verified user's input
```