import datetime
import func_dados

'''
    Para salvar usuarios no arquivo, tem a funçao:
    func_dados.salvar_usuarios('lista_de_usuarios')
'''


def menu():
    print('''
    1. Inserir jogos
    2. Remover jogos
    3. Imprimir jogos
    4. Lista de jogos por criterio
    9. Avaliar determinado jogo
    0.sair
            '''
          )
    return int(input())

def sub_menu_lista():
    print('''
        1. Lista de jogos em determinado ano
        2. Lista de jogos de determinado periodo
        3. Lista de jogos abaixo de determinado preco
        4. Lista de jogos acima de determinado preco
        5. Lista de jogos de uma mesma empresa
        6. Lista de jogos de um mesmo genero
            '''
        )
    return int(input())


def sub_opc(func):
    i = 1  
    lst = set(func(lambda elem: True))
    for elem in lst:
        print(i, elem)
        i += 1
    opc = int(input())
    return opc, lst 
# Funçoes basicas

def insere(jogo, lst):   
    jogo["id"] = int(str(jogo['lancamento'])+str(len(jogo['empresa']))+str(len(lst)+1))
    lst.append(jogo)
    func_dados.salvar_jogos(lst)

def remove(jogo, lst):
    lst.remove(jogo)
    func_dados.salvar_jogos(lst)

def imprime(lst):
    for elem in lst:
        for camp in elem:
            print('{}: {}'.format(camp, elem[camp]))
        print('\n')


# Outras Funçoes nem tao basicas assim

def input_plataforma():
    lista = []
    while int(input('1.add\n0.sair\n')) != 0:
        lista.append(input('plataforma: '))
    return lista

def busca(lst, param, ident):
    for elem in lst:
        if elem[param] == ident:
            return elem
    return None

def lista_filtrada(lista):
    return lambda param: lambda condicao: [elem[param] for elem in lista if condicao(elem)] 




lista_jogos = func_dados.carregar_jogos()
lista_usuarios = func_dados.carregar_usuarios()

filtrada = lista_filtrada(lista_jogos)
jogos_filtrados = filtrada('nome')
empresas_filtradas = filtrada('empresa')
generos_filtrados = filtrada('genero')

# __MAIN__:

if __name__ == '__main__':
    while True:
        op = menu()
        #inserir jogo
        if op == 1:  
            insere(
                {
                    'nome': input('nome: '),
                    'empresa': input('empresa: '),
                    'lancamento': int(input('lancamento: ')),
                    'genero': input('genero: '),
                    'plataformas': input_plataforma(),
                    'avaliacao': float(input('avaliacao: ')),
                    'preco_medio': float(input('preco: '))
                }, lista_jogos)
        
        #remover jogo
        elif op == 2:
            elem = busca(lista_jogos, "nome", input('jogo: '))
            if  elem != None:
                remove(elem, lista_jogos)
            else:
                print('Elemento inexistente')
        #imprimir jogos
        elif op == 3:  
            imprime(lista_jogos)  

        #lista de jogos por criterio
        elif op == 4: 

            op2 = sub_menu_lista()
            #Lista de jogos em determinado ano
            if op2 == 1:
                ano = input('ano: ')
                if ano == '':
                    ano = ano=datetime.date.today().year
                print(jogos_filtrados(lambda elem: elem['lancamento']==int(ano)))
            
            #Lista de jogos de determinado periodo
            elif op2 == 2:
                ano1 = input('periodo 1: ')
                ano2 = input('periodo 2: ')
                if ano2 == '':
                    ano2 = ano = datetime.date.today().year
                print(jogos_filtrados(lambda elem: elem['lancamento'] >= int(ano1) and elem["lancamento"] <= int(ano2)))
            
            #Lista de jogos abaixo de determinado preco
            elif op2 == 3:
                valor = float(input("valor: "))
                print(jogos_filtrados(lambda elem: elem["preco_medio"] <= valor))
            
            #Lista de jogos acima de determinado preco
            elif op2 == 4:
                valor = float(input("valor: "))
                print(jogos_filtrados(lambda elem: elem["preco_medio"] >= valor))
            
            #Lista de jogos de uma mesma empresa
            elif op2 == 5:
                opc,lst = sub_opc(empresas_filtradas)  
                print(jogos_filtrados(lambda elem: elem['empresa'] == list(lst)[opc-1]))
            
            #Lista de jogos de um mesmo genero
            elif op2 == 6:
                opc,lst = sub_opc(generos_filtrados)
                print(jogos_filtrados(lambda elem: elem['genero'] == list(lst)[opc-1]))
            

        #
        elif op == 5: 
            pass

        #
        elif op == 6:
            pass
        
        #
        elif op == 7:  
            pass
        
        #
        elif op == 8:
            pass

        #
        elif op == 9:
            pass
        
        #
        elif op == 10:
            pass

        #sair
        else:
            break