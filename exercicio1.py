class Produto:
    def __init__(self, codigo, nome, quantidade, preco_unitario):
        self.codigo = codigo 
        self.nome = nome
        self.quantidade = quantidade
        self.preco_unitario = preco_unitario
        
    def exibir(self):
        print (f"Codigo do produto: {self.codigo}\nNome: {self.nome}\nQuantidade: {self.quantidade}\nPreço Unitário: R$: {self.preco_unitario}")

produto = Produto(101, "Tomate", 1, 5.00)
produto.exibir()