n = int(input("Digite o valor de n: "))


if n < 0:
		
	print("Não existe fatorial de número negativo.")

else:

	fatorial = 1  

	while n > 1:
	
		fatorial = fatorial * n

		n = n - 1

	print(fatorial)

	
	
	
