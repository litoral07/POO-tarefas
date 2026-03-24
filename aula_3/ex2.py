class triangulo:
    def __init__(self) -> None:
        self.b = 0
        self.h = 0
    def calc_area(self):
        return self.b * self.h / 2    
x = triangulo()
print(x.b, x.h)
x.b = float(input("informe a base do triangulo\n" ))
x.h = float(input("informe a altura do triangulo\n"))
print(x.b, x.h)
a = x.calc_area()
print(f"a area do triagulo é {a:.2f}")

y = triangulo()
print(y.b, y.h)
y.b = float(input("informe a base do segundo triangulo\n"))
y.h = float(input("informe a altura do segundo triangulo\n"))
print(y.b, y.h)
a = y.calc_area()
print(f"a area do triagulo é {a:.2f}")

