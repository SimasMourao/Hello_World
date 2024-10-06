line = "="

print("Hello World!")
print(line * 50)
nUm = float(input("Digite um valor: "))
print(line * 50)
op = input("escolha entre as operacoes: | + | - | * | / |  ")
print(line * 50)
nDois = float(input("Digite outro valor: "))
print(line * 50)

match op:
    case "+":
        print(f"{nUm} + {nDois} = {nUm + nDois}")
    
    case "-":
       print(f"{nUm} - {nDois} = {nUm - nDois}")
    
    case "*":
       print(f"{nUm} * {nDois} = {nUm * nDois}")
    
    case "/":
       print(f"{nUm} / {nDois} = {nUm / nDois}")

    
    