import math

def calc_d(a, b, c):
    return b**2 - 4*a*c

def solve(a, b, c):
    d = calc_d(a, b, c)
    
    if d > 0:
        x1 = (-b + math.sqrt(d)) / (2 * a)
        x2 = (-b - math.sqrt(d)) / (2 * a)
        print("x1 =", x1)
        print("x2 =", x2)
    elif d == 0:
        x = -b / (2 * a)
        print("x =", x)
    else:
        print("Коренів немає")

print("Рівняння ax^2 + bx + c = 0")
a = float(input("Введіть a: "))
b = float(input("Введіть b: "))
c = float(input("Введіть c: "))

solve(a, b, c)