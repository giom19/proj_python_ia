
kg = [50, 60, 70, 80, 90, 100, 110, 120, 130, 140]

gravidade_terra = 9.81
gravidade_lua = 1.62
gravidade_marte = 3.71
gravidade_mercurio = 3.7

peso_terra = [x * gravidade_terra for x in kg]
peso_lua = [x * gravidade_lua for x in kg]
peso_marte = [x * gravidade_marte for x in kg]
peso_mercurio = [x * gravidade_mercurio for x in kg]

print("{:<4} {:<6} {:<10} {:<10} {:<10} {:<10}".format("Nº", "Kg", "Terra", "Lua", "Marte", "Mercúrio"))
print("="*50)

for i in range(len(kg)):
    print("{:<4} {:<6} {:<10.2f} {:<10.2f} {:<10.2f} {:<10.2f}".format(i+1, kg[i], peso_terra[i], peso_lua[i], peso_marte[i], peso_mercurio[i]))