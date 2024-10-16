
kelvin = [273.15, 300, 350, 400, 450, 500, 550, 600, 650, 700]

celsius = [(x - 273.15) for x in kelvin]
fahrenheit = [(x * 9/5 - 459.67) for x in kelvin]

print("{:<4} {:<10} {:<10} {:<10}".format("Nº", "Kelvin", "Celsius", "Fahrenheit"))
print("="*40)

for i in range(len(kelvin)):
    print("{:<4} {:<10.2f} {:<10.2f} {:<10.2f}".format(i+1, kelvin[i], celsius[i], fahrenheit[i]))