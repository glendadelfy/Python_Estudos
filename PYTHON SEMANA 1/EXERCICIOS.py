#DIA 05/09/2026 
#PYTHON

#Sistema de Aprovação Escolar
#Crie um programa que receba:

#A nota de um aluno

#O percentual de presença

#Regras:

#Se a nota for maior ou igual a 7 e a presença maior ou igual a 75 → o aluno está aprovado.

#Se a nota for maior ou igual a 7 mas a presença for menor que 75 → o aluno está reprovado por falta.

#Se a nota for menor que 7 mas a presença for maior ou igual a 75 → o aluno está reprovado por nota.

#Caso contrário → o aluno está reprovado por nota e presença.

nota = 6
presenca = 79

if nota >= 7:
    if presenca >= 75:
        print ("Parabéns você está aprovado")
    else:
        print ("Você atingiu a nota superior a sete mas foi reprovadp por presença inferior a 75")
elif presenca > 75:
    print("Você foi reprovado por falta de nota mas atingiu a presenca suprior a 75")
else:
    print("Você foi reprovado por falta de nota")

# 03:16

#Exercício 2 – Sistema de Ingressos 
#Crie um programa que receba a idade de uma pessoa e verifique o valor do ingresso:

#Se a idade for menor que 12 → ingresso gratuito.

#Se a idade estiver entre 12 e 17 → ingresso com 50% de desconto.

#Se a idade for maior ou igual a 18 → ingresso com valor integral.
    
idade = 14
ingresso = True

if idade < 12:
    print("Você não precisa pagar pelo ingresso")
elif idade >= 12 and idade <= 17:
    print ("Voce tem 50% de desconto")
else:
    print("Você paga o valor integral do ingresso")

#03:38

