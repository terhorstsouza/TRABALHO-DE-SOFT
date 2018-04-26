negativos = []
valores = 0
import json


with open ('Arquivo.txt','r') as arquivo:
    conteudo = arquivo.read()
    estoque = json.loads(conteudo)

#HUB de escolhas
print('O que deseja fazer?')
print('A - Adicionar loja')
print('B - Acessar loja')
print('C - Excluir loja')

escolha2 = input('Digite sua escolha:  ')

if escolha2 == 'A':
    Franquia = {}
    Nome = input('Digite sua loja: ')
    while Nome in Franquia:
        print('J� est� Cadastrada')
        Nome = input('Digite sua loja: ')
        
if escolha2 == 'B':
    Franquia = {}
    Nome = input('Digite sua loja: ')
    if Nome in Franquia:
        print(Franquia[Nome])

    else:
        while Nome not in Franquia:    
            print('Essa loja n�o existe')
            Nome = input('Digite sua loja: ')

if escolha2 == 'C':
    Franquia = {}
    Nome = input('Digite sua loja: ')
    if Nome not in Franquia:
        print('Essa loja n�o existe')
        while Nome not in Franquia:
           Nome = input('Digite sua loja: ')

print("Controle de Estoque")
print("0 - sair",
      "1 - adicionar item",
      "2 - remover item",
      "3 - alterar item",
      "4 - imprimir estoque",
      "5 - Alterar pre�o")

escolha = int(input("Fa�a sua escolha: "))
estoque = {}



while escolha > 0:        
    if escolha == 1:
        nome_produto = input('Digite o Produto: ')
        if nome_produto in Franquia[Nome]:
            print('Esse produto j� est� no estoque')
            
        quantidade = int(input('Digite a quantidade do produto: '))
        if quantidade < 0:
            print('A quantidade inicial n�o pode ser negativa')
               
        preco = int(input('Digite o pre�o do produto: '))
        Franquia[Nome][nome_produto] = {}
        Franquia[Nome][nome_produto]['Quantidade'] = quantidade
        Franquia[Nome][nome_produto]['preco'] = preco

    if escolha == 2:
        nome_produto = input('Digite o Produto: ')
        if nome_produto in Franquia[Nome]:
            del Franquia[Nome][nome_produto]
        else:
            print('Nao se encontra no estoque')
            

    if escolha == 3:
         nome_produto = input('Digite o Produto: ')
         if nome_produto in Franquia[Nome]:
            quantidade+= int(input('Digite a quantidade do produto adicionada/removida: '))
         else:
            print("Esse produto n�o est� no estoque")
         Franquia[Nome][nome_produto] = quantidade
    
    if escolha == 4:
        print(Franquia)
    
    if escolha == 5:
        nome_produto = int(input('Digite um produto: '))
        novo_preco = int(input('Digite o novo preco: '))
        estoque[nome_produto]['preco'] = novo_preco
    

    print("Controle de Estoque")
    print("0 - sair",
      "1 - adicionar item",
      "2 - remover item",
      "3 - alterar item",
      "4 - imprimir estoque",
      "5 - Alterar pre�o")

    escolha = int(input("Fa�a sua escolha: "))
    

   
if escolha == 0:
   
    print("at� mais!")


    for coisas in Franquia[Nome]:
    	valor = Franquia[Nome][coisas]['Quantidade']*Franquia[Nome][coisas]['preco']
    	valores += valor
    print('O valor total em estoque �: {0} Reais'.format(valores))


    
    for produtos in estoque:
        if (estoque[produtos]['Quantidade']) < 0:
            negativos.append(produtos)
    print('Os seguintes produtos possuem estoques negativos: ')
    print(negativos)



with open ('Arquivo.txt','w') as arquivo:
    conteudo = json.dumps(estoque, sort_keys=True, indent=4)
    arquivo.write(conteudo)