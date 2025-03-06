#Exercício que calcula o IMC e classifica o seu resultado
#pegando os dados
peso = float(input('Digite o Peso(kg): '))
altura = float(input('Digite a Altura(m): '))
#calculando o IMC = peso / altura²
imc = peso / (altura ** 2)
print('O resultado do IMC é {:.2f} kg/m2'.format(imc))
#fazendo comparações para Classificação de IMC
