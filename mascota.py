class Mascota:
    def __init__(self, nombre, edad, especie):
        self.nombre = nombre
        self.edad = edad
        self.especie = especie

    def __str__(self):
        return f"{self.nombre} es un(a) {self.especie} de {self.edad} años."

    def hacer_sonido(self):
        raise NotImplementedError("Este método debe ser implementado por las subclases.")