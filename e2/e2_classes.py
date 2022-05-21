import numpy as np

GENDER = {
    'M': 'male', 'F': 'female'
}


def ask_for_details(property):
    value = input(f"Enter {property}: ")
    return value


class Person:
    imc_types = {
        "-1": 'None',
        "0": 'Underweight',
        "1": 'Overweight'
    }

    def _generate_dni(self):
        return np.random.randint(10**8, 10**9)

    def __init__(self, name: str = '', age: int = 0, gender='M', weight: float = 1, height: float = 1):
        try:
            self.name = name
            self.age = int(age)
            self.weight = float(weight)
            self.height = float(height)
            self.dni = self._generate_dni()

            if gender not in GENDER:
                raise ValueError

            self.gender = gender

        except ValueError:
            print('Unprocessable input')

    def __str__(self) -> str:
        return f"Name: {self.name} Age: {self.age} Height/Weight: {self.height}/{self.weight}"

    def findIMC(self):
        imc = self.weight / (self.height ** 2)

        if imc > 20 or imc < 26:
            return 0

        if imc > 25:
            return 1

        return -1

    def is_old_enough(self):
        return self.age >= 18

    def checkGender(self, gender_input):
        if gender_input not in GENDER.keys():
            # Make default gender to be male
            self.gender = 'M'

    def define_imc(self):
        imc = str(self.findIMC())
        if imc in self.imc_types:
            return self.imc_types[imc]
