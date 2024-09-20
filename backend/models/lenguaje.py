class Lenguaje:
    def __init__(self, nombre, popularidad, uso, usuarios, logo):
        self.nombre = nombre
        self.popularidad = popularidad
        self.uso = uso
        self.usuarios = usuarios
        self.logo = logo
    
    def getNombre(self):
        return self.nombre
    
    def getPopularidad(self):
        return self.popularidad
    
    def getUso(self):
        return self.uso
    
    def getUsuarios(self):
        return self.usuarios
    
    def getLogo(self):
        return self.logo
    
    def setNombre(self, nombre):
        self.nombre = nombre
    
    def setPopularidad(self, popularidad):
        self.popularidad = popularidad

    def setUso(self, uso):
        self.uso = uso

    def setUsuarios(self, usuarios):
        self.usuarios = usuarios

    def setLogo(self, logo):
        self.logo = logo