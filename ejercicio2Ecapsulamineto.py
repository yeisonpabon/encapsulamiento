class Circulo:
    def __init__(self,radio):
        self.__radio = radio
        self.__pi = 3.1415

    def calcularPerimetro(self):
        return 2*self.__pi*self.__radio
    
    def calculaArea(self):
        return self.__pi*self.__radio**2
    

c1 = Circulo(2.5)
print(c1.calculaArea())
print(c1.calcularPerimetro())
print(f'la constante PI es {c1.__pi}')