import datetime
import func_dados


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


# Funçoes basicas

def insere(jogo, lst):   
    jogo["id"] = verifica_id(lst, len(lst)+1)
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

def input_empresa():
    lista = []
    while int(input('1.add\n0.sair\n')) != 0:
        lista.append(input('plataforma: '))
    return lista

def verifica_id(lst, id):
    alt = 0
    for elem in lst:
        if id == elem['id']:
            alt += 1
    return id + alt        

def busca(lst, param, ident):
    for elem in lst:
        if elem[param] == ident:
            return elem

def lista_filtrada(lista):
    return lambda param: lambda condicao: [elem[param] for elem in lista if condicao(elem)] 




lista_jogos = func_dados.carregar_jogos()
lista_usuarios = func_dados.carregar_usuarios()

filtrada = lista_filtrada(lista_jogos)
jogos_filtrados = filtrada('nome')
empresas_filtradas = filtrada('empresa')


# __MAIN__:
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
        print(jogos_filtrados(lambda elem: elem['lancamento']==int(ano)))

    #lista de jogos de um determinado periodo
    elif op == 5: 
        ano1 = input('periodo 1: ')
        ano2 = input('periodo 2: ')
        if ano2 == '':
            ano2 = ano = datetime.date.today().year
        print(jogos_filtrados(lambda elem: elem['lancamento'] >= int(ano1) and elem["lancamento"] <= int(ano2)))


    #lista de jogos abaixo de determinado preco
    elif op == 6:
        valor = float(input("valor: "))
        print(jogos_filtrados(lambda elem: elem["preco_medio"] <= valor))
    
    #lista de jogos acima de determinado preco
    elif op == 7:  
        valor = float(input("valor: "))
        print(jogos_filtrados(lambda elem: elem["preco_medio"] >= valor))
    
    #lista jogos de uma mesma empresa
    elif op == 8:
        i = 1  
        print('Sub menu:')
        l_emp = set(empresas_filtradas(lambda elem: True))
        for elem in l_emp:
            print(i, elem)
            i += 1
        opc = int(input())    
        print(jogos_filtrados(lambda elem: elem['empresa'] == list(l_emp)[opc-1]))

    #avaliar determinado jogo
    elif op == 9:
        pass
    
    #favoritos
    elif op == 10:
        pass

    #sair
    else:
        break