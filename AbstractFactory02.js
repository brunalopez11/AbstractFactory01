// Interface da Fabrica Abstrata:
class LojaAbstrata{
    criaProdutoEletronico(){}
    criaProdutoModa(){}
}
 
// Fabrica Concreta para Criar Produtos - Loja Fisica:
class LojaFisica extends LojaAbstrata{
    criaProdutoEletronico(){
        return new Telefone();
    }
 
    criaProdutoModa(){
        return new Camiseta();
    }
}
 
// Fabrica Concreta para Criar Produtos - Loja Virtual:
class LojaVirtual extends LojaAbstrata{
    criaProdutoEletronico(){
        return new Telefone();
    }
 
    criaProdutoModa(){
        return new Camiseta();
    }
}
 
// Classe Abstrata para Produtos Eletronicos:
class ProdutoELetronico{
    constructor(){
        this.tipo = "eletronico";
    }
 
    descricao(){
        return `Produto ${this.tipo}: Telefone`;
    }
}
 
// Classe Abstrata paraa Produtos de Moda:
class ProdutoModa{
    constructor(){
        this.tipo = "Moda";
    }
 
    descricao(){
        return `Produto ${this.tipo}: Camisa`;
    }
}
 
// Classe Concreta Para Produtos Eletronicos:
class Telefone extends ProdutoELetronico{
    descricao(){
        return `Produto ${this.tipo}: Telefone`;
    }
}
 
// Classe Concreta Para Produtos De Moda:
class Camiseta extends ProdutoELetronico{
    descricao(){
        return `Produto ${this.tipo}: Camiseta`
    }
}
 
//Interface de simulação da loja:
function lojaI(cliente, loja){
    const lojaFisica = loja.criaProdutoEletronico();
    const lojaVirtual = loja.criaProdutoModa();
   
    console.log(`${cliente} Comprou:`);
    console.log(lojaFisica.descricao());
    console.log(lojaVirtual.descricao());
}
 
//Aplicação da venda simulada:
const cliente1 = "João da Silva";
const lojaFisica = new LojaFisica();
lojaI(cliente1, lojaFisica);
 
console.log("-------------------------------------------------");
 
const cliente2 = "Maria Oliveira";
const lojaVirtual = new LojaVirtual();
lojaI(cliente2, lojaVirtual);
