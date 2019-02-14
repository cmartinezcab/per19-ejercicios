
class Defecto():
    def __init__(self):
        pass
    def Comprobar_Fecha():
        print('No hay fecha')
    def Modificar_Fecha():
        print('No hay fecha')
class Fecha():
    def __init__(self, dia, mes, año):
        self.dia = dia
        self.mes = mes
        self.año = año
    def Comprobar_Fecha(self):
        if self.dia != 14 or self.mes != 'febrero' or self.año != 2019:
            return 'La fecha no es correcta'
        else:
            return 'La fecha es correcta!!'
    def Modificar_Fecha(self):
        x = self.dia
        return x + 1

F=Fecha(14,'febrero',2019)
print('Hoy es dia:', F.dia, F.mes, F.año, 'y mañana sera: ', F.Modificar_Fecha())
print(F.Comprobar_Fecha())
