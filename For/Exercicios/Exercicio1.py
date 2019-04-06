'''Com base no último ex.do FOR, faça com q o usuario digite um palavra e o "FOR" exiba somente as vogais'''
palavra = input("Digite uma palavra para verificar as vagais: ")
for letra in palavra:
    if letra in "aeiouAEIOU":
        print(letra)