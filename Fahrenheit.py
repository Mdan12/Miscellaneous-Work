# Convert Celsius to Fahrenheit
# (°C × 9/5) + 32 = °F



def fahrenheit():
    while True:
        try:
            celcius = float(input("Please enter a number, it will then return the heat in fahrenheit. "))
        except ValueError:
            print("Please only use numbers. Thank you.\n")
        else:
            break
    fahrenheit = (celcius * 9/5 )+ 32
    return fahrenheit



print(fahrenheit())
