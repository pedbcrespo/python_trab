import datetime
import operator
import func_dados


# Funçoes basicas

def insere(jogo, lst):
    jogo["id"] = len(lst)+1
    lst.append(jogo)
    func_dados.salvar_jogos(lst)

def remove(jogo, lst):
    lst.remove(jogo)
    func_dados.salvar_jogos(lst)

def imprime(lst):
    for elem in lst:
        for camp in elem:
            print(camp + ':', elem[camp])
        print('\n')

# Funçoes auxiliares

def menu():
    print('''
    1. Inserir jogos
    2. Remover jogos
    3. Imprimir jogos
    4. Lista de jogos em determinado ano
    5. Lista de jogos de determinado periodo
    6. Lista de jogos abaixo de determinado preco
    7. Lista de jogos acima de determinado preco
    8. Lista jogos de uma mesma empresa
    9. Avaliar determinado jogo
    0.sair
            '''
          )
    return int(input())

def input_empresa():
    lista = []
    while True:
        lista.append(input('plataforma: '))
        op = int(input('1.add\n0.sair\n'))
        if not op:
            break
    return lista


def busca(param, nome, lst):
    for elem in lst:
        if elem[param] == nome:
            return elem


def lista_empresas(lista):
    lst_empresas = []
    i = 1
    for elem in lista:
        if elem['empresa'] in lst_empresas:
            continue
        else:
            lst_empresas.append({str(i): elem['empresa']})
        i += 1    
    return lst_empresas

# Funçoes Criativas
def lista_filtrada(lista, condicao):
    return [elem['nome'] for elem in lista if condicao(elem)] 


# __MAIN__:


lista_jogos = func_dados.carregar_jogos()
lista_usuarios = func_dados.carregar_usuarios()

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
                'plataformas': input_empresa(),
                'avaliacao': float(input('avaliacao: ')),
                'preco_medio': float(input('preco: '))
            }, lista_jogos)
    
    #remover jogo
    elif op == 2:  
        remove(busca("nome", input('jogo: '), lista_jogos), lista_jogos)
    
    #imprimir jogos
    elif op == 3:  
        imprime(lista_jogos)
    

    #lista de jogos em determinado ano
    elif op == 4: 
        
        ano = input('ano: ')
        if ano == '':
            ano = ano=datetime.date.today().year
        print(lista_filtrada(lista_jogos, lambda elem: elem['lancamento']==int(ano)))

    #lista de jogos de um determinado periodo
    elif op == 5: 
        ano1 = input('periodo 1: ')
        ano2 = input('periodo 2: ')
        if ano2 == '':
            ano2 = ano=datetime.date.today().year
        print(lista_filtrada(lista_jogos, lambda elem: elem['lancamento'] >= int(ano1) and elem["lancamento"] <= int(ano2)))


    #lista de jogos abaixo de determinado preco
    elif op == 6:
        valor = float(input("valor: "))
        print(lista_filtrada(lista_jogos, lambda elem: elem["preco_medio"] <= valor))
    
    #lista de jogos acima de determinado preco
    elif op == 7:  
        valor = float(input("valor: "))
        print(lista_filtrada(lista_jogos, lambda elem: elem["preco_medio"] >= valor))
    
    #lista jogos de uma mesma empresa
    elif op == 8:  
        print('Sub menu:')
        lst_emp = lista_empresas(lista_jogos)
        imprime(lst_emp)
        id_emp = int(input())
        print(lista_filtrada(lista_jogos, lambda elem: elem['empresa'] == lst_emp[id_emp-1][str(id_emp)]))
    #avaliar determinado jogo
    elif op == 9:
        pass
    
    #favoritos
    elif op == 10:
        pass

    #sair
    else:
        break