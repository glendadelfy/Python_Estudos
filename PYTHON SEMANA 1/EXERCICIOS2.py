#PYTHON DIA 06/09/2026

#INICIO 16:30

#Exercício: Sistema de Verificação de Idade para Ingresso em Evento 🎟️
#Você foi contratado para criar um programa que verifica se uma pessoa pode entrar em um evento. As regras são:

# programa deve pedir a idade da pessoa.

#Se a idade for menor que 18, a entrada não é permitida.

#Se a idade for entre 18 e 65, a entrada é permitida normalmente.

#Se a idade for maior que 65, a entrada é permitida, mas com desconto especial.

#O programa deve imprimir uma mensagem adequada para cada caso.


Idade = int(input("Qual sua idade? "))

if Idade < 0:
    print ("Você não essa idade")
elif Idade < 18:
     print ("Você é menor de idade e não pode entrar")
elif Idade > 65:
    print("Você pode entrar e tem desconto especial")
elif Idade >= 18 and Idade <= 65:
    print("Você pode entrar")
else:
    print("Idade invalida")

# 17:22

#19:20 


#Exercício de Lógica – Sistema de Classificação de Viagem ✈️
#Crie um programa que receba três informações do usuário:

#Idade

#Possui carteira de motorista? (True/False)

#Possui passaporte válido? (True/False)

#Regras:

#Se a idade for menor que 18, a pessoa não pode viajar sozinha.

#Se a idade for maior ou igual a 18 e tiver carteira de motorista, mas não tiver passaporte, o programa deve dizer que ela só pode viajar dentro do país.

#Se a idade for maior ou igual a 18 e tiver passaporte válido, o programa deve dizer que ela pode viajar para fora do país.
    
#Se a idade for maior que 65, além das regras acima, deve aparecer uma mensagem extra dizendo que a pessoa tem direito a prioridade no embarque.

#Caso nenhuma condição seja atendida, exiba "Informações inválidas".

idade = int(input("Qual a sua idade? "))
carteira_motorista = input("Você possui carteira de motorista? (sim/não) ").lower() == "sim"
passaporte = input("Você possui passaporte válido? (sim/não) ").lower() == "sim"

if idade >= 18:
    if carteira_motorista and not passaporte:
        print("Você só pode viajar dentro do país")
    elif passaporte:
        print("Você pode viajar para fora do país")
    else:
        print("Você não pode viajar")
else:
    print("Você não pode viajar sozinho")

# 20:30

