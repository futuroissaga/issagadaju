# Inicializando o contador
contador = 0

# Loop para ler os números
while True:
    numero = int(input("Digite um número (0 para sair): "))
    
    # Verificando se o número é 0 para parar o loop
    if numero == 0:
        break
    
    # Verificando se o número está entre 100 e 200
    if 100 <= numero <= 200:
        contador += 1

# Resultado final
print(f"Quantidade de números entre 100 e 200: {contador}")
