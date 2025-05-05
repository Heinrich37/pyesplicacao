# while True:
#     print ("Loop Infinito \n") #while true faz um loop infinitamente

#--------------------------------------------------------------------------------

# while True:
#     valor = int(input("Digite 1 ou 0 Para fim: \n"))
#     if valor == 1:
#         print("valor correto")
#     else:
#         print ("Valor para sair")
#         break #break para terminar o loop

#-------------------------------------------------------------------------------

# while True:
#     valor = int(input("Digite um numero: \n"))
#     if valor <= 1:
#         continue
#         print("maior o igual a um")
#     if valor > 1:
#         print ("maior que um")


#------------------------------------------------------------------------------
# a = int(input("Informe um numero: "))
# b = 0
# while a > 0:
#     print(a)
#     a = a-1
#     b = b+1
# print(b)
    

#-------------------------------------------------------------------------------
# while True:    
    # operacao = input("Infome a operação. (a)Para adição (d)Para Divisão (m)Para multiplicação (s)Para subtração (x)Para sair:\n").lower()
    # if (operacao == "a" or operacao == "A"):
    #     a1 = float(input("informer o primeiro numero:"))
    #     a2 = float(input("informer o segundo numero:"))
    #     print (a1 + a2)
    # if (operacao == "d" or operacao == "D"):
    #     a1 = float(input("informer o primeiro numero:"))
    #     a2 = float(input("informer o segundo numero:"))
    #     print (a1 / a2)
    # if (operacao == "m" or operacao == "M"):
    #     a1 = float(input("informer o primeiro numero:"))
    #     a2 = float(input("informer o segundo numero:"))
    #     print (a1 * a2)
    # if (operacao == "s" or operacao == "S"):
    #     a1 = float(input("informer o primeiro numero:"))
    #     a2 = float(input("informer o segundo numero:"))
    #     print (a1 - a2)
    # if (operacao == "x" or operacao == "X"):
    #     break
    
    
#------------------------------------------------------------------------------------

# while True:    
#     n = float(input("Infome um numero entre 0 e 10:\n"))
#     if (n >= 0 and n <= 10):
#         print("valor valido")
#         break
#     else:
#         print ("valor invalido")
    
#-----------------------------------------------------------------------------
# while True:
#     nome = input("Informe seu nome:\n").upper()
#     senha = input("Iforme sua senha:\n").upper()
#     if(nome == senha):
#         print("Senha digitada não pode ser igual ao nome")
#     if(nome != senha):
#         print("login feito com sucesso")
#         break
    

#---------------------------------------------------------------------------

# while True:
#     nome = input("Infome seu nome:\n")
#     idade = int(input("Informe sua idade:\n"))
#     salario = float(input("Informe seu salario:\n"))
#     sexo = input("Informe seu sexo. (f)Para feminino (m)Para masculino (o)Para outros")
#     estado_civil = input("Informe seu estado civil. (s)Para solteiro(a), (c)Para casado(a), (v)Para viuvo(a), (d)Para divorciado(a)")
#     quantidade = len(nome)
#      if (nome >= 3 and idade):





Bolsonaro = 0
Lula = 0
Geraldo = 0
Ciro = 0
nulo = 0
branco = 0

print("------------------------------Sistema de votação presidencial------------------------------")

print("1 - Bolsonaro")
print("2 - Lula")
print("3 - Geraldo Alckmin")
print("4 - Ciro gomes")
print(" - Nulo")
print("Voto em Branco")

voto = -1

while voto != 0:
    voto = int(input("Digite numero do candidato: "))
    
    if voto == 1:
        Bolsonaro += 1 
    elif voto == 2:
        Lula += 1
    elif voto == 3:
        Geraldo += 1
    elif voto == 4:
        Ciro += 1
    elif voto == " ":
        nulo += 1
    elif voto == 6:
        branco += 1
    elif voto == 0:
        print("Votaçao encerrada!!!")
    else:
        print ("Voto invalido! Tente novamente.")
    
    
print ("------------------------------RESULTADO FINAL DA ELEIÇÃO------------------------------")
print("Bolsonaro:", Bolsonaro, "Votos")
print("Lula:", Lula, "Votos")
print("Geraldo :", Geraldo, "Votos")
print("Ciro:", Ciro, "Votos")
print("Nulo:", nulo, "Votos")
print("Branco:", branco, "Votos")

if Lula > Bolsonaro and Lula > Geraldo and Lula > Ciro:
    print("Lula ganhador")
if Bolsonaro > Lula and Bolsonaro > Geraldo and Bolsonaro > Ciro:
    print("2 ganhador")
if Geraldo > Lula and Geraldo > Bolsonaro and Geraldo > Ciro:
    print("Geraldo ganhador")
if Ciro > Lula and Ciro > Geraldo and Ciro > Bolsonaro:
    print("Ciro ganhador")


