class Control:
    def __init__(self):
        self._tv = None
    
    def turnOn(self):
        self.tv.turnOn()
    def turnOff(self):
        self.tv.turnOff()

    def canalUp(self):
        self.tv.canalUp()
    def canalDown(self):
        self.tv.canalDown()

    def volumenUp(self):
        self.tv.volumenUp()
    def volumenDown(self):
        self.tv.volumenDown()

    def setCanal(self, num):
        self.tv.setCanal(num)
    def setVolumen(self, num):
        self.tv.setVolumen(num)

    def enlazar(self, tv):
        self.tv = tv
        self.tv.control = self

    def getTv(self):
        return self.tv
    def setTv(self, tv):
        self.tv = tv