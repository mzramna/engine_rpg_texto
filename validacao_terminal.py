class validacao:
    def S_N(self, texto):
        resposta = input(str(texto) + "(s/n)")
        if resposta == "s":
            return True
        elif resposta == "n":
            return False
        else:
            self.limpar()
            print("opção inválida")
            return self.S_N(texto)
        
    def numero(self,texto,inteiro=False):
        resposta = input(str(texto))
        if type(resposta) == type(0) and inteiro == True:
            return resposta
        elif type(resposta) == type(0.0) and inteiro == False:
            return resposta
        else:
            self.limpar()
            print("o valor inserido é inválido")
            texto="o valor inserido deve ser um"
            if inteiro==True:
                texto+=" numero sem virgula"
            else:
                texto+=" numero com virgula"
            return self.numero(texto,inteiro)

    def correto(self, texto):
        print("o valor:")
        print(texto)
        resposta = input("está correto? (s/n)")
        if resposta == "s":
            return True
        elif resposta == "n":
            return False
        else:
            self.limpar()
            print("opção inválida")
            return self.correto(texto)

    def resposta_valida(self, respostas: [], pergunta: str = "", pergunta2: str = "", predefinido: int = -1,
                        confirmar=False,initial=0):
        try:
            if predefinido < -1 or predefinido > len(respostas):
                print(len(respostas))
                raise Exception
            else:
                if predefinido < -1:
                    predef_valid = True
                else:
                    predef_valid = False
            print(pergunta)
            for i in respostas:
                print(str(respostas.index(i)+initial) + " - " + str(i))
            resposta = input(pergunta2)
            if resposta.isdecimal():
                resposta = int(resposta)-initial
                if resposta < 0 or resposta > len(respostas):
                    if predef_valid:
                        print("a opção é invalida")
                        if self.S_N("deseja usar o valor pré definido " + str(respostas[predefinido+initial]) + " ?"):
                            return int(predefinido)
                        else:
                            return self.resposta_valida(respostas, pergunta, pergunta2, predefinido, confirmar,initial)
                    else:
                        self.limpar()
                        print("a opção selecionada não existe")
                        return self.resposta_valida(respostas, pergunta, pergunta2, predefinido, confirmar,initial)
                else:
                    if confirmar:
                        print("a resposta selecionada foi: "+str(resposta))
                        if self.S_N("a resposta selecionada está correta?"):
                            return int(resposta)
                        else:
                            self.limpar()
                            return self.resposta_valida(respostas, pergunta, pergunta2, predefinido, confirmar,initial)
                    else:
                        return int(resposta)
            else:
                print("a opção selecionada deve ser um dos numeros indicados")
                return self.resposta_valida(respostas, pergunta, pergunta2, predefinido, confirmar,initial)
        except Exception as e:
            print("valor " + str(predefinido) + " inválido para predefinição")

    def confirmacao(self, pergunta, tipo=str):
        resposta = input(pergunta)
        try:
            resposta = tipo(resposta)
        except:
            self.limpar()
            print("resposta inválida")
            return self.confirmacao(pergunta, tipo)
        print("a resposta selecionada foi: " + str(resposta))
        if self.S_N("a resposta dada está correta?"):
            return resposta
        else:
            self.limpar()
            return self.confirmacao(pergunta, tipo)

    def limpar(self):
        import os
        os.system('cls' if os.name == 'nt' else 'clear')
