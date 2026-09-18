# Programa de cálculo: Consumo de energia

# Entrada
Eletrodomestico = input("Qual é o eletrodoméstico a ser calculado? ")
Potencia = float(input("Qual é a potência do aparelho em watts (W)? "))
horasDia = float(input("Qual é o tempo médio de uso diário em horas? "))

# Processamento
consumoMensal = (Potencia * horasDia * 30) / 1000
Custo = consumoMensal * 0.75

# Saída
print(f"O aparelho {Eletrodomestico} tem um consumo estimado de {consumoMensal:.2f} kWh por mês, com um custo estimado de R$ {Custo:.2f}.")