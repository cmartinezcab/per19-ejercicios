class Cuenta():
    def __init__(self, ingreso, reintegro, transferencia):
        self.ingreso = ingreso
        self.reintegro = reintegro
        self.transferencia = transferencia
    def get_integro(self):
        return self.ingreso
    def get_reintegro(self):
        return self.reintegro
    def get_transferencia(self):
        return self.transferencia

c= Cuenta('70', '20', '50')
print('Ingreso', c.get_integro(), 'hizo un reintegro de', c.get_reintegro(),'y una transferencia de', c.get_transferencia())
