def mcd(a, b):
    r = a % b if b !=0 else a
    return b if r == 0 else mcd(b, r)

numeros = float( input ("Ingrese la cantidad de numeros a calcular el MCD: "))

def f(numbers):
    if len(numbers) >=2:
        r = mcd(numbers[0], numbers[1])
        for n in numbers[2:]:
            r = mcd(r, n)
        return r
numbers = []
i = 1
while i <= numeros:
    try:
        num = int(input("Ingrese el {}° numero : ".format(i)))
        numbers.append(num)
        i += 1
    except ValueError as e:
        print("El valor ingresado no es un numero valido")

result = f(numbers)
print('El maximo comun divisor es: ')
print(result)
