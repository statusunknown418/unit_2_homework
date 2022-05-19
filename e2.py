GENDER = {
    'M': 'male', 'F': 'female'
}


class Person:
    imc_normal_range = range(20, 26)
    imc_types = {
        '-1': 'None',
        '0': 'Underweight',
        '1': 'Overweight'
    }

    def __init__(self, name: str, age: int, dni: str | int, gender: GENDER, weight: float, height: int):
        self.name = name
        self.age = age
        self.dni = dni
        self.gender = gender
        self.weight = weight
        self.height = height

    def findIMC(self):
        imc = self.weight / (self.height ** 2)

        if imc in self.imc_normal_range:
            return 0

        if imc > 25:
            return 1

        return -1
