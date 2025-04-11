# nota1 = float(input("Informe a primeira nota: "))
# nota2 = float(input("Informe a segunda nota: "))
# media = (nota1 + nota2)/2
# if (media >= 7):
#     print("Aprovado")
# elif (media <= 6):
#     print("Reprovado")
# print("A media é :", media)

# --------------------------------------------------------------

# salario = float(input("Informe o salario: "))
# if (salario < 500.00):
#     print(f"O reajuste é de 15%, total de = {salario*1.15:.2f}" )
          
# elif (salario >= 500.00 and salario < 1000.00):
#     print (f"O reajuste é de 10%, total de = {salario*1.10:.2f}")

# elif (salario >= 1000.00):
#     print(f"O reajuste é de 5%, total de = {salario*1.05:.2f}")
          
# ------------------------------------------------------------

# sexo = input("Digite F, M ou O: ").upper()
# if sexo == "F":
#     print ("F = Feminino")
# elif sexo == "M":
#     print ("M = Masculino")
# elif sexo == "O":
#     print("O = Outros")

# else:
#     print ("sexo invalido")

# -----------------------------------------------------------------------

# letra = input("Digite uma letra: ").upper()
# if (letra == "A" or letra == "E" or letra == "i" or letra == "O" or letra == "U"):
#     print("A letra é uma vogal")
# else:
#     print ("A letra é uma consoante")


#-------------------------------------------------------------------------


# numero1 = input("Informe o primeiro numero: ")
# numero2 = input("Informe o segundo numero: ")
# numero3 = input("Informe o terceiro numero: ")

# if (numero1 > numero2 and numero2 > numero3):
#     print("O numero menor é:", numero3, "e o maior numero é:", numero1)

# elif (numero2 > numero3 and numero3 > numero1):
#     print("O numero menor é:", numero1, "e o maior numero é:", numero2)

# elif (numero3 > numero1 and numero1 > numero2):
#     print("O numero menor é:", numero2, "e o maior numero é:", numero3)

# elif (numero3 > numero2 and numero2 > numero1):
#     print("O menor é:", numero1, "o maior é:", numero3)

# elif (numero1 > numero3 and numero2 > numero2):
#     print("o menor é:", numero2, "e o maior é:", numero1)

# elif (numero2 > numero1 and numero1 > numero3):
#     print ("o menor é:", numero3, "e o maior é:", numero2)

#--------------------------------------------------------------


# valor1 = input("Informe o primeiro valor: ")
# valor2 = input("Informe o segundo valor: ")
# valor3 = input("Informe o terceiro valor: ")

# if (valor1 > valor2 and valor2 > valor3):
#     print("O produto com menor valor é:", valor3)

# elif (valor2 > valor3 and valor3 > valor1):
#     print("O produto com menor valor é:",valor1)

# elif (valor3 > valor1 and valor1 > valor2):
#     print("O produto com menor valor é:",valor2)

# elif (valor3 > valor2 and valor2 > valor1):
#     print("O produto com menor valor é:", valor1)

# elif (valor1 > valor3 and valor3 > valor2):
#     print("O produto com menor valor é:", valor2)

# elif (valor2 > valor1 and valor1 > valor3):
#     print ("O produto com menor valor é:", valor3)

#-------------------------------------------------------------------

# n1 = input("Informe o primeiro numero: ")
# n2 = input("Informe o segundo numero: ")
# n3 = input("Informe o terceiro numero: ")

# if (n1 > n2 and n2 > n3):
#     print(n1, n2, n3)
# elif (n2 > n3 and n3 > n2):
#     print(n2, n3, n1)
# elif (n3 > n1 and n1 > n2):
#     print(n3, n1, n2)

# elif (n3 > n2 and n2 > n1):
#     print(n3, n2, n1)

# elif (n1 > n3 and n2 > n2):
#     print(n1, n3, n2)

# elif (n2 > n1 and n1 > n3):
#     print (n2, n1, n3)

#-------------------------------------------------------------



salario = float(input("Informe o salario: "))
if (salario <= 280.55):
    print(f"O reajuste é de 22,51%, total de = {salario+salario*22.51/100:.2f}" )
          
elif (salario >= 280.56 and salario < 709.72):
    print (f"O reajuste é de 15,39%, total de = {salario+salario*15.39/100:.2f}")

elif (salario >= 709.73 and salario <= 1501.33):
    print(f"O reajuste é de 10,97%, total de = {salario+salario*10.97/100:.2f}")

elif (salario >= 1501.34 ):
    print(f"O reajuste é de 5.19%, total de = {salario+salario*5.19/100:.2f}")
else:
    print(salario)