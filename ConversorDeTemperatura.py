def celsius_para_fahrenheit(celsius):
    return celsius * 9/5 + 32

def fahrenheit_para_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def celsius_para_kelvin(celsius):
    return celsius + 273.15

def kelvin_para_celsius(kelvin):
    return kelvin - 273.15

def fahrenheit_para_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15

def kelvin_para_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32

def main():
    print("Conversor de Temperatura")
    print("------------------------")

    while True:
        print("Escolha uma opção:")
        print("1. Celsius para Fahrenheit")
        print("2. Fahrenheit para Celsius")
        print("3. Celsius para Kelvin")
        print("4. Kelvin para Celsius")
        print("5. Fahrenheit para Kelvin")
        print("6. Kelvin para Fahrenheit")
        print("7. Sair")

        opcao = input("Digite a opção: ")

        if opcao == "1":
            celsius = float(input("Digite a temperatura em Celsius: "))
            fahrenheit = celsius_para_fahrenheit(celsius)
            print(f"{celsius}°C é igual a {fahrenheit}°F")
        elif opcao == "2":
            fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
            celsius = fahrenheit_para_celsius(fahrenheit)
            print(f"{fahrenheit}°F é igual a {celsius}°C")
        elif opcao == "3":
            celsius = float(input("Digite a temperatura em Celsius: "))
            kelvin = celsius_para_kelvin(celsius)
            print(f"{celsius}°C é igual a {kelvin} K")
        elif opcao == "4":
            kelvin = float(input("Digite a temperatura em Kelvin: "))
            celsius = kelvin_para_celsius(kelvin)
            print(f"{kelvin} K é igual a {celsius}°C")
        elif opcao == "5":
            fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
            kelvin = fahrenheit_para_kelvin(fahrenheit)
            print(f"{fahrenheit}°F é igual a {kelvin} K")
        elif opcao == "6":
            kelvin = float(input("Digite a temperatura em Kelvin: "))
            fahrenheit = kelvin_para_fahrenheit(kelvin)
            print(f"{kelvin} K é igual a {fahrenheit}°F")
        elif opcao == "7":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()