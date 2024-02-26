class TV:
    numTV = 0
    def __init__(self, marca, estado):
        self._marca = marca
        self.canal = 1
        self._precio = 500
        self. estado = estado
        self.volumen = 1
        self.control = None
        TV.numTV += 1
        

    def getMarca(self):
        return self._marca
    def setMarca(self, marca):
        self._marca = marca

    def getCanal(self):
        return self.canal
    def setCanal(self, num):
        if self.estado == True:
            if num > 0 and num <= 120:
                self.canal = num

    def getPrecio(self):
        return self._precio
    def setPrecio(self, num):
        self._precio = num

    def getVolumen(self):
        return self.volumen
    def setVolumen(self, num):
        if self.estado == True:
            if num >= 0 and num <= 7:
                self.volumen = num
    
    def getControl(self):
        return self.control
    def setControl(self, control):
        self.control = control

    @classmethod
    def getNumTV(cls):
        return cls.numTV
    @classmethod
    def setNumTV(cls, num):
        cls.numTV = num

    def turnOn(self):
        self.estado = True
    def turnOff(self):
        self.estado = False
    def getEstado(self):
        return self.estado
    
    def canalUp(self):
        if self.estado == True:
            if self.canal < 120:
                self.canal += 1
    def canalDown(self):
        if self.estado == True:
            if self.canal > 1:
                self.canal -= 1

    def volumenUp(self):
        if self.estado == True:
            if self.volumen < 7:
                self.volumen += 1
    def volumenDown(self):
        if self.estado == True:
            if self.volumen > 0:
                self.volumen -= 1

    