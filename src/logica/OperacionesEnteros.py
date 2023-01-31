class OperacionesEnteros:
    def __init__(self, numeros):
        self.__numeros = numeros

    def calcularMCD(self):
        if len(self.__numeros) == 2 :
            return self.MCD(self.__numeros[0], self.__numeros[1])
        elif len(self.__numeros) == 3 :
            mcd = self.MCD(self.__numeros[0], self.__numeros[1])
            mcd = self.MCD(mcd, self.__numeros[2])

            return mcd
        else:
            return 0

    def MCD(self, numero1, numero2):
        temporal = 0
        while numero2 != 0:
            temporal = numero2
            numero2 = numero1 % numero2
            numero1 = temporal
        return numero1
