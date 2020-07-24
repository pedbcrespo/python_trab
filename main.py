import datetime
import func_dados


'''
    func_dados.salvar_usuarios('lista_usuarios') => salva usuarios no arquivo
    func_dados.salvar_jogos('lista_jogos') => salva jogos no arquivo
'''

#FUNÇÕES TRY EXCEPT
#A vantagem de usar try except é que uma operação como int(variavel) pode parar a exercução do programa :p

#Função para checar se é inteiro
def e_int(a):
    try:
        int(a)
        return True
    except ValueError:
        return False

#Função para checar se é float
def e_float(a):
    try:
        float(a)
        return True
    except ValueError:
        return False

#Função para gerar um ID para o jogo (perdi)
def ID_Gerador(lst):
    # Começa zerado
    IDvago = 0
    #Procura o ID de maior valor
    for i in range (0, len(lst)):
        if (lst[i]['ID'] > IDvago):
            IDvago = lst[i]['ID']
    #Garante que o ID gerador é uma unidade acima do maior ID criando um novo
    IDvago = IDvago + 1
    return IDvago

#Inserir
def insere(jogo, lst):
    lst.append(jogo)

#Remover
#não ta funcionando
def remove(lst, ID):
    for elem in lst:
        print(type(ID))
        print(type(elem['ID']))
        print(ID)
        print(elem['ID'])
        if elem['ID'] == ID:
            lst.remove(elem)
            print("Removido")
    return lst

def imprime(lst):
    for elem in sorted(lst, key=lambda lst: lst['ID']):
        for camp in elem:
            print(camp + ':', elem[camp])
        print('\n')

# Funçoes relacionadas a menu
def menu():
    print('''
    1. Inserir jogo
    2. Remover
    3. Imprimir
    4. Lista sob condicao
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
    lista = set(func(lambda elem: True))
    for elem in sorted(list(lista)):
        print('{}. {}'.format(i, elem))
        i += 1

    return int(input())-1, sorted(list(lista))

def ano():
    numero = 0
    Operador = False
    while (Operador == False):
        numero = input("Digite um ano válido: ")
        if (e_int(numero) == True):
            Operador = True
    return numero

def lista_empresa():
    lista = []
    while True:
        lista.append(input('Plataforma: '))
        Operador = False
        while (Operador == False):
            op = input('1.Continuar adicionando\n0.Prosseguir\n')
            if (e_int(op) == True):
                Operador = True
        if (Operador):
            break
    return lista

def review():
    numero = 0
    Operador = False
    while (Operador == False):
        numero = input("Digite uma avaliação válida: ")
        if (e_int(numero) == True):
            numero = float(numero)
            Operador = True
            if (numero < 0 or numero > 100):
                Operador = False
                print("Entre 0 e 100")
    return numero

def preco():
    numero = 0
    Operador = False
    while (Operador == False):
        numero = input("Digite um ano válido: ")
        if (e_float(numero) == True):
            Operador = True
    return numero

def busca(lst, param, ident):
    for elem in lst:
        if elem[param] == ident:
            return elem
    return None

def lista_filtrada(lista):
    return lambda camp: lambda condicao: [elem[camp] for elem in lista if condicao(elem)] 


lista_jogos = func_dados.carregar_jogos()
lista_usuarios = func_dados.carregar_usuarios()

filtrada = lista_filtrada(lista_jogos)
jogos_filtrados = filtrada('nome')
empresas_filtradas = filtrada('empresa')
generos_filtrados = filtrada('genero')

if __name__ == '__main__':
    while True:
        op = menu()
        lst = []
        
        # sair 
        if op == 0:
            break
        
        # insere
        if op == 1:  
            #Apenas Inicializando
            jogo = {"nome": "The Elder Scrolls: Skyrim",'empresa': "Bethesda",'lancamento': 2011,'genero': 'RPG',        'plataformas': ['PS3', 'PS4', 'PC', 'XBOX 360', 'XBOX ONE'],        'avaliacao':95.6,        'preco_medio':100.5}
            jogo['ID'] = ID_Gerador(lst)
            jogo['nome'] = input('Nome: ')
            jogo['empresa'] = input('Empresa: ')
            jogo['lancamento'] = ano()
            jogo['genero'] = input('Gênero: ')
            jogo['plataformas'] = lista_empresa()
            jogo['avaliacao'] = review()
            jogo['preco_medio'] = preco()
            lst.append(jogo)
        
        # remove
        if op == 2:  
            operador = False
            while (operador == False):
                numero = input("Insira o ID do jogo que deseja remover do sistema: ")
                if (e_int(numero) == True):
                    enviar = int(numero)
                    operador = True
            lst = remove(lst, enviar)
        
        # imprime
        if op == 3:  
            imprime(lst)

        # lista sob condicao
        if op == 4: 
            op2 = sub_menu_lista()

            #Lista de jogos em determinado ano
            if op2 == 1:
                ano = input('ano: ')
                if ano == '':
                    ano = datetime.date.today().year
                print(jogos_filtrados(lambda elem: elem['lancamento']==int(ano)))
            
            #Lista de jogos de determinado periodo
            elif op2 == 2:
                ano1 = input('ano inicio: ')
                ano2 = input('ano fim: ')
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
                print(jogos_filtrados(lambda elem: elem['empresa'] == list(lst)[opc]))

            #Lista de jogos de um mesmo genero
            elif op2 == 6:
                opc,lst = sub_opc(generos_filtrados)
                print(jogos_filtrados(lambda elem: elem['genero'] == list(lst)[opc]))
        