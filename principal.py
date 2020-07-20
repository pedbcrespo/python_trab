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
    print('\n')
    for elem in lst:
        for camp in elem:
            print(camp + ':', elem[camp])
        print('\n')


# Funçoes auxiliares

def menu():
    print('''
    1. Inserir jogo
    2. Remover
    3. Imprimir
    4. Recentes
    5. Abaixos de valor x
    6. Mesma desenvolvedora
    7. Acima de valor x
    8. #Fazer
    0.sair
            '''
          )
    return int(input())


def opcoes(op):
    if op == 1:  # insere
        insere(
            {
                'nome': input('nome: '),
                'empresa': input('empresa: '),
                'lancamento': int(input('lancamento: ')),
                'genero': input('genero: '),
                'plataformas': lista_empresa(),
                'avaliacao': float(input('avaliacao: ')),
                'preco_medio': float(input('preco: '))
            }, lista)
    if op == 2:  # remove
        remove(busca(input('jogo: '), lista), lista)
    if op == 3:  # imprime
        imprime(lista)
    if op == 4:  # lista de jogos mais recentes
        imprime(recentes(lista))
    if op == 5:  # lista de jogos abaixo de X preco
        pass
    if op == 6:  # lista de jogos de um mesmo desenvolvedor
        pass
    if op == 7:  # lista de jogos acima de faixa de preco
        pass
    if op == 8:  # avaliar determinado jogo
        pass


def lista_empresa():
    lista = []
    while True:
        lista.append(input('plataforma: '))
        op = int(input('1.add\n0.sair\n'))
        if not op:
            break
    return lista


def busca(nome, lst):
    for elem in lst:
        if elem['nome'] == nome:
            return elem


# Funçoes Criativas
def recentes(lst):
    atual = datetime.date.today()
    return [elem for elem in lst if elem['lancamento'] == atual.year]


lista = func_dados.carregar_jogos()

# __MAIN__:
while True:
    op = menu()
    if op == 0:
        break
    else:
        opcoes(op)
