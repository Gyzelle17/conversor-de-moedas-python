print("=== Conversor de Moedas Simples ===")

# Entrada do usuário
valor_em_euros = float(input("Digite o valor em euros (€): "))

# Taxas de câmbio fictícias
taxa_euro_para_dolar = 1.07   # 1 euro = 1.07 dólares
taxa_euro_para_libra = 0.85   # 1 euro = 0.85 libras

# Conversões
valor_em_dolares = valor_em_euros * taxa_euro_para_dolar
valor_em_libras = valor_em_euros * taxa_euro_para_libra

# Resultados formatados
print("\n=== Resultado da Conversão ===")
print(f"€{valor_em_euros:.2f} equivalem a ${valor_em_dolares:.2f} dólares")
print(f"€{valor_em_euros:.2f} equivalem a £{valor_em_libras:.2f} libras")
