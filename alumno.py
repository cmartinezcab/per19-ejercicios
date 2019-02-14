class Alumno():
    def __init__(self, matricula, nombre, nota1, nota2, nota3):
        self.matricula = matricula
        self.nombre = nombre
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3
    def get_info(self):
        return self.matricula, self.nombre
    def Calcular_Final(self):
        nota_final = (self.nota1 + self.nota2 + self.nota3)/3
        ap = a.Aprobar(nota_final)
        print(ap)
        return nota_final

    def Aprobar(self, nota_final):
        if nota_final >= 4.8:
            return 'El alumno esta aprobado!!!'
        else:
            return 'El alumno esta suspenso'

a = Alumno(526, 'Alex', 3,4,5)
print('El alumno cuya matricula es: ', a.matricula, ',se llama ', a.nombre, 'y su nota final es ', a.Calcular_Final())
