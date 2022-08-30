import time

def limparTela():

    #essa funcao limpa a tela para uma melhor visuaalizacao
    #funcao que chaamam ela ate agora:
    #colocarNavios

    for e in range(5):
        print('')

def mainJogarVsJogador(tabuleiroJogador1,tabuleiroJogador2,dicioPosicaoNaviosJogador1,dicioPosicaoNaviosJogador2,\
                       tabuleiroMostrar1,tabuleiroMostrar2,notaJog1=10000,notaJog2=10000):

    v = 0
    vitoria = False
    while True:
        try:
            if v == 0:
                print('- '*12)
                print('Agora e a vez do Jogador 1 ')
                time.sleep(3)
                limparTela()
                    
                jogador = 'Jogador 2'
                mostrarSeuTabuleiro(tabuleiroJogador1)
                print('\n')
                mostrarTabuleiroInimigo(tabuleiroMostrar1)
                linha,coluna = pedirPosicao()
                linha,coluna = verificarValorPassado(linha,coluna)
                linha,coluna = verificarSeExisteNavioPeça(linha,coluna,tabuleiroMostrar1)
                print('Voto computado!')
                time.sleep(2) 
                tabuleiroJogador2,tabuleiroMostrar1,dicioPosicaoNaviosJogador2,notaJog1 = verificarSeAtingiuAlgumNavio(linha,coluna,tabuleiroJogador2,\
                                            tabuleiroMostrar1,dicioPosicaoNaviosJogador2,jogador,notaJog1)
                condicao = verificarVitoriaJogador1(dicioPosicaoNaviosJogador2)

                if condicao:
                    vitoria = True
                    pontFinal = notaJog1
                    limparTela()
                    print('- '*12)
                    print('Parabens Jogador 1! Voce venceu o jogo!!')
                    print()
                    print(f'A pontuacao do Jogador 1 foi: {notaJog1}')
                    print(f'A pontuacao do Jogador 2 foi: {notaJog2}')
                    print()
                    print('A pontuacao do Jogador 1 sera guardada no rank de pontuacoes')
                    print('- '*12)                
                    break

                for z in range(10):
                    print('\n')
                print('Agora troque de lugar com o Jogador 2 para ele nao ver suas pecas!')
                input('Aperte qualquer tecla para continuar ou Ctrl+C para sair!')

                v = 1

                continue

            if v == 1:
                print('- '*12)
                print('Agora e a vez do Jogador 2.')
                time.sleep(3)                    
                limparTela()

                jogador = 'Jogador 1'                
                mostrarSeuTabuleiro(tabuleiroJogador2)
                print('\n')
                mostrarTabuleiroInimigo(tabuleiroMostrar2)
                linha,coluna = pedirPosicao()
                linha,coluna = verificarValorPassado(linha,coluna)
                linha,coluna = verificarSeExisteNavioPeça(linha,coluna,tabuleiroMostrar2)
                print('Voto computado!')
                time.sleep(2) 
                tabuleiroJogador1,tabuleiroMostrar2,dicioPosicaoNaviosJogador1,notaJog2 = verificarSeAtingiuAlgumNavio(linha,\
                                                coluna,tabuleiroJogador1,tabuleiroMostrar2,dicioPosicaoNaviosJogador1,jogador,notaJog2)
                condicao = verificarVitoriaJogador2(dicioPosicaoNaviosJogador1)
                
                if condicao:
                    vitoria = True
                    pontFinal = notaJog2
                    limparTela()
                    print('- '*12)
                    print('Parabens Jogador 2! Voce venceu o jogo!!')
                    print()
                    print(f'A pontuacao do Jogador 2 foi: {notaJog2}')
                    print(f'A pontuacao do Jogador 1 foi: {notaJog1}')
                    print()
                    print('A pontuacao do Jogador 2 sera guardada no rank de pontuacoes')
                    print('- '*12) 
                    break
                
                for z in range(10):
                    print('\n')
                print('Agora troque de lugar com o Jogador 1 para ele nao ver suas pecas!')
                input('Aperte qualquer tecla para continuar ou Ctrl+C para sair! ')
                
                v = 0
                
                continue

        except KeyboardInterrupt:
            print('Saindo e salvando informacoes...')
            arq = open('Salvar Jogo2.txt','w')
            #Salvando o Tabuleiro Jogadores
            for z in tabuleiroJogador1:
                arq.write(str(z))
                arq.write('\n')
            for z in tabuleiroJogador2:
                arq.write(str(z))
                arq.write('\n')
            #Salvando os Dicios
            arq.write(str(dicioPosicaoNaviosJogador1))
            arq.write('\n')
            arq.write(str(dicioPosicaoNaviosJogador2))
            arq.write('\n')
            #Salvando Tabuleiro Mostrado
            for z in tabuleiroMostrar1:
                arq.write(str(z))
                arq.write('\n')
            for z in tabuleiroMostrar2:
                arq.write(str(z))
                arq.write('\n')
            #Salvando Notas
            arq.write(str(notaJog1)+'\n')
            arq.write(str(notaJog2))
            arq.close()
            break
    
    if vitoria:
        while True:
            try:
                arq = open('pontuacao.txt','r')
                conteudo = arq.readline()
                dicio = eval(conteudo)
                nome = input('Digite seu nome para guardar sua pontuacao: ')
                if pontFinal in dicio:
                    dicio[pontFinal] += [nome]
                else:
                    dicio[pontFinal] = [nome]
                arq.close()
                arq = open('pontuacao.txt','w')
                arq.write(str((dicio)))
                arq.close()
                print('- '*12)
                input('Aperte qualquer tecla para voltar ao menu')
                break
            
            except SyntaxError:
                arq.close()
                dicio = {}
                arq = open('pontuacao.txt','w')
                nome = input('Digite seu nome para guardar sua pontuacao: ')
                if pontFinal in dicio:
                    dicio[pontFinal] += [nome]
                else:
                    dicio[pontFinal] = [nome]
                arq.write(str((dicio)))
                arq.close()
                print('- '*12)
                input('Aperte qualquer tecla para voltar ao menu')
                break
            
            except FileNotFoundError:
                arq = open('pontuacao.txt','w')
                arq.close()
                continue

def pedirPosicao():
    
    print('- - - - - - - - - - -')
    linha = input('Digite a linha que deseja atirar: ')
    coluna = input('Digite a coluna que deseja atirar: ')
               
    return linha,coluna

def verificarValorPassado(linha,coluna):

    #verifico se o valor passado em linha e coluna esta correto

    while True:    
        try:
            colunaAux = int(coluna)
            if colunaAux < 0 or colunaAux > 12:
                raise Exception
            linha = linha.upper()
            listaLetras = ['A','B','C','D','E','F','G','H','I','J']
            if linha not in listaLetras:
                raise Exception
        except:
            print('- - - - - - - - - - -')
            print('Algum valor passado na linha ou na coluna esta Incorreto!')
            print('Lembre-se: a linha precisa ser uma letra entra A e J')
            print('E a coluna um numero entre 1 e 12')
            print('Tente novamente!')
            linha,coluna = pedirPosicao()
            continue
        else:
            break

    return linha,coluna

def mostrarSeuTabuleiro(lista):

    print('         Seu Tabuleiro!')
    print('       - - - - - - - - - - - -')
    linhasTabuleiro = ['a','b','c','d','e','f','g','h','i','j']
    aux2 = 0
    print('  ',end='')
    for i in range(1,13):
        print(i,end='  ')
    print()
    for aux in lista:
        print(linhasTabuleiro[aux2],aux)
        #print()
        aux2=aux2+1

def mostrarTabuleiroInimigo(lista):

    print('         Tabuleiro Inimigo!')
    print('       - - - - - - - - - - - -')
    linhasTabuleiro = ['a','b','c','d','e','f','g','h','i','j']
    aux2 = 0
    print('  ',end='')
    for i in range(1,13):
        print(i,end='  ')
    print()
    for aux in lista:
        print(linhasTabuleiro[aux2],aux)
        #print()
        aux2=aux2+1


def verificarSeExisteNavioPeça(linha,coluna,tabuleiro):

    #Verifico se a posicao ja foi atirada anteriormente

    while True:
        dicio = {'A':0,'B':1,'C':2,'D':3,'E':4,'F':5,'G':6,'H':7,'I':8,'J':9}
        linhaAux = dicio[linha]
        colunaAux = int(coluna) - 1

        if tabuleiro[linhaAux][colunaAux] == 7 or tabuleiro[linhaAux][colunaAux] == 8:
            print('- - - - - - - - - - -')
            print('Aparentemente essa posicao ja foi atirada por voce!')
            print('Tente novamente outra posicao!')
            linha,coluna = pedirPosicao()
            linha,coluna = verificarValorPassado(linha,coluna)
            continue
        else:
            break

    return linha,coluna

def verificarSeAtingiuAlgumNavio(linha,coluna,tabuleiro,tabuleiroMostrar,dicioPosicaoNavios,jogador,nota):

    #Verificar se a posicao atirada foi na agua ou certeira

    dicio = {'A':0,'B':1,'C':2,'D':3,'E':4,'F':5,'G':6,'H':7,'I':8,'J':9}

    linhaAux = linha
    colunaAux = coluna
    linha = dicio[linha]
    coluna = int(coluna) - 1

    if tabuleiro[linha][coluna] == 0:
        print('- '*15)
        print('Errou!')
        print(f'Infelizmente o seu  tiro nao acertou nenhum navio do {jogador}.')
        print('- '*15)
        tabuleiroMostrar[linha][coluna] = 7
        nota = nota - 70
        
    elif tabuleiro[linha][coluna] != 0:
        print('- '*15)
        print('Acertoouuu!!!!')
        print(f'Seu tiro foi na mosca, acertou um navio inimigo do {jogador}!')
        print('- '*15)
        tabuleiroMostrar[linha][coluna] = 8
        st = linhaAux+colunaAux
        dicioPosicaoNavios = organizarDicio1(dicioPosicaoNavios,st)
        nota = nota

    return tabuleiro,tabuleiroMostrar,dicioPosicaoNavios,nota

def organizarDicio1(dicio,string):

    for navio in dicio:
        for listas in dicio[navio]:
            if string in listas:
                listas.remove(string)
                listas.append(0)
                for u in listas:
                    if u != 0:
                        condicao = False
                        break
                    else:
                        condicao = True
                if condicao:        
                    print(f'Parabens! Um dos {navio} foi destruido!')
                    print('- '*15)

    return dicio

def verificarVitoriaJogador1(dicio):

    condicao = True

    for navio in dicio:
        for listas in dicio[navio]:
            for u in listas:
                if u != 0:
                    condicao = False
                    return condicao
    return condicao

def verificarVitoriaJogador2(dicio):

    condicao = True

    for navio in dicio:
        for listas in dicio[navio]:
            for u in listas:
                if u != 0:
                    condicao = False
                    return condicao

    return condicao


if __name__ == '__main__':

    tabuleiroJogador1 = [[0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 5, 3, 3, 3],[0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 2, 0],[0, 0, 0, 0, 0, 1, 3, 0, 5, 0, 2, 0],[4, 4, 4, 4, 0, 0, 3, 0, 2, 2, 0, 0],[0, 0, 0, 0, 1, 0, 3, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 4, 4, 4, 4, 0]]

    dicioPosicaoNaviosJogador1 = {'porta-avioes':[['G9', 'F9', 'E9', 'D9', 'C9']],'cruzador':[['J11', 'J10', 'J9', 'J8'],['H1', 'H2', 'H3', 'H4']],'hidro-aviao':[['G7', 'H7', 'I7'], ['C12', 'C11', 'C10']],'rebocador': [['F11', 'G11'], ['H9', 'H10'],['B9', 'B10']],'submarino':[['I5'],['G6'],['A6']]}

    dicioPosicaoNaviosJogador2 = {'porta-avioes':[['E8', 'E9', 'E10', 'E11', 'E12']],'cruzador':[['D2', 'D3', 'D4', 'D5'],['H2', 'G2', 'F2', 'E2']],'hidro-aviao':[['F7', 'F8', 'F9'], ['B3', 'B4', 'B5']],'rebocador':[['B1','B2'],['G4', 'G5'],['G9', 'H9']],'submarino': [['J12'],['J6'], ['B12']]}

    tabuleiroJogador2 = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[2, 2, 3, 3, 3, 0, 0, 0, 0, 0, 0, 1],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 4, 4, 4, 4, 0, 0, 0, 0, 0, 0, 0],[0, 4, 0, 0, 0, 0, 0, 5, 5, 5, 5, 5],[0, 4, 0, 0, 0, 0, 3, 3, 3, 0, 0, 0],[0, 4, 0, 2, 2, 0, 0, 0, 2, 0, 0, 0],[0, 4, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1]]

    tabuleiroMostrar1 = [[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0]]

    tabuleiroMostrar2 = [[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0]]
    
    mainJogarVsJogador(tabuleiroJogador1,tabuleiroJogador2,dicioPosicaoNaviosJogador1,dicioPosicaoNaviosJogador2,tabuleiroMostrar1,tabuleiroMostrar2)

