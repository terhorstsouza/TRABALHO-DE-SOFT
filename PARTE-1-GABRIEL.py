negativos = []
valores = 0
import json



with open ('Arquivo.txt','r') as arquivo:
    conteudo = arquivo.read()
    estoque = json.loads(conteudo)


print('O que deseja fazer?')
print('A - Adicionar loja')
print('B - Acessar loja')
print('C - Excluir loja')

escolha2 = input('Digite sua escolha:  ')

if escolha2 == 'A':
    
    Nome = input('Digite sua loja: ')
    while Nome in estoque:
        print('J� est� Cadastrada')
        Nome = input('Digite sua loja: ')
        
if escolha2 == 'B':
    
    Nome = input('Digite sua loja: ')
    if Nome in estoque:
        print(estoque[Nome])

    else:
        print('Essa loja n�o existe')
	while Nome not in estoque:    
            Nome = input('Digite sua loja: ')

if escolha2 == 'C':
    
    Nome = input('Digite sua loja: ')
    if Nome not in estoque:
        print('Essa loja n�o existe')
        while Nome not in estoque:
           Nome = input('Digite sua loja: ')

print("Controle de Estoque")
print("0 - sair",
      "1 - adicionar item",
      "2 - remover item",
      "3 - alterar item",
      "4 - imprimir estoque",
      "5 - Alterar pre�o")

escolha = int(input("Fa�a sua escolha: "))




while escolha > 0:        
    if escolha == 1:
        nome_produto = input('Digite o Produto: ')
        if nome_produto in estoque[Nome]:
            print('Esse produto j� est� no estoque')
            
        quantidade = int(input('Digite a quantidade do produto: '))
        if quantidade < 0:
            print('A quantidade inicial n�o pode ser negativa')
            break 
        preco = float(input('Digite o pre�o do produto: '))
	if preco < 0:
	    print('A quantidade inicial n�o pode ser negativa')
	    break
        estoque[Nome][nome_produto] = {}
        estoque[Nome][nome_produto]['Quantidade'] = quantidade
        estoque[Nome][nome_produto]['preco'] = preco

    if escolha == 2:
        nome_produto = input('Digite o Produto: ')
        if nome_produto in estoque[Nome]:
            del estoque[Nome][nome_produto]
        else:
            print('Nao se encontra no estoque')
            

    if escolha == 3:
         nome_produto = input('Digite o Produto: ')
         if nome_produto in estoque[Nome]:
            nova_quantidade+= (int(input('Digite a quantidade do produto adicionada/removida: ')))
            estoque[Nome][nome_produto]['Quantidade'] += nova_quantidade 
	 else:
            print("Esse produto n�o est� no estoque")
	    
         
    
    if escolha == 4:
        print(estoque[Nome])
    
    if escolha == 5:
        nome_produto = input('Digite um produto: ')
        novo_preco = float(input('Digite o novo preco: '))
        estoque[Nome][nome_produto]['preco'] = novo_preco
    

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

for coisas in estoque[Nome]:
    valor = (int(estoque[Nome][coisas]['Quantidade']))*(int(estoque[Nome][coisas]['preco']))
    valores += valor
print('O valor total em estoque �: {0} Reais'.format(valores))


    
for produtos in estoque[Nome]:
    if (estoque[Nome][produtos]['Quantidade']) < 0:
       	negativos.append(produtos)
print('Os seguintes produtos possuem estoques negativos: ')
print(negativos)



with open ('Arquivo.txt','w') as arquivo:
    conteudo = json.dumps(estoque, sort_keys=True, indent=4)
    arquivo.write(conteudo)