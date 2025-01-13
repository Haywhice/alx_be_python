#This script will define functions to convert temperatures between Celsius and Fahrenheit, demonstrating the use of global variables to store conversion factors that are accessible within functions.

#Global Conversion Factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celcius(fahrenheit):
    """converts temperature in fahrenheit to celsius"""
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """Converts teOOBmperature in celsius to fahrenheit"""
    return ((celsius) * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
def main():
    """Receives user's input and converts the temperature"""
    while True:
        try:
            #Prompts user for temperature
            temperature = int(input("Enter the temperature to convert: "))
            break #exits the loop for a valid entry
        
        except ValueError:
            # handle non-numeric input
            print("Invalid temperature. Please enter a numeric value.")

   #Prompts user for unit
    unit = input("Is this temperature in Celcius or Fahrenheit? (C/F): ").strip().upper()
    
    if unit == "F":
        #Converts celsius to fahrenheit
        celcius =  convert_to_celcius(temperature)
        print(f" {temperature} is {celcius}°C")
    elif unit == "C":
        #Converts fahrenheit to celsius
        fahrenheit =  convert_to_fahrenheit(temperature)
        print(f" {temperature} is {fahrenheit}°F")
    else:
        #Invalid unit input
        raise ValueError("Invalid unit Please enter 'C' for Celsius or 'F' for Fahrenheit.")

if __name__ == "__main__":
    main()

