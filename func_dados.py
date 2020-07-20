import json

def carregar(nome):
    '''
    :return: uma lista de dicionarios do arquivo .json
    '''
    url = '{}.json'.format(nome)
    lista = []
    with open(url,'r') as json_file:
        try:
            dados = json.load(json_file)
            for dado in dados["jogos"]:
                lista.append(dado)
        except:
            print("ERRO - dados_{} nao encontrados".format(nome))
    return lista

def carregar_usuarios():
    return carregar("usuarios")
def carregar_jogos():
    return carregar("jogos")

def salvar(elem):
    '''
        :param lista: uma lista de dicionarios
        :return: True se der certo, False se der errado
    '''
    def _slv(lista):
        dic = {elem: lista}
        with open('jogos.json', 'w') as json_file:
            try:
                json.dump(dic, json_file, indent=4)
            except:
                print('ERRO')
                return False
            return True
    return _slv

salvar_usuarios = salvar("usuario")
salvar_jogos = salvar("jogos")
