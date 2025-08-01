from mascota import Mascota

class Perro(Mascota):
    def __init__(self, nombre, edad, raza):
        super().__init__(nombre, edad, especie='Perro')
        self.raza = raza

    def hacer_sonido(self):
        print("Guau guau!")

    def __str__(self):
        return f"Perro: {self.nombre}, Edad: {self.edad}, Raza: {self.raza}"