produtos = []

class Produto:
    def _init_(self, nome, preco):
        self.nome = nome
        self.preco = preco
     
def cadastrarProdutos():
    while True:
        try: 
            nome = input("Digite o nome do produto: ")
            if nome == (""):
                print ("Nome inválido.")
                return
            preco = float(input("Digite o preço do produto: ")) 
            if preco <= 0:
                print ("Preço Inválido.")
                return
        except ValueError:
            print ("Preço Inválido.")
            return 
        
        produto = Produto(nome, preco)
        produtos.append(produto)
        print ("Produto Cadastrado Com Sucesso!")
        
        resposta = input("Deseja cadastrar mais produtos? (sim/não) \n")
        if resposta.lower() == "sim":
            continue
        else: 
            return
            
                 
def mostrarProdutos():
    if produtos == []:
        print ("Não há produtos cadastrados.")
        return
    else:
        for i, produto in enumerate(produtos):
            print (f"produto {i + 1}: {produto.nome} - preço: {produto.preco}")           

def comprarProdutos():
    while True:
        try:
            i = int(input("Digite o número do produto desejado: "))
            produto = produtos[i - 1]
            quantidade = int(input("Digite a quantidade desejada: "))
            if quantidade <= 0:
                print ("Quantidade inválida")
                return
        except (ValueError, IndexError): 
            print ("Produto Inválido, tente novamente.")
            return
            
        total = produto.preco * quantidade
        if total >= 100:
            print (f"Desconto disponível.\nO total a ser pago por {quantidade} unidades de {produto.nome} é de R$ {total * 0.90}")
        else:
            print (f"Sem desconto. \nO total a ser pago por {quantidade} unidades de {produto.nome} é de R$ {total}")       
        resposta = input("Deseja comprar mais produtos? (sim/não) \n")
        if resposta.lower() == "sim":
            continue
        else: 
            return

def Menu():    
    while True:
        try: 
            opcao = int(input( "Opção 1 - Cadastrar Produtos\nOpção 2 - Mostrar Produtos\nOpção 3 - Comprar Produtos\nOpção 4 - Sair do Programa\n\nDigite a opção desejada: "))    
            if opcao == 1:
                cadastrarProdutos()        
            elif opcao == 2:
                mostrarProdutos()      
            elif opcao == 3:
                comprarProdutos()      
            elif opcao == 4:
                print ("Programa Encerrado")
                break 
            else:
                print ("Opção Inválida.")
        except ValueError:
            print ("Opção inválida.")
            continue 
Menu()
