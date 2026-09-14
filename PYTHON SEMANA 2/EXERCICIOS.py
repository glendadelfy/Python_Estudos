#DIA 07/09/2026

#LETS GO TREINO 22:36


# Exercício: Sistema de classificação de clientes em um banco

# Imagine que um banco quer classificar seus clientes de acordo com a renda mensal.
# Regras:
# - Se a renda for maior que 15.000 → "Cliente VIP"
# - Se a renda for entre 8.000 e 15.000 → "Cliente Premium"
# - Se a renda for entre 3.000 e 8.000 → "Cliente Regular"
# - Se a renda for abaixo de 3.000 → "Cliente Básico"

renda = int(input("Digite a renda mensal do cliente: "))

# Escreva aqui a estrutura if, elif e else para classificar o cliente

if renda < 0:
    print("Entrada irregular")
elif renda >= 15000:
    print("Cliente VIP")
elif renda >= 8000 and renda <= 15000:
    print("Cliente Premium")
elif renda >= 3000 and renda <= 8000:
    print("Cliente regular")
elif renda < 3000:
    print("Cliente báico")
else:
    print("Você não é cliente")

# Exercício: Aprovação de Empréstimo

# Um banco precisa decidir se aprova ou não um empréstimo para um cliente.
# As regras são:
# - Se a renda mensal for menor que 2000 → "Empréstimo negado"
# - Se a renda mensal for entre 2000 e 5000:
#       - Se o cliente tiver mais de 2 anos de histórico no banco → "Empréstimo aprovado com limite baixo"
#       - Caso contrário → "Empréstimo negado"
# - Se a renda mensal for entre 5000 e 10000 → "Empréstimo aprovado com limite médio"
# - Se a renda mensal for acima de 10000 → "Empréstimo aprovado com limite alto"

renda = int(input("Digite a renda mensal do cliente: "))
historico = int(input("Digite os anos de histórico no banco: "))

# Escreva aqui a estrutura if, elif e else para aplicar as regras acima

if renda < 2000:
    print("Empréstimo negado")
elif renda >= 2000 and renda < 5000:
    if historico > 2:
        print("Empréstimo aprovado com limite baixo")
    else:
        print("Empréstimo negado")
elif renda >= 5000 and renda < 10000:
    print("Empréstimo aprovado com limite médio")
elif renda >= 10000:
    print("Empréstimo aprovado com limite alto")

#23:24