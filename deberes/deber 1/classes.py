class Superhero:
    real_name:""
    superhero_name:""
    height=None
    apparence_year:1900
    status:True
    comics = []
    def __init__(self,real_name="",superhero_name="", height=1.0, apparence_year=1900, status= True, comics=[]):
        self.real_name = real_name
        self.superhero_name = superhero_name
        self.height = height
        self.apparence_year = apparence_year
        self.status = status
        self.comics = comics
    
    def __str__(self):
        return f"""
        Nombre real: {self.real_name}
        Alterego:{self.superhero_name}
        Altura:{self.height}
        Anio de aparición:{self.apparence_year}
        Estatus: {self.status}
        Comics: {self.comics}
        """

    def from_dict_to_superhero(self, arr_de_datos):
        return Superhero(arr_de_datos["real_name"],
        arr_de_datos["superhero_name"],
        arr_de_datos["height"],
        arr_de_datos["apparence_year"],
        arr_de_datos["status"],
        arr_de_datos["comics"])

    def from_sups_to_dict(self):
        return {self.superhero_name:{
            "real_name": self.real_name,
            "superhero_name":self.superhero_name,
            "height":self.height,
            "apparence_year":self.apparence_year,
            "status": self.status,
            "comics": self.comics
        }}

    def add_comic_serie(self, serie_name):
        self.comics.append(serie_name)


class Comic_Serie:
    serie_name:""
    pubish_year: 1900
    volumes: 0
    finalized:True
    writer: ""

    def __init__(self, serie_name="", pubish_year=1900, volumes=0, finalized= True, writer=""):
        self.serie_name = serie_name
        self.pubish_year=pubish_year
        self.volumes= volumes
        self.finalized = finalized
        self.writer= writer

    def __str__(self):
        return f"""
        Nombre: {self.serie_name}
        Anio de publicación:{self.pubish_year}
        Numero de comics:{self.volumes}
        Finalizado:{self.finalized}
        Escritor: {self.writer}
        """

    def from_dict_to_comicv(self, arr_de_datos):
        return Comic_Serie(arr_de_datos["serie_name"],
        arr_de_datos["publish_year"],
        arr_de_datos["volumes"],
        arr_de_datos["finalized"],
        arr_de_datos["writer"])

    def from_comicv_to_dict(self):
        return {self.serie_name:{
            "serie_name": self.serie_name,
            "publish_year":self.pubish_year,
            "volumes":self.volumes,
            "finalized":self.finalized,
            "writer": self.writer
        }}

