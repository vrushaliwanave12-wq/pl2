#temperatue/_init_.py
from celsius_to_fahrenheit import celsius_to_fahrenheit
from fahrenheit_to_celsius import fahrenheit_to_celsius
from celsius_to_kelvin import celsius_to_kelvin

#temperatue/celsius_to_fahrenheit.py
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

#temperatue/fahrenheit_to_celsius.py
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

#temperatue/celsius_to_kelvin.py
def celsius_to_kelvin(celsius):
    return celsius + 273.15

#Main.py
from temperatue import celsius_to_fahrenheit, fahrenheit_to_celsius, celsius_to_kelvin

def main():
    print("Temperature Conversion Options:")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")

    choice = input("Enter the number of your choice:")

    if choice == "1":
        celsius = float(input("Enter temperature in Celsius:"))
        fahrenheit = celsius_to_fahrenheit.celsius_to_fahrenheit(celsius)
        print(f"{celsius:.2f}°C is equal to {fahrenheit:.2f}°F")

    elif choice == "2":
        fahrenheit = float(input("Enter temperature in Fahrenheit:"))
        celsius = fahrenheit_to_celsius.fahrenheit_to_celsius(fahrenheit)
        print(f"{fahrenheit:.2f}°F is equal to {celsius:.2f}°C")

    elif choice == "3":
        celsius = float(input("Enter temperature in Celsius:"))
        kelvin = celsius_to_kelvin.celsius_to_kelvin(celsius)
        print(f"{celsius:.2f}°C is equal to {kelvin:.2f}K")

    else:
        print("Invalid choice. Please select a valid option.")

if _name_=="_main_":
    main()