from consolemenu import *
from consolemenu.items import *
import files


file = files.Files("./lolo.txt")
data = file.to_json()

menu = ConsoleMenu("Superheroes", "Python 2020")
menu_search = FunctionItem("Search",input ,file.show_sup(input,data) )
menu.append_item(menu_search)

menu.show()