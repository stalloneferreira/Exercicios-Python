#Exercício que calcula o IMC e classifica o seu resultado
#pegando os dados
peso = float(input('Digite o Peso(kg): '))
altura = float(input('Digite a Altura(m): '))
#calculando o IMC = peso / altura²
imc = peso / (altura ** 2)
print('O resultado do IMC é {:.2f} kg/m2'.format(imc))
#fazendo comparações para Classificação de IMC
if imc < 16:
    print('Você está com MAGREZA GRAVE, procure um médico o mais RÁPIDO')
elif imc < 17:
    print('Você está com MAGREZA MODERADA, precisa ter CUIDADO!')
elif imc < 18.5:
    print('Você está com MAGREZA LEVE, precisa ter ATENÇÃO!')
elif imc < 25:
    print('Você está SAUDÁVEL, PARABÉNS mantenha assim!')
elif imc < 30:
    print('Você está com SOBREPESO, cuide-se!')
elif imc < 35:
    print('Você está com OBESIDADE GRAU I, precisa ter ATENÇÃO!')
elif imc < 40:
    print('Você está com OBESIDADE GRAU II, precisa ter CUIDADO!')
else:
    print('Você está com OBESIDADE GRAU III, procure um médico o mais RÁPIDO')
