def discriminant(a, b, c):
    return b**2 - 4*a*c

a = float(input("Введіть a: "))
b = float(input("Введіть b: "))
c = float(input("Введіть c: "))

D = discriminant(a, b, c)
print("Дискримінант =", D)
