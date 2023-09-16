class Employee:
    def __init__(self, name, family, salary):
        self.name = name
        self.family = family
        self.salary = salary

    def give_raise(self, raise_const='5000'):
        self.salary += int(raise_const)
        return self.salary


Daniil = Employee('Daniil', 'Moscow', 100000)
