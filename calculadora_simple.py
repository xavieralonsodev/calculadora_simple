'''
calculadora_simple.py
Autor: xavier
Decripcion: Calculadora básica en Python
Fecha: 28/10/2025
'''

def sumar(a,b):
    return a + b

def restar(a,b):
    return a - b

def multiplicar(a,b):
    return a * b

def division(a,b):
    if b ==0:
        return "Error:division entre cero"
    else:
        return a / b

def potencia(a,b):
    return a ** b
    
    
def main():
    
    print('Calculador simple')
    x = float(input('Introduce el primer numero:'))
    y = float(input('Introduce el segundo numero:'))
    
    print(f'Suma: {sumar(x,y)}')
    print(f'Resta: {restar(x,y)}')
    print(f'Multiplicación: {multiplicar(x,y)}')
    print(f'División: {division(x,y)}')
    print(f'Potencia: {potencia(x,y)}')
    print('Cambio hecho a pelo en github')

# main

if __name__ == 'main':
    main()
