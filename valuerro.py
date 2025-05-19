while True:
    try:
        num = int(input("Digite um número: "))
        if num < 100:
            print("Número ok")
        else:
            break
    except ValueError:
        print("Digite um número válido")
