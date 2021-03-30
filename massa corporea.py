peso = float(input('Qual é seu peso ? (kg)'))
altura = float (input('Qual é sua altura ? (m)'))
imc = peso / (altura ** 2)
print ('O imc dessa pessoa é de {:.1f}'.format(imc))

