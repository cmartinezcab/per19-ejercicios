class Libro():
    def __init__(self, prestamo, devolucion):
        self.prestamo= prestamo
        self.devolucion = devolucion
    def dame_info(self):
        return self.prestamo, self.devolucion
l= Libro('3','21')
print('Hizo un prestamo de', l.prestamo, 'libros, y la fecha de devolucion es dentro de', l.devolucion, 'dias')
