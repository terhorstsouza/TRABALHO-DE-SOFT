negativos = []
valores = 0
from firebase import firebase

#abrindo o arquivo 
database = firebase.FirebaseApplication("https://ep-d-soft.firebaseio.com/",None)
estoque = database.get("/estoque/loja", None)
if estoque == None:
    estoque = {}
#HUB de escolhas
print('O que deseja fazer?')
print('A - Adicionar loja')
print('B - Acessar loja')
print('C - Excluir loja')

escolha2 = input('Digite sua escolha:  ')

if escolha2 == 'A':
    
    Nome = input('Digite sua loja: ')
    if Nome in estoque:
        print('Já está Cadastrada')
        Nome = input('Digite sua loja: ')
        
if escolha2 == 'B':
    Nome = input('Digite sua loja: ')
    if Nome in estoque:
        print(estoque[Nome])
    else:
        print('Não está cadastrada')
        while Nome not in estoque: 
            Nome = input('Digite uma loja: ')
            



if escolha2 == 'C':
    Nome = input('Digite sua loja: ')
    if Nome not in estoque:
        print('Essa loja não existe')
        while Nome not in estoque:
           Nome = input('Digite sua loja: ')
    else:
        del estoque[Nome]
        
if Nome not in estoque:
    estoque[Nome] = {}        
        
#HUB de estoque        
print("Controle de Estoque")
print("0 - sair")
print("1 - adicionar item")
print("2 - remover item")
print("3 - alterar item")
print("4 - imprimir estoque")
print("5 - Alterar preço")
    
escolha = int(input("Faça sua escolha: "))
    


    
    
while escolha > 0: 
           
    #Adicionar produtos
        
    if escolha == 1:
        nome_produto = input('Digite o Produto: ')
        if nome_produto in estoque[Nome]:
            print('Esse produto já está no estoque')
                
                
        quantidade = int(input('Digite a quantidade do produto: '))
        if quantidade < 0:
            print('A quantidade não pode ser negativa')
            break  
        preco = float(input('Digite o Preço Unitário do produto: '))
        if preco < 0:
            print('O preço não pode ser negativo')
            break    
        estoque[Nome][nome_produto] = {}
        estoque[Nome][nome_produto]['Quantidade'] = quantidade
        estoque[Nome][nome_produto]['preco'] = preco
    #Removendo do estoque
    
    if escolha == 2:
        nome_produto = input('Digite o Produto: ')
        if nome_produto in estoque[Nome]:
            del estoque[Nome][nome_produto]
        else:
            print('Nao se encontra no estoque')
                
        
    #alterar produtos        
    
    if escolha == 3:
        nome_produto = input('Digite o Produto: ')
        if nome_produto in estoque[Nome]:
            nova_quantidade = (int(input('Digite a quantidade do produto adicionada/removida: ')))
            estoque[Nome][nome_produto]['Quantidade'] += nova_quantidade
        else:
            print('Elemento não encontrado')
            
            
    
    #Imprimir estoque
        
    if escolha == 4:
        print(estoque[Nome])
        
    #Alterar preço
        
    if escolha == 5:
        nome_produto = input('Digite um produto: ')
        novo_preco = float(input('Digite o novo preco: '))
        estoque[Nome][nome_produto]['preco'] = novo_preco
    
    
    #volta ao HUB
    
    print("Controle de Estoque")
    print("0 - sair",
          "1 - adicionar item",
          "2 - remover item",
          "3 - alterar item",
          "4 - imprimir estoque",
          "5 - Alterar preço")
    
    escolha = int(input("Faça sua escolha: "))
        
    
        
    #Encerra o programa
    
if escolha == 0:
    print("até mais!")
    novo_estoque = database.patch("/estoque/lojas/", estoque)
    #Imprime o valor total em estoque
    
for coisas in estoque[Nome]:

    valor = (int(estoque[Nome][coisas]['Quantidade']))*(int(estoque[Nome][coisas]['preco']))
    valores += valor
print('O valor total em estoque é: {0} Reais'.format(valores))
    
    #Imprime os produtos negativos
    
        
for produtos in estoque[Nome]:
    if (estoque[Nome][produtos]['Quantidade']) < 0:
        negativos.append(produtos)
print('Os seguintes produtos possuem estoques negativos: ')
print(negativos)



    
#encerrando e salvando o arquivo

