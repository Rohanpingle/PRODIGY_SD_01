def celsius_to_fahrenheit(celsius):
    return celsius * 9/5 + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32

def convert_temperature(temperature, unit):
    if unit.lower() == 'c':
        celsius = temperature
        fahrenheit = celsius_to_fahrenheit(celsius)
        kelvin = celsius_to_kelvin(celsius)
    elif unit.lower() == 'f':
        fahrenheit = temperature
        celsius = fahrenheit_to_celsius(fahrenheit)
        kelvin = fahrenheit_to_kelvin(fahrenheit)
    elif unit.lower() == 'k':
        kelvin = temperature
        celsius = kelvin_to_celsius(kelvin)
        fahrenheit = kelvin_to_fahrenheit(kelvin)
    else:
        print("Invalid unit. Please enter 'C' for Celsius, 'F' for Fahrenheit, or 'K' for Kelvin.")
        return

    print(f"{temperature} degrees {unit.upper()} is equal to:")
    print(f"{fahrenheit:.2f} degrees Fahrenheit")
    print(f"{kelvin:.2f} Kelvin")
    print(f"{celsius:.2f} degrees Celsius")

temperature = float(input("Enter the temperature value: "))
unit = input("Enter the unit of measurement (C for Celsius))
