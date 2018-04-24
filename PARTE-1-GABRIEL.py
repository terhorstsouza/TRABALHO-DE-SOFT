negativos = []
valores = 0
import json


with open ('Arquivo.txt','r') as arquivo:
    conteudo = arquivo.read()
    estoque = json.loads(conteudo)



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
            print('A quantidade inicial não pode ser negativa')
            break    
        preco = int(input('Digite o preço do produto: '))
    estoque[nome_produto] = {}
    estoque[nome_produto]['Quantidade'] = quantidade
    estoque[nome_produto]['preço'] = preco	

    if escolha == 2:
        nome_produto = input('Digite o Produto: ')
        if nome_produto in estoque:
            del estoque[nome_produto]
        else:
            print('Nao se encontra no estoque')
            break
    
    if escolha == 4:
        print(estoque)
    
    
    print("Controle de Estoque")
    print("0 - sair",
      "1 - adicionar item",
      "2 - remover item",
      "3 - alterar item",
      "4 - imprimir estoque")

    escolha = int(input("Faça sua escolha: "))
    

   
if escolha == 0:
   
    print("até mais!")


    for coisas in estoque:
        valor = (estoque[coisas]['preco']) * (estoque[coisas]['Quantidade'])
        valores += valor
    print('O valor total em estoque é: {0} Reais'.format(valores))


    
    for produtos in estoque:
        if (estoque[produtos]['Quantidade']) < 0:
            negativos.append(produtos)
    print('Os seguintes produtos possuem estoques negativos: ')
    print(negativos)


with open ('Arquivo.txt','w') as arquivo:
    conteudo = json.dumps(estoque, sort_keys=True, indent=4)
    arquivo.write(conteudo)