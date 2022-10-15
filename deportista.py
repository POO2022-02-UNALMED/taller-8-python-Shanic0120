class Deportista():
    def __init__(self,deporte=None,añosPracticando=0):
        self._deporte=deporte
        self._añosPracticando=añosPracticando

    
    def getDeporte(self):
        return self._deporte

    def setDeporte(self,n):
        self._deporte=n

    def getAñosPracticando(self):
        return self._añosPracticando

    def setAñosPracticando(self,n):
        self._añosPracticando=n