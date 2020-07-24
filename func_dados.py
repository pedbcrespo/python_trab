import json

def carregar(arquivo):
    with open(arquivo,'r') as json_file:
        try:
            dados = json.load(json_file)
            return dados
        except:
            print('ERRO ao carregar')    
            return {"jogos":[],"usuarios":[]}
            
def carregar_campo(camp):
    return carregar('dados.json')[camp]

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
                
salvar_usuarios = salvar("usuarios")
salvar_jogos = salvar("jogos")


if __name__ == '__main__':
    print(carregar('dados.json')['jogos'])
    # usuarios = ['Pedro', "Leonardo", "Lucas"]
    # salvar_usuarios(usuarios)
    # print(carregar('dados.json')['usuarios'])
