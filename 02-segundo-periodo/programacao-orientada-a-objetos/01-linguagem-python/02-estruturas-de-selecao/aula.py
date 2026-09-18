n1 = 10
n2 = 4
n3 = 6
n4 = 10

soma = n1 + n2 + n3 + n4
media = soma / 4

# Estrutura de Seleção/Condição Simples - if

if media >= 7:
    print("Aprovado")
    #print("Esse print está dentro do if")


#print("Esse print está fora do if")

'''
O if executa seu bloco somente quando a condição é verdadeira.

Em Python:
- não é necessário colocar a condição entre parênteses;
- os dois pontos (:) indicam o início do bloco;
- a indentação determina quais comandos pertencem ao if.

Com n4 = 10:
media = 7.5 -> condição verdadeira

Com n4 = 2:
media = 5.5 -> condição falsa

""" ... """ é uma string multilinha, não é um comentário.
Strings multilinha podem ser delimitadas por três aspas simples
ou três aspas duplas.

'''


print("A média é:", media)

# Estrutura de Seleção/Condição Composta - if/else

if media >= 7:
    print("Aprovado")
else:
    print("Reprovado")

'''
Na estrutura de seleção composta, temos dois caminhos possíveis:

if -> executado quando a condição é verdadeira.
else -> executado quando a condição do if é falsa.

Neste exemplo:
media >= 7 -> Aprovado
media < 7  -> Reprovado

O else não possui uma condição própria.
Ele representa todos os casos em que a condição do if é falsa.

Em uma mesma execução, apenas um dos blocos será executado:
ou o bloco do if ou o bloco do else, nunca os dois.

'''

# Estrutura de Seleção/Condição Encadeada - if/elif/else - pode ser usado mais de um elif

if media >= 7:
    print("Aprovado")
elif media < 5:
    print("Reprovado")
else:
    print("Em Recuperação")

'''
Na estrutura de seleção encadeada, podemos testar mais de uma condição.

if   -> testa a primeira condição.
elif -> testa outra condição caso as anteriores sejam falsas.
else -> executado quando nenhuma das condições anteriores é verdadeira.

Podemos utilizar mais de um elif.

Quando uma condição é verdadeira, seu bloco é executado
e as condições seguintes da mesma estrutura são ignoradas.

Neste exemplo:
media >= 7 -> Aprovado
media < 5  -> Reprovado
caso contrário -> Em Recuperação

'''

# Estrutura de Seleção/Condição - match/case - comparação com if/elif/else

#dia = 4

#dia = input("Digite o número do dia da semana: ")
# Retorna uma string, portanto não corresponde aos números inteiros usados nas comparações.

dia = int(input("Digite o número do dia da semana: "))
# int() converte a entrada de string para inteiro, permitindo a comparação com 1, 2, 3...

'''

if dia == 1:
    print("Domingo")
elif dia == 2:
    print("Segunda")
elif dia == 3:
    print("Terça")
elif dia == 4:
    print("Quarta")
elif dia == 5:
    print("Quinta")
elif dia == 6:
    print("Sexta")
elif dia == 7:
    print("Sábado")
else:
    print("Dígito Inválido")

'''

match dia:
    case 1:
        print("Domingo")
    case 2:
        print("Segunda")
    case 3:
        print("Terça")
    case 4:
        print("Quarta")
    case 5:
        print("Quinta")
    case 6:
        print("Sexta")
    case 7:
        print("Sábado")
    case other:
        print("Dígito Inválido")

'''
O match compara o valor de uma variável com diferentes casos (case).

Neste exemplo:
case 1 -> Domingo
case 2 -> Segunda
...
case 7 -> Sábado

O professor utilizou "case other:" para capturar qualquer outro valor.
Também é comum utilizar "case _:" para representar o caso padrão.

O match/case pode deixar mais organizada uma situação em que vários
if/elif são utilizados apenas para comparar uma mesma variável com
diferentes valores.

No match, a variável é informada uma única vez e cada case
representa um possível valor dessa variável.

'''