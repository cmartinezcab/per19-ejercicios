class NIF():
    def __init__(self, num1, num2, num3, num4, num5, num6, num7, num8):
        self.num1 = num1
        self.num2 = num2
        self.num3 = num3
        self.num4 = num4
        self.num5 = num5
        self.num6 = num6
        self.num7 = num7
        self.num8 = num8
    def Calcular_Letra(self):
        if self.num1 == 1 or self.num1== 3:
            return 'A'
        if self.num1 == 2 or self.num1== 4:
            return 'M'
        if self.num1 == 5 or self.num1== 7:
            return 'K'
        if self.num1 == 6 or self.num1== 8 or self.num1==9:
            return 'L'
n=NIF(4,5,6,7,8,2,1,9)
print('El NIF es: ',n.num1, n.num2, n.num3, n.num4, n.num5, n.num6, n.num7, n.num8, n.Calcular_Letra())
