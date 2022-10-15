from deportista import Deportista
from persona import Persona

class Futbolista(Persona,Deportista):
    listaFutbolistas=[]
    def __init__(self, nombre=None, edad=0, altura=None, sexo=None,añosPracticando=0,
        golesMarcados=0,tarjetasRojas=0,piernaHabil=None):
        Persona.__init__(self,nombre, edad, altura, sexo)
        Deportista.__init__(self,"Futbol",añosPracticando)
        self._golesMarcados=golesMarcados
        self._tarjetasRojas=tarjetasRojas
        self._piernaHabil=piernaHabil
        Futbolista.listaFutbolistas.append(self)

    def getGolesMarcados(self):
        return self._golesMarcados

    def setGolesMarcados(self,n):
        self._golesMarcados=n

    def getTarjetasRojas(self):
        return self._tarjetasRojas

    def setTarjetasRojas(self,n):
        self._tarjetasRojas=n

    def getPiernaHabil(self):
        return self._piernaHabil

    def setPiernaHabil(self,n):
        self._piernaHabil=n

    def __str__(self):
        return "Mi nombre es %s soy profesional en el deporte %s Tengo %s años de edad y llevo %s años en el deporte"%(self.getNombre(),self.getDeporte(),self.getEdad(),self.getAñosPracticando)