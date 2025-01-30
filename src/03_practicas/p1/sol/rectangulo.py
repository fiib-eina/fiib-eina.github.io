print("Introduzca x1:")
x1 = float(input())
print("Introduzca y1:")
y1 = float(input())
print("Introduzca x2:")
x2 = float(input())
print("Introduzca y2:")
y2 = float(input())

base = abs(x2 - x1)
altura = abs(y2 - y1)

area = base * altura
perimetro = 2 * (base + altura)

print("\nEl área del rectángulo es:")
print(area)
print("\nEl perímetro del rectángulo es:")
print(perimetro)


