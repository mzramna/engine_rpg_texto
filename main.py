import math

from validacao_terminal import validacao
import myJSON
'''
    arquitetura json:
    comodo:{"identificador":0,"nome do comodo":"","texto de entrada":"","possiveis comodos":[0,0],"acoes":[0,0],"redirecao por acao":[(0,1),(0,1)]}
        "redirecao por acao"=caso a ação indicada seja realizada,toda vez que o jogador entrar nesse mapa será enviado para a localização indicada,
        podendo ser um vetor,cada tupla indica uma ação,e deve estar na ordem de prioridade: 
            ex: a primeira condição foi ativada,sendo assim verifica a segunda,e assim por diante até que alguma não seja ativada,
            a anterior a essa não ativada será a selecionada 
    item:{"identificador":0,"nome do item":"","descricao do item":"","usavel em":[0,0],"durabilidade":1,"crafting":[0,0]}
    acao:{"identificador":0,"descrição da ação":"","itens necessários":[],"dicas":[0,0],"resultado":0}
    resultados:{"identificador":0,"texto explicativo":"","itens ganhos":[0,0],"itens perdidos":[0,0],"local destino":0/NULL}
    dica:{"identificados":0,"item necessário":[0,0],"local necessário":[0,0],"texto da dica":""}
'''

class engine_rpg_texto:
    def __init__(self,comodo_inicial:int,comodos,itens,acoes,resultados,dicas, *args, **kwargs):
        super(self).__init__(*args, **kwargs)
        self.json=myJSON()
        self.validacao=validacao()
        self.comodos=self.json.readfile(comodos)
        self.itens = self.json.readfile(itens)
        self.acoes = self.json.readfile(acoes)
        self.resultados = self.json.readfile(resultados)
        self.dicas = self.json.readfile(dicas)
        self.posicao_jogador=comodo_inicial
        self.mochila=[]
        self.acoes_realizadas=[]
        self.opcoes_base=["inventario","criacao","menu","mapa"]
    def start(self):
        self.entrar_comodo(self.posicao_jogador)

    def entrar_comodo(self,comodo:int):
        _comodo=self.json.search(self.comodos,"identificador",comodo)
        opcao=self.validacao.resposta_valida(self.opcoes_base+_comodo["acoes"],pergunta=_comodo["texto de entrada"],confirmar=True)
        if opcao == 0:#inventario
            self.mostrar_inventario()
        elif opcao == 1:#criacao
            self.mostrar_crafting()
        elif opcao == 2:#menu
            self.mostrar_menu()
        elif opcao == 3:#mapa
            self.mostrar_mapa()
        else :
            _acao=_comodo["acoes"][opcao-len(self.opcoes_base)]
            if self.pre_requisito_acao(_acao):
                if self.validacao.S_N("deseja realizar essa ação?"):
                    self.realizar_acao(_acao["identificador"])
            else:
                self.mostrar_dica(_acao["identificador"])
                self.entrar_comodo(comodo)

    def realizar_acao(self,acao:int):
        _acao=self.json.search(self.acoes,"identificador",acao)
        opcao = self.validacao.resposta_valida(self.opcoes_base + _acao["acoes"],
                                               pergunta=_acao["texto de entrada"], confirmar=True)
        self.acoes_realizadas.append(opcao)

    def pre_requisito_acao(self,acao:int):
        _acao = self.json.search(self.acoes, "identificador", acao)
        for item in _acao["itens necessarios"]:
            if item not in self.mochila:
                return False
        return True

    def mostrar_dica(self,acao:int):
        _acao = self.json.search(self.acoes, "identificador", acao)
        print(_acao["dicas"][math.random(0,len(_acao["dicas"]))])

    def mostrar_menu(self):
        pass
    def mostrar_inventario(self):
        pass
    def mostrar_crafting(self):
        pass
    def mostrar_mapa(self):
        pass