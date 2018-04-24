print("Controle de Estoque")
print("0 - sair",
      "1 - adicionar item",
      "2 - remover item",
      "3 - alterar item",
      "4 - imprimir estoque")

escolha = int(input("Faça sua escolha: "))
estoque = {}



while escolha > 0:        
    if escolha == 1:
        nome_produto = input('Digite o Produto: ')
        if nome_produto in estoque:
            print('Esse produto já está no estoque')
            break
        quantidade = int(input('Digite a quantidade do produto: '))
    if quantidade < 0:
        while quantidade < 0:
            print('A quantidade inicial não pode ser negativa')
            quantidade = int(input('Digite a quantidade do produto: '))
    estoque[nome_produto] = quantidade
    
    print("Controle de Estoque")
    print("0 - sair",
      "1 - adicionar item",
      "2 - remover item",
      "3 - alterar item",
      "4 - imprimir estoque")

    escolha = int(input("Faça sua escolha: "))
    

   
if escolha == 0:
    print(estoque)
    print("até mais!")

