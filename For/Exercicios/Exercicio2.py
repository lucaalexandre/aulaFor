get_number = 0
position = 0


for x in range(1,10):
    number = int(input("Digite um numero: "))

    if number > get_number:
        get_number = number
        position = x
print("Maior Numero: ", get_number)
print("Posicao", position)
