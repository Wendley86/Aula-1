#este print e um teste
#para receber infor do usuario usar (imput)
# IF = se Else = senao Condicional
print("-------calculadora------\n")
opcao = int(input("Digite:\n1- soma\n2- subtracao\n3- multiplicacao\n4- divisao\n"))

if opcao == 1:#opcao de soma
  print("Voce esta na opcao de soma")
  numero1 = int(input("Insira o primeiro numero: "))
  numero2 = int(input("Insira o segundo numero: "))
  soma = numero1 + numero2
  print(f"o resultado da soma e {soma}")
  
elif opcao == 2:
  print("Voce esta na opcao de subtracao")
  numero1 = int(input("Insira o primeiro numero: "))
  numero2 = int(input("Insira o segundo numero: "))
  subtracao = numero1 - numero2
  print(f"o resultado da subtracao e {subtracao}")
  
elif opcao == 3:
  print("Voce esta na opcao de multiplicacao")
  numero1 = int(input("Insira o primeiro numero: "))
  numero2 = int(input("Insira o segundo numero: "))
  multiplicacao = numero1 * numero2
  print(f"o reusltado da multiplicacao e {multiplicacao}")
  
elif opcao == 4:
  print("Voce esta na opcao de divisao")
  numero1 = int(input("Insira o primeiro numero: "))
  numero2 = int(input("Insira o segundo numero: "))
  divisao = numero1 / numero2
  print(f"o resultado da divisao e {divisao}")
else: 
 print("Usuario foi de F")