import os, time

lista = []

class AdicionarItem(object):
    def adiciona_item_final(item) -> list:
        lista.append(item)
        return lista
    
class ApagarItem(object):
    def apaga_item(item) -> list:
        item_removido = lista.remove(item)
        return item_removido
    
class ListarItens(object):
    def lista_itens() -> list:
        indice = 1
        for item in lista:
            print(item)
            indice += 1
        return lista
    
while True:
    opcao = input('\nInserir [i]\nApagar [a]\nVisualizar [v]\nTerminar [t]\n')

    if opcao == 'i':
        os.system('cls')
        while True:
            item = input('Adicionar Item: ')
            
            if item == '0':
                ListarItens.lista_itens()
                time.sleep(1.0)
                break
            
            AdicionarItem.adiciona_item_final(item)


    elif opcao == 'a':
        os.system('cls')

        try: 
            item = input('Apagar Item: ')
            ApagarItem.apaga_item(item)
            print(f'\n{item} foi removido/a da lista.')
            ListarItens.lista_itens()
            time.sleep(1.0)
        except Exception:
            print('Item não encontrado na lita.')

        continue

    elif opcao == 'v':
        os.system('cls')

        if len(lista) == 0:
            print('Lista vazia. Nada para visualizar.')
            time.sleep(1.0)
    
        ListarItens.lista_itens()
        time.sleep(1.0)
        continue

    elif opcao == 't':
        os.system('cls')
        print('Lista concluída')
        ListarItens.lista_itens()
        time.sleep(1.0)
        break

