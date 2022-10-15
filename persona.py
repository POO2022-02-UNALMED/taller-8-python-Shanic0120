class Persona():
    def __init__(self,nombre=None,edad=0,altura=None,sexo=None):
        self._nombre=nombre
        self._edad=edad
        self._altura=altura
        self._sexo=sexo
    
    def getNombre(self):
        return self._nombre

    def setNombre(self,n):
        self._nombre=n

    def getEdad(self):
        return self._edad

    def setEdad(self,n):
        self._edad=n

    def getAltura(self):
        return self._altura

    def setAltura(self,n):
        self._altura=n

    def getSexo(self):
        return self._sexo

    def setSexo(self,n):
        self._sexo=n