
def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Error: No se puede dividir entre cero."
    return a / b

def calculadora():
    while True:
        print("\n--- Calculadora Básica ---")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        print("5. Salir")
        
        opcion = input("Selecciona una opción (1-5): ")
        
        if opcion == '5':
            print("¡Hasta luego!")
            break
            
        if opcion in ['1', '2', '3', '4']:
            try:
                num1 = int(input("Ingresa el primer número: "))
                num2 = int(input("Ingresa el segundo número: "))
            except ValueError:
                print("Error: Por favor, ingresa solo números válidos.")
                continue
            
            if opcion == '1':
                print(f"Resultado: {num1} + {num2} = {sumar(num1, num2)}")
            elif opcion == '2':
                print(f"Resultado: {num1} - {num2} = {restar(num1, num2)}")
            elif opcion == '3':
                print(f"Resultado: {num1} * {num2} = {multiplicar(num1, num2)}")
            elif opcion == '4':
                print(f"Resultado: {dividir(num1, num2)}")
        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    calculadora()