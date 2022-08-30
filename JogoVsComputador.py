import random
import time

def limparTela():

    #essa funcao limpa a tela para uma melhor visuaalizacao

    for e in range(5):
        print('')

def mainJogarVsComputador(tabuleiroJogador,tabuleiroComputador,dicioPosicaoNaviosComputador,dicioPosicaoNaviosJogador,tabuleiroMostrar,nota=10000):

    #Funcao que organiza todo o jogo
    
    v = 0
    vitoria = False
    
    while True:
        
        try:
            #Jogada do Jogador
            if v == 0:

                mostrarTabuleiroInimigo(tabuleiroMostrar)   
                linha,coluna = pedirPosicao()            
                linha,coluna = verificarValorPassado(linha,coluna)  
                linha,coluna = verificarSeExisteNavioPeça(linha,coluna,tabuleiroMostrar)
                print('Voto computado!')
                time.sleep(1)                                                                             
                tabuleiroMostrar,dicioPosicaoNaviosComputador,nota = verificarSeAtingiuAlgumNavioJogador(linha,coluna,tabuleiroComputador,tabuleiroMostrar,dicioPosicaoNaviosComputador,nota) 
                condicao = verificarVitoriaJogador(dicioPosicaoNaviosComputador)
                if condicao:
                    limparTela()
                    vitoria = True
                    print('- '*12)
                    print('Parabens! Voce venceu o jogo!')
                    print(f'Essa foi a sua pontuacao:')
                    print()
                    print(f'{nota}')
                    print()
                    print('Vamos guardar ela e colocar no rank de pontuacoes')
                    print('- '*12)
                    break

                input('Aperte qualquer tecla para continuar ou Ctrl+C para sair!')
                
                v = 1
                continue
            
            #Jogada do computador
            if v == 1:
                limparTela()
                
                tabuleiroJogador = sortearPosicaoTabuleiro(tabuleiroJogador,dicioPosicaoNaviosJogador)
                
                limparTela()
                mostrarTabuleiroJogador(tabuleiroJogador)
                condicao = verificarVitoriaComputador(dicioPosicaoNaviosJogador)
                if condicao:
                    limparTela()                  
                    print('- '*12)
                    print('Poxa! Voce perdeu o jogo!')
                    print(f'Essa foi a sua pontuacao:')
                    print()
                    print(f'{nota}')
                    print()
                    print('- '*12)
                    break

                input('Aperte qualquer tecla para continuar ou Ctrl+C para sair!')
                
                limparTela()
                v = 0
                continue

        #Salvando os tabuleiros e informacoes
        except KeyboardInterrupt:
            print('Saindo e salvando informacoes...')
            #Salvando o tabuleiro do Jogador, dicio nota
            arq = open('Salvar Jogo1.txt','w')
            for z in tabuleiroJogador:
                arq.write(str(z))
                arq.write('\n')
            arq.write(str(dicioPosicaoNaviosJogador))
            arq.write('\n')
            arq.write(str(nota)+'\n')
            #Salvando o tabuleiro inimigo e o mostrado
            for z in tabuleiroComputador:
                arq.write(str(z))
                arq.write('\n')
            arq.write(str(dicioPosicaoNaviosComputador))
            arq.write('\n')
            for z in tabuleiroMostrar:
                arq.write(str(z))
                arq.write('\n')
            arq.close()
            break
        
    #Escrevendo no dicio para salvar as pontuacoes
    if vitoria:
        while True:
            try:
                arq = open('pontuacao.txt','r')
                conteudo = arq.readline()
                dicio = eval(conteudo)
                nome = input('Digite seu nome para guardar sua pontuacao: ')
                if nota in dicio:
                    dicio[nota] += [nome]
                else:
                    dicio[nota] = [nome]
                arq.close()
                arq = open('pontuacao.txt','w')
                arq.write(str((dicio)))
                arq.close()
                print('- '*12)
                input('Aperte qualquer tecla para voltar ao menu: ')
                break
            
            except SyntaxError:
                dicio = {}
                arq = open('pontuacao.txt','w')
                nome = input('Digite seu nome para guardar sua pontuacao: ')
                if nota in dicio:
                    dicio[nota] += [nome]
                else:
                    dicio[nota] = [nome]
                arq.write(str((dicio)))
                arq.close()
                print('- '*12)
                input('Aperte qualquer tecla para voltar ao menu: ')
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

def mostrarTabuleiroInimigo(lista):

    print('         Tabuleiro inimigo!')
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
    
def mostrarTabuleiroJogador(lista):
    
    print('         Seu tabuleiro!')
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
    print('- - - - - - - - - - - -')

def verificarSeAtingiuAlgumNavioJogador(linha,coluna,tabuleiroComputador,tabuleiroMostrar,dicioPosicaoNaviosComputador,nota):

    #Verificar se a posicao atirada foi na agua ou certeira

    dicio = {'A':0,'B':1,'C':2,'D':3,'E':4,'F':5,'G':6,'H':7,'I':8,'J':9}

    linhaAux = linha
    colunaAux = coluna
    linha = dicio[linha]
    coluna = int(coluna) - 1

    if tabuleiroComputador[linha][coluna] == 0:
        print('- '*15)
        print('Errou!')
        print('Infelizmente o seu  tiro nao acertou nenhum navio.')
        print('- '*15)
        tabuleiroMostrar[linha][coluna] = 7
        nota = nota - 70
        
    elif tabuleiroComputador[linha][coluna] != 0:
        print('- '*15)
        print('Acertoouuu!!!!')
        print('Seu tiro foi na mosca, acertou um navio inimigo!')
        print('- '*15)
        tabuleiroMostrar[linha][coluna] = 8
        st = linhaAux+colunaAux
        dicioPosicaoNaviosComputador = organizarDicio1(dicioPosicaoNaviosComputador,st)
        nota = nota 

    return tabuleiroMostrar,dicioPosicaoNaviosComputador,nota

                
def sortearPosicaoTabuleiro(tabuleiro,dicioPosicaoNaviosJogador):

    #Sorteio a jogada do computador e verificar se atingiu ou nao

    colunasDicio = {'1':0,'2':1,'3':2,'4':3,'5':4,'6':5,'7':6,'8':7,'9':8,'10':9,'11':10,'12':11}
    linhasDicio = {'A':0,'B':1,'C':2,'D':3,'E':4,'F':5,'G':6,'H':7,'I':8,'J':9}

    while True:
        linha = random.choice(list(linhasDicio.keys()))
        coluna = random.choice(list(colunasDicio.keys()))
        linhaAux = linhasDicio[linha]
        colunaAux = colunasDicio[coluna]
        
        if tabuleiro[linhaAux][colunaAux] == 7 or tabuleiro[linhaAux][colunaAux] == 8:
            #Essa peca ja foi atirada
            continue
        elif tabuleiro[linhaAux][colunaAux] == 0:
            #tiro na Agua
            print('Estamos calculando a jogada do computador...')
            time.sleep(1)
            print('Voto do adversário computado!')
            print('O tiro foi na água!')
            st = linha+coluna
            print(f'A jogada foi {st}')
            tabuleiro[linhaAux][colunaAux] = 7
            
            break
        else:
            #Tiro Certo
            print('Estamos calculando a jogada do computador...')
            time.sleep(1)
            print('Voto do adversário computado!')
            print('Droga, ele acertou uma peca sua!')
            st = linha+coluna
            print(f'A jogada foi {st}')
            tabuleiro[linhaAux][colunaAux] = 8
            dicioPosicaoNaviosJogador = organizarDicio2(dicioPosicaoNaviosJogador,st) 
            break

    return tabuleiro


def organizarDicio1(dicio,string):

    #Retirar a posicao que foi acertada do dicionario pelo JOGADOR

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

def organizarDicio2(dicio,string):

    #Retirar a posicao que foi acertada do dicionario pelo COMPUTADOR

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
                    print('- '*15)
                    print(f'Droga! Um dos seus {navio} foi destruido!')
                    print('- '*15)

    return dicio

def verificarVitoriaJogador(dicio):

    condicao = True

    for navio in dicio:
        for listas in dicio[navio]:
            for u in listas:
                if u != 0:
                    condicao = False
                    return condicao
    return condicao

def verificarVitoriaComputador(dicio):

    condicao = True

    for navio in dicio:
        for listas in dicio[navio]:
            for u in listas:
                if u != 0:
                    condicao = False
                    return condicao

    return condicao
                    
                        
                
                

    
    
# Alguns testes

#dicioPosicaoNaviosJogador = {'porta-avioes':[[0, 0, 0, 0, 0]],'cruzador':[[0, 0, 0, 0],[0, 0, 0, 0]],'hidro-aviao':[[0, 0, 0], [0, 0, 0]],'rebocador':[[0,0],[0, 0],[0, 0]],'submarino': [['J12'],[0], [0]]}
#dicioPosicaoNaviosJogador = {'porta-avioes':[['E8', 'E9', 'E10', 'E11', 'E12']],'cruzador':[['D2', 'D3', 'D4', 'D5'],['H2', 'G2', 'F2', 'E2']],'hidro-aviao':[['F7', 'F8', 'F9'], ['B3', 'B4', 'B5']],'rebocador':[['B1','B2'],['G4', 'G5'],['G9', 'H9']],'submarino': [['J12'],['J6'], ['B12']]}

    
if __name__ == '__main__':

    tabuleiroComputador = [[0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 5, 3, 3, 3],[0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 2, 0],[0, 0, 0, 0, 0, 1, 3, 0, 5, 0, 2, 0],[4, 4, 4, 4, 0, 0, 3, 0, 2, 2, 0, 0],[0, 0, 0, 0, 1, 0, 3, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 4, 4, 4, 4, 0]]

    dicioPosicaoNaviosComputador = {'porta-avioes':[['G9', 'F9', 'E9', 'D9', 'C9']],'cruzador':[['J11', 'J10', 'J9', 'J8'],['H1', 'H2', 'H3', 'H4']],'hidro-aviao':[['G7', 'H7', 'I7'], ['C12', 'C11', 'C10']],'rebocador': [['F11', 'G11'], ['H9', 'H10'],['B9', 'B10']],'submarino':[['I5'],['G6'],['A6']]}

    dicioPosicaoNaviosJogador = {'porta-avioes':[['E8', 'E9', 'E10', 'E11', 'E12']],'cruzador':[['D2', 'D3', 'D4', 'D5'],['H2', 'G2', 'F2', 'E2']],'hidro-aviao':[['F7', 'F8', 'F9'], ['B3', 'B4', 'B5']],'rebocador':[['B1','B2'],['G4', 'G5'],['G9', 'H9']],'submarino': [['J12'],['J6'], ['B12']]}
    
    tabuleiroJogador = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[2, 2, 3, 3, 3, 0, 0, 0, 0, 0, 0, 1],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 4, 4, 4, 4, 0, 0, 0, 0, 0, 0, 0],[0, 4, 0, 0, 0, 0, 0, 5, 5, 5, 5, 5],[0, 4, 0, 0, 0, 0, 3, 3, 3, 0, 0, 0],[0, 4, 0, 2, 2, 0, 0, 0, 2, 0, 0, 0],[0, 4, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1]]

    tabuleiroMostrar = [[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0]]

    mainJogarVsComputador(tabuleiroJogador,tabuleiroComputador,dicioPosicaoNaviosComputador,dicioPosicaoNaviosJogador,tabuleiroMostrar)
