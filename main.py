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

def lista_filtrada(lista):
    return lambda camp: lambda condicao: [elem[camp] for elem in lista if condicao(elem)] 

filtrada = lista_filtrada(lista_jogos)
jogos_filt_nome = filtrada('nome')
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
    txt = ''
    for elem in sorted(lst, key=lambda lst: lst['ID']):
        for camp in elem:
            txt += str(camp) + ': '+ str(elem[camp]) + '\n'
        txt += '\n'
    return txt

def ano():
    numero = 0
    Operador = False
    while (Operador == False):
        numero = input("Digite um ano válido: ")
        if (e_int(numero) == True):
            Operador = True
    return int(numero)

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
    return float(numero)

def preco():
    numero = 0
    Operador = False
    while (Operador == False):
        numero = input("Digite um preco válido: ")
        if (e_float(numero) == True):
            Operador = True
    return float(numero)


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
                        if user == lista_usuarios[i]['nome']:
                            print("Nome de Usuario já existente")
                            a = 0
               
                favorito = criafav(lista_jogos, [])                     

                usuario = {
                    "nome": user,
                    "jogos": favorito
                }
                lista_usuarios.append(usuario)
                func_dados.salvar_usuarios(lista_usuarios)

            else:
                existente = 0
                for i in range(0,len(lista_usuarios)):
                    if user == lista_usuarios[i]['nome']:
                        favorito = lista_usuarios[i]['jogos']
                        existente = 1
                
                if existente == 1:

                    favorito = criafav(lista_jogos, favorito)        
                    usuario = {
                        "nome": user,
                        "jogos": favorito
                    }
                    lista_usuarios[i] = usuario
                    func_dados.salvar_usuarios(lista_usuarios)
                else:
                    print("Usuario Ainda não cadastrado")


def pesquisaID(lista_jogos, x):         
    for i in range(0,len(lista_jogos)):                
        if int(lista_jogos[i]['ID']) == x:
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
                favorito.append(lista_jogos[i]['ID'])
                print("Jogo ", lista_jogos[i]['nome'], "Adicionado a sua lista")

        elif op2 == 2:
            jogo = input("Digite o nome do jogo que deseja remover: ")
            i = pesquisaNome(lista_jogos, jogo)
            try:
                favorito.remove(lista_jogos[i]['ID'])
                print("Jogo Removido")
            except:
                print("Jogo não esta na sua Lista")

        elif op2 == 3:
            print(imprime(lista_jogos))  

        elif op2 == 4:
            for i in range(0,len(favorito)):
                print(lista_jogos[pesquisaID(lista_jogos, favorito[i])]['nome'])

    return favorito

# Funcao Alysson
def busca_nome(lista):
    lista_aux = []
    aux = input('nome: ')
    for i in range(0, len(lista)):
        if aux in lista[i]['nome']:
            lista_aux.append(lista[i])
    return lista_aux if len(lista_aux) > 0 else 'nao encontrado' 

# Funcoes Leo
def altera(lista_jogos):
    x = int(input("Digite o id do jogo que deseja alterar: "))

    if x == -1:
        print("Jogo não encontrado")

    else:
        i = pesquisaID(lista_jogos, x)
        x = 1
        print(lista_jogos[i])
        while x != 8:

            x = int(input(
                "O que deseja Alterar? \n1 - Nome\n2 - Empresa\n3 - Lancamento\n4 - genero\n5 - Avaliacao\n6 - Preco Medio\n7 - Plantaforma\n8 - Sair\n"))
            if x == 1:
                lista_jogos[i]['nome'] = input("Digite o nome do jogo para alterar: ")
            elif x == 2:
                lista_jogos[i]['empresa'] = input("Digite o nome da empresa para alterar: ")
            elif x == 3:
                lista_jogos[i]['lancamento'] = ano()
            elif x == 4:
                lista_jogos[i]['genero'] = input("Digite o genero para alterar: ")
            elif x == 5:
                lista_jogos[i]['avaliacao'] = review()
            elif x == 6:
                lista_jogos[i]['preco_medio'] = preco()
            elif x == 7:
                lista_jogos[i]['plataforma'] = lista_empresa()

        func_dados.salvar_jogos(lista_jogos)

id_jogos = len(lista_jogos) + 2
id_usuarios = len(lista_usuarios) + 2

# MAIN
if __name__ == '__main__':
    while True:
        op = menu('''
    1. Inserir jogo
    2. Remover
    3. Imprimir
    4. Lista sob condicao
    5. Usuario
    6. Alterar informacao jogo
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
            op2 = menu('''
        1. Todos os jogos
        2. Jogos especificos por nome
            ''')

            if op2 == 1:
                print(imprime(lista_jogos))
            elif op2 == 2:
                print(imprime(busca_nome(lista_jogos)))

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
                print(jogos_filt_nome(lambda elem: elem['lancamento']==int(ano)))
            
            #Lista de jogos de determinado periodo
            elif op2 == 2:
                ano1 = input('ano inicio: ')
                if ano1 == '':
                    ano1 = datetime.date.today().year
                    ano2 = datetime.date.today().year
                else:    
                    ano2 = input('ano fim: ')
                    if ano2 == '':
                        ano2 = datetime.date.today().year
                print(jogos_filt_nome(lambda elem: elem['lancamento'] >= int(ano1) and elem["lancamento"] <= int(ano2)))

            #Lista de jogos abaixo de determinado preco
            elif op2 == 3:
                valor = float(input("valor: "))
                print(jogos_filt_nome(lambda elem: elem["preco_medio"] <= valor))

            #Lista de jogos acima de determinado preco
            elif op2 == 4:
                valor = float(input("valor: "))
                print(jogos_filt_nome(lambda elem: elem["preco_medio"] >= valor))

            #Lista de jogos de uma mesma empresa
            elif op2 == 5:
                opc,lst = sub_opc(empresas_filtradas)  
                print(jogos_filt_nome(lambda elem: elem['empresa'] == lst[opc]))

            #Lista de jogos de um mesmo genero
            elif op2 == 6:
                opc,lst = sub_opc(generos_filtrados)
                print(jogos_filt_nome(lambda elem: elem['genero'] == lst[opc]))
    
        # Usuario
        elif op == 5:
            menu_usuario(lista_jogos)
        
        elif op == 6:
            altera(lista_jogos)
