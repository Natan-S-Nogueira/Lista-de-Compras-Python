# Lsita de Compras em Python

O objetivo deste projeto é criar e manipular uma lista de compras, podendo adicionar e remover itens da lista.

### 📋 Pré-requisitos

Para executar o arquivo será necessário que o usuário possua a versão mais recente do Python, que pode ser baixada [aqui](https://www.python.org/downloads/).

### Execução

Caso esteja utilizando VSCode ou qualquer outro editor e não possua a extenção para rodar um programa .py instalada, abra o terminal no programa e digite python ListaDeCompras.py para iniciar o programa.

O programa mostrará no terminal a seguinte mensagem:

```
Inserir [i]
Apagar [a]
Visualizar [v]
Terminar [t]
```

Inserir [i]: ativa o loop while para inserir um ou vários intens na lista através da função adiciona_item_final(item). Após isso, digite o nome do item que deseja adicionar, caso queira sair do loop digite 0.

Apagar [a]: ativa a função apaga_item(). Após isso, digite o nome do item que deseja apagar e caso ele não esteja na lista, uma exeção será mostrada no terminal.

Visualizar [v]: ativa a função lista_itens(). Após isso, a função irá retornar a lista no terminal, caso ela esteja vazia o terminal mostrará uma mensagem dizendo que ela está vazia.

Terminar [t]: retorna a lista no terminal e encerra o programa.

As classes e métodos são: 

AdicionarItem:
```
class AdicionarItem(object):
    def adiciona_item_final(item) -> list:
        lista.append(item)
        return lista
```

ApagarItem:
```
class ApagarItem(object):
    def apaga_item(item) -> list:
        item_removido = lista.remove(item)
        return item_removido
```

ListarItens:
```
class ListarItens(object):
    def lista_itens() -> list:
        indice = 1
        for item in lista:
            print(item)
            indice += 1
        return lista
```

## ✒️ Autores

* **Natan Nogueira** - *Código + Documentação* - [Natan Nogueira](https://github.com/Natan-S-Nogueira)

