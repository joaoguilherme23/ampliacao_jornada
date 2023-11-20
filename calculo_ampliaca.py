while True:
    print()
    print("CALCULO DE AMPLIAÇÃO DE JORNADA")
    print("---------------------------------------------------")
    print("O valor de aux.alimenta/refeição é um valor fixo")
    print("---------------------------------------------------")
    valor_base = float(input("digite o valor o base: "))


    previdencia =  valor_base * 0.14
    print()  
    print(f"Resultado previdencia {previdencia:.2f}")

    ferias = valor_base / 3
    resultado_ferias = ferias / 12
    print(f"Resultado Ferias:   {resultado_ferias:.2f}")

    decimo = valor_base / 12
    print(f"Resultado Decimo  {decimo:.2f}")

    result = 74.80

    total = valor_base + previdencia+ resultado_ferias + decimo + result
    print()
    print(f"Resultado do calculo de ampliação de jornada {total:.2f}")
    print()
    print("***************** NOVO CALCULO *****************")