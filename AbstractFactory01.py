# 1 Interface da Abstract Factory:
class AbstractFactory:
    def criaProdutoA(self):
        pass
    def criaProdutoB(self):
        pass

# 1 Fabrica 1 Concreta que Cria Produto do Tipo A e B:

class FabricaConcreta1(AbstractFactory):
    def criaProdutoA(self):
        return ProdutoConcretoA1()
    
    def criaProdutoB(self):
        return ProdutoConcretoB1()
    


# 1 Fabrica 2 Concreta que Cria Produto do Tipo A e B:
class FabricaConcreta2(AbstractFactory):
    def criaProdutoA(self):
        return ProdutoConcretoA2()
    
    def criaProdutoB(self):
        return ProdutoConcretoB2()

# 2 Interface dos Produtos do Tipo A:
class ProdutoAbstratoA:
    def metodoA(self):
        pass
# 2 Implementação Concreta do Produto do Tipo A - Fabrica 1:
class ProdutoConcretoA1(ProdutoAbstratoA):
    def metodoA(self):
        return "Produto do Tipo A da Fabrica 1"
# 2 Implementação Concreta do Produto do Tipo A - Fabrica 2:
class ProdutoConcretoA2(ProdutoAbstratoA):
    def metodoA(self):
        return "Produto do tipo A da fabrica 2"
# 3 Interface dos Produtos do Tipo B:
class ProdutoAbstratoB:
    def metodoB(self):
        pass
# 3 Implementação Concreta do Produto do Tipo B - Fabrica 1:
class ProdutoConcretoB1(ProdutoAbstratoB):
    def metodoB(self):
        return "Produto do tipo B da fabrica 1"
# 3 Implementação Concreta do Produto do Tipo B - Fabrica 2:
class ProdutoConcretoB2(ProdutoAbstratoB):
    def metodoB(self):
        return "Produto do tipo B da fabrica 2"

# 4 USO DO PADRÃO ABSTRACT FACTORY - IMPLEMENTAÇÃO:
def clienteCod(factory):
    produtoA = factory.criaProdutoA()
    produtoB = factory.criaProdutoB()

    print(produtoA.metodoA())
    print(produtoB.metodoB())

# Exemplo de uso da Fabrica 1:
factory1 = FabricaConcreta1()
clienteCod(factory1)

# Exemplo de uso da Fabrica 2:
factory2 = FabricaConcreta2()
clienteCod(factory2)