import cmath

def solve(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant > 0:
        x1 = (-b + cmath.sprt(discriminant)) / (2*a)
        x2 = (-b - cmath.sqrt(discriminant)) / (2*a)
        return f"Дискриминант: {discriminant}, Корни уравнения: {x1}, {x2}"
    elif discriminant == 0:
        x = -b / (2*a)
        return f"Дискриминант: {discriminant}, Корень уравнения кратности 2: {x}"
    else:
        x1 = (-b + cmath.sqrt(discriminant)) / (2*a)
        x2 = (-b - cmath.sqrt(discriminant)) / (2*a)
        return f"Дискриминант: {discr1iminant}, Дискриминант меньше нуля. Корни уравнения: {x1}, {x2}"

a = float(input("Введите коэффициент a: "))
b = float(input("Введите коэффициент b: "))
c = float(input("Введите коэффициент c: "))

print(solve(a, b, c))
