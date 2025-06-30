reais = 100.00
taxa_dolar = 5.20
taxa_euro = 6.15

dolares = reais / taxa_dolar
euros = reais / taxa_euro

print(f"Valor em dólares: ${dolares:.2f}")
print(f"Valor em euros: €{euros:.2f}")
