class LojaAbstrata:
    def criaProdutoEletronico(self):
        pass
    def criaProdutoModa(self):
        pass


class lojaVirtual(LojaAbstrata):
    def criaProdutoEletronico(self):
        return Telefone()

    def criaProdutoModa(self):
        return Camiseta()


class LojaFisica(LojaAbstrata):
    def criaProdutoEletronico(self):
        return Telefone()

    def criaProdutoModa(self):
        return Camiseta()
    

class ProdutoEletronico:
    def __init__(self):
        self.tipo = "eletronico"
    
    def descricao(self):
        return f"Produto {self.tipo}: Telefone"
    
class ProdutoModa:
    def __init__(self):
        self.tipo = "moda"

    def descricao(self):
        return f"Produto {self.tipo}: Camiseta"
    

class Telefone(ProdutoEletronico):
    def descricao(self):
        return f"Produto: {self.tipo}: Telefone"
    
class Camiseta(ProdutoModa):
    def descricao(self):
        return f"Produto {self.tipo}: Camiseta"
    
def loja(cliente, loja):
    LojaFisica = loja.criaProdutoEletronico()
    LojaVirtual = loja.criaProdutoEletronico()

    print(f"{cliente} Comprou:")
    print(LojaFisica.descricao())
    print(LojaFisica.descricao())


cliente1 = "Joao da Silva"
LojaFisica = LojaFisica()
loja(cliente1, LojaFisica)

print("n\...\n")

cliente2 = "Maria da Silva"
lojaVirtual = lojaVirtual()
loja(cliente2, lojaVirtual)