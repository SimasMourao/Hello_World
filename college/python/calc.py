line = "="
op = ["+", "-", "*", "/"]

while True:
   print("Hello World!")
   print(line * 50)
   nUm = float(input("Digite um valor: "))
   opUser = input("escolha entre as operacoes: | + | - | * | / |  ")
   nDois = float(input("Digite outro valor: "))
   print(line * 50)

   match opUser:
      case "+":
         print(f"{nUm} + {nDois} = {nUm + nDois}")
      
      case "-":
         print(f"{nUm} - {nDois} = {nUm - nDois}")
      
      case "*":
         print(f"{nUm} * {nDois} = {nUm * nDois}")
      
      case "/":
         print(f"{nUm} / {nDois} = {nUm / nDois}")

   print(line * 50)  
   continuar = input("Deseja contnuar?(DIGITE 'S' OU 'N')")

   if  continuar == "N":
      break

      
    