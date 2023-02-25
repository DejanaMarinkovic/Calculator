"""
Vežba 1:

Koristeći primer dekorator funkcije koja omogućava izbor matematičke operacije, potrebno je realizovati kalkulator.
Ovaj kalkulator treba da poseduje četiri operacije (sabiranje, oduzimanje, deljenje i množenje). Potrebno je omogućiti
korisniku da unese operaciju (+-*/) i da unese dva broja.

"""


class Calculator:
    def __init__(self):
        self.operation = input("Unesi operaciju (+, -, *, /): ")
        self.num1 = int(input( "Unesi prvi broj: "))
        self.num2 = int(input( "Unesi drugi broj: "))

    def decorator(self, func):
        def wrapper(a, b):
            if self.operation == "+":
                return a + b
            elif self.operation == "-":
                return a - b
            elif self.operation == "*":
                return a * b
            elif self.operation == "/":
                return a / b
            return func(a, b)

        return wrapper

    def calculate(self):
        decorated_func = self.decorator(lambda a, b: None)
        result = decorated_func(self.num1, self.num2)
        print ( "Rezultat:", result)


# Create a Calculator instance and perform the calculation
calculator = Calculator()
calculator.calculate()











