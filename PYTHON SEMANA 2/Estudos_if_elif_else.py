#DIA 07/09/2026

#INICIO 23:00

#if-elif-else
#Estruturas de Decisão
#Em Python, as estruturas de decisão são fundamentais para controlar o fluxo de execução de um programa. Elas permitem que o código tome decisões e execute diferentes blocos de instruções com base em diferentes condições. Estas estruturas são essenciais para a lógica de programação e representam a base de muitos algoritmos.

#Entendendo Condições
#As estruturas de decisão em Python dependem das condições que são avaliadas como verdadeiras (True) ou falsas (False). Estas condições são frequentemente baseadas em operadores de comparação e lógicos.

#Operadores de Comparação
#Estes operadores são usados para comparar valores:

#==: Igual a
#!=: Diferente de
#<: Menor que
#>: Maior que
#<=: Menor ou igual a
#>=: Maior ou igual a
#Exercícios sobre Operadores de Comparação

#Operadores Lógicos
#Estes operadores são usados para combinar condições:

#and: Retorna verdadeiro se ambas as condições forem verdadeiras
#or: Retorna verdadeiro se pelo menos uma das condições for verdadeira
#not: Inverte o resultado da condição
#Exercícios sobre Operadores Lógicos

#A Estrutura if
#A estrutura if é a base das estruturas de decisão em Python. Ela avalia uma condição e, se essa condição for verdadeira, executa o bloco de código indentado sob ela.

temperatura = 30
if temperatura > 25:
    print("Está quente!")
#Exercícios sobre if

#Qual será a saída do seguinte código se `valor = 50`?
a = 10
valor = a
valor = a**2
if valor < 100:
    print("Baixo")


#A Estrutura else
# else captura qualquer condição que não tenha sido capturada pelas cláusulas if e elif. Não tem uma condição associada a ela, pois serve como um coletor padrão.

#Exercícios sobre else

#Dado o código abaixo, qual será a saída se `num = 10`?
num =10
if num % 2 == 0:
    print("Par")
else:
    print("Ímpar")

#Usando o mesmo código, qual será a saída se `num = 15`?

#A Estrutura elif
#A palavra-chave elif é uma abreviação de "else if". É útil quando você precisa verificar várias condições em sequência. Ela segue um if ou outro elif e sua condição é avaliada apenas se as condições anteriores não forem satisfeitas.

temperatura = 20
if temperatura > 25:
    print("Está quente!")
elif temperatura < 18:
    print("Está frio!")
else:
    print("Está ameno!")

#Exercícios sobre elif

#Dado o código abaixo, qual será a saída se `pontos = 75`?
#python
pontos =10
if pontos > 90: print("Excelente!") 
elif pontos > 80: print("Muito bom!")
elif pontos > 70: print("Bom!")
else: print("Tente novamente") 

#Considerando o código da questão anterior, qual será a saída se `pontos = 50`?

#Aninhamento
#É possível aninhar estruturas if dentro de outras estruturas if. Isso permite criar avaliações mais complexas. No entanto, é importante garantir que o código permaneça legível e evitar aninhamentos excessivamente profundos.

idade = 15
acompanhado = True

if idade < 18:
    if acompanhado:
        print("Menor de idade, mas está acompanhado.")
    else:
        print("Menor de idade e desacompanhado.")
else:
    print("Maior de idade.")

#Exercícios sobre Aninhamento
#Usando o código acima, qual será a saída se `idade = 13` e `acompanhado = False`?


#Dicas e Boas Práticas
#Mantenha a legibilidade: Evite aninhar muitos níveis de condições. Se um if tem muitos elif ou níveis profundos de aninhamento, pode ser um sinal de que o código precisa ser refatorado.
#Evite condições complexas: Se uma condição está se tornando muito complexa, considere dividi-la ou use variáveis intermediárias para tornar a lógica mais clara.
#Use parênteses para clareza: Em condições complexas com múltiplos operadores lógicos, use parênteses para tornar a ordem das avaliações clara.

for c in range (1, 10):
    print (c)
print("FIM")

#00:10

