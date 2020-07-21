import json

def carregar(arquivo):
    with open(arquivo,'r') as json_file:
        try:
            dados = json.load(json_file)
            return dados
        except:
            print('ERRO')    
            return False
            
def carregar_campo(camp):
    '''
    :return: uma lista de dicionarios do arquivo .json
    '''
    lista = []
    with open('dados.json','r') as json_file:
        dados = carregar('dados.json')
        for dado in dados[camp]:
            lista.append(dado)
    return lista

def carregar_usuarios():
    return carregar_campo("usuarios")
def carregar_jogos():
    return carregar_campo("jogos")

def salvar(camp):
    def slv(lista):
        dados = carregar('dados.json')
        dados[camp] = lista
        
        with open('dados.json','w') as json_file:
            try:
                json.dump(dados, json_file, indent=4)
            except:
                print("ERRO ao salvar")

    return slv
                
salvar_usuarios = salvar("usuario")
salvar_jogos = salvar("jogos")


if __name__ == '__main__':
    print(carregar('dados.json')['usuarios'])