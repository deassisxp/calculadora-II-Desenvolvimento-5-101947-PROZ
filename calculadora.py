def Calculadora(num1, num2, op):
    if(op == '1'):
        resultado = num1 + num2
    elif(op == '2'):
        resultado = num1 - num2
    elif(op == '3'):
        resultado = num1 * num2
    elif(op == '4'):
        if num2 != 0:
            resultado = num1 / num2
        else:
            resultado = "Erro: Divisão por zero"
    else:
        resultado = "Essa opção não existe"
    
    return resultado


op = ''
while(op != '0'):
    print("---- Escolha uma opção ----")
    print("1 Soma")
    print("2 Subtração")
    print("3 Multiplicação")
    print("4 Divisão")
    print("0 Sair")
    op = input()
    if(op != '0'):
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        resultado = Calculadora(num1, num2, op)
        print("O Resultado é: ",resultado)

    

    
