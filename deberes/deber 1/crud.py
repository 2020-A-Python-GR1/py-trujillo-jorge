class Superhero:
    real_name:""
    superhero_name:""
    height=None
    apparence_year:1900
    status:True
    def __init__(self,real_name,superhero_name, height, apparence_year, status):
        self.real_name = real_name
        self.superhero_name = superhero_name
        self.height = height
        self.apparence_year = apparence_year
        self.status = status

    def __str__(self):
        return f"Nombre real: {self.real_name}\nAlterego: {self.superhero_name}\nAltura: {self.height}\nAnio de aparición: {self.apparence_year}\nEstatus: {self.status}"

class Comic_Volume:
    volume_name:""
    pubish_year: 1900

    pass
supernam = Superhero("Superman", 'Clarck Kent', 1.86, 1983, True)
print(supernam)