import datetime
import func_dados


'''
    func_dados.salvar_usuarios('lista_usuarios') => salva usuarios no arquivo
    func_dados.salvar_jogos('lista_jogos') => salva jogos no arquivo
'''

lista_jogos = func_dados.carregar_jogos()
lista_usuarios = func_dados.carregar_usuarios()

# Funcoes Pedro

# Funçoes relacionadas a menu
def menu(opcao):
    print(opcao)
    return int(input())

def sub_opc(func):
    i = 1
    lista = set(func(lambda elem: True))
    for elem in sorted(list(lista)):
        print('{}. {}'.format(i, elem))
        i += 1

    return int(input())-1, sorted(list(lista))

def busca(lst, param, ident):
    for elem in lst:
        if elem[param] == ident:
            return elem
    return None

def lista_filtrada(lista):
    return lambda camp: lambda condicao: [elem[camp] for elem in lista if condicao(elem)] 

filtrada = lista_filtrada(lista_jogos)
jogos_filtrados = filtrada('nome')
empresas_filtradas = filtrada('empresa')
generos_filtrados = filtrada('genero')


# Funcoes Gummy
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
        if input('1.Continuar adicionando\n0.Prosseguir\n') == '0':
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
        numero = input("Digite um preco válido: ")
        if (e_float(numero) == True):
            Operador = True
    return numero


# Funcoes Ruivo

def menu_usuario(lista_jogos):
            user = input("\tDigite o seu nome de usuario ou escreva ""ADD"" Para adicionar um novo usuario:  ")
            op2 = 1
            favorito = []
            
            if(user == "ADD"):
                a = 0
                
                while a == 0:
                    a = 1
                    user = input("Digite o nome de usuario: ")
                    for i in range (0, len(lista_usuarios)):
                        if user == lista_usuarios[i]['Nome']:
                            print("Nome de Usuario já existente")
                            a = 0
               
                favorito = criafav(lista_jogos, [])                     

                usuario = {
                    "Nome": user,
                    "Jogos": favorito
                }
                lista_usuarios.append(usuario)
                func_dados.salvar_usuarios(lista_usuarios)

            else:
                existente = 0
                for i in range(0,len(lista_usuarios)):
                    if user == lista_usuarios[i]['Nome']:
                        favorito = lista_usuarios[i]['Jogos']
                        existente = 1
                
                if existente == 1:

                    favorito = criafav(lista_jogos, favorito)        
                    usuario = {
                        "Nome": user,
                        "Jogos": favorito
                    }
                    lista_usuarios[i] = usuario
                    func_dados.salvar_usuarios(lista_usuarios)
                else:
                    print("Usuario Ainda não cadastrado")


def pesquisaID(lista_jogos, x):         
    for i in range(0,len(lista_jogos)):                
        if int(lista_jogos[i]['id']) == x:
            return i

    return -1

def pesquisaNome(lista_jogos, x):          
    for i in range(0,len(lista_jogos)):                
        if lista_jogos[i]['nome'] == x:
            return i
    
    return -1

def criafav(lista_jogos, favorito):
    op2 = 1

    while op2 != 5:

        op2 = int(input("\t1 - Adicionar um jogo a SUA lista\n\t2 - Remover um  jogo\n\t3 - Imprimir TODOS Jogos\n\t4 - Imprimir SUA lista de jogos\n\t5 - Sair\n"))

        if op2 == 1:
            jogo = input("Digite o nome do jogo: ")
            i=pesquisaNome(lista_jogos, jogo)
            if i == -1:
                print("Jogo não encontrado")
            else:
                favorito.append(lista_jogos[i]['id'])
                print("Jogo ", lista_jogos[i]['nome'], "Adicionado a sua lista")

        elif op2 == 2:
            jogo = input("Digite o nome do jogo que deseja remover: ")
            i = pesquisaNome(lista_jogos, jogo)
            try:
                favorito.remove(lista_jogos[i]['id'])
                print("Jogo Removido")
            except:
                print("Jogo não esta na sua Lista")

        elif op2 == 3:
            imprime(lista_jogos)  

        elif op2 == 4:
            for i in range(0,len(favorito)):
                print(lista_jogos[pesquisaID(lista_jogos, favorito[i])])

    return favorito



id_jogos = len(lista_jogos) + 1
id_usuarios = len(lista_usuarios) + 1


if __name__ == '__main__':
    while True:
        op = menu('''
    1. Inserir jogo
    2. Remover
    3. Imprimir
    4. Lista sob condicao
    5. Usuario
    0.sair
            ''')
        
        # sair 
        if op == 0:
            break
        
        # insere
        elif op == 1:  
            #Apenas Inicializando
            jogo = {}
            jogo['ID'] = id_jogos
            jogo['nome'] = input('Nome: ')
            jogo['empresa'] = input('Empresa: ')
            jogo['lancamento'] = ano()
            jogo['genero'] = input('Gênero: ')
            jogo['plataformas'] = lista_empresa()
            jogo['avaliacao'] = review()
            jogo['preco_medio'] = preco()
            lista_jogos.append(jogo)
            func_dados.salvar_jogos(lista_jogos)
            id_jogos += 1
        
        # remove
        elif op == 2:  
            operador = False
            while (operador == False):
                numero = input("Insira o ID do jogo que deseja remover do sistema: ")
                if (e_int(numero) == True):
                    enviar = int(numero)
                    operador = True
            lista_jogos = remove(lista_jogos, enviar)
            func_dados.salvar_jogos(lista_jogos)
        # imprime
        elif op == 3:  
            imprime(lista_jogos)

        # lista sob condicao
        elif op == 4: 
            op2 = menu('''
        1. Lista de jogos em determinado ano
        2. Lista de jogos de determinado periodo
        3. Lista de jogos abaixo de determinado preco
        4. Lista de jogos acima de determinado preco
        5. Lista de jogos de uma mesma empresa
        6. Lista de jogos de um mesmo genero
            ''')

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
    
        # Usuario
        elif op == 5:
            menu_usuario(lista_jogos)
