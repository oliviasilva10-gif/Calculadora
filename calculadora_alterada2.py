def somar(valor1, valor2):
    somar = valor1 + valor2
    return somar
def subtrair (valor1, valor2):
    subtrair = valor1 - valor2
    return subtrair
def multiplicar (valor1, valor2):
    multiplicar = valor1 * valor2
    return multiplicar
def dividir (valor1, valor2):
    dividir = valor1 / valor2
    return dividir
def potenciacao (valor1, valor2):
    potencia = valor1 ** valor2
    return potencia
def porcentagem(valor1, valor2):
    porcentagem = (valor1 / 100) * valor2
    return porcentagem
print(" Bem-Vindo a calculadora")
valor1 = float(input("Insira valor: "))
operacao = input("Digite operação desejada: ")
valor2 = float(input("Insira valor: "))
if operacao == "+":
    resultado = somar(valor1, valor2)
elif operacao == "-":
    resultado = subtrair(valor1, valor2)
elif operacao == "*":
    resultado = multiplicar(valor1, valor2)
elif operacao == "/":
    resultado = dividir(valor1, valor2)
elif operacao == "**":
    resultado = potenciacao(valor1, valor2)
elif operacao == "%":
    resultado = porcentagem(valor1, valor2)
else: 
    print("Valor invàlido, por favor digite uma operação válida")
print (resultado)
