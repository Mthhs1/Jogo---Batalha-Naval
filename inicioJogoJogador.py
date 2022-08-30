import random
import time

def mainJogador():

    tabuleiroJogador1 = [[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],\
                       [0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],\
                       [0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0]]


    tabuleiroJogador2 = [[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],\
                       [0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],\
                       [0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0]]

    jogador = 'Jogador 1'
    tabuleiroJogador1,dicioNavios1 = colocarNavios(tabuleiroJogador1,jogador)

    for i in range(5):
        print('\n')
    print('- '*12)
    print('Certo! O tabuleiro do Jogador 1 foi finalizado')
    print('Agora, vamos preparar o tabuleiro do Jogador 2')
    print('- '*12)
    input('Pressione qualquer tecla para continuar: ')
          
    jogador = 'Jogador 2'
    tabuleiroJogador2,dicioNavios2 =colocarNavios(tabuleiroJogador2,jogador)

    return tabuleiroJogador1,dicioNavios1,tabuleiroJogador2,dicioNavios2

def limparTela():

    #essa funcao limpa a tela para uma melhor visuaalizacao
    #funcao que chaamam ela ate agora:
    #colocarNavios
    
    for e in range(30):
        print('')

def mostrarTabuleiro(lista):

    #funcao para mostrar o tabuleiro do jogador durante
    #a selecao de posicoes para os seus navios no
    #comeco do jogo

    print('- - - - - - - - - - - -')
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

def verificarValorPassado(linha,coluna):

    #verificar se os valoros psssados de
    #linha e coluna estao corretos 

    verificar = False
    colunaAux = coluna
       
    try:
        colunaAux = int(coluna)
        if colunaAux < 0 or colunaAux > 12:
            raise Exception
        linha = linha.upper()
        listaLetras = ['A','B','C','D','E','F','G','H','I','J']
        if linha not in listaLetras:
            raise Exception
    except:
        verificar = True
        return verificar
    else:
        return verificar
 
def verificarContemJogador(linha,coluna,tabuleiro):

    #verifico se na posicao escolhida ja contem uma peca

    dicioLinhas = {'A':0,'B':1,'C':2,'D':3,'E':4,'F':5,'G':6,'H':7,'I':8,'J':9}

    while True:

        try:
            linhaAux = dicioLinhas[linha]
            colunaAux = int(coluna)-1
        
            if tabuleiro[linhaAux][colunaAux] == 0:
                break
            else:
                print('- - - - - - - - - - - -')
                print('Erro!')
                print('Essa posicao ja contem uma peca!')
                print('Insira outra!')
                print('- - - - - - - - - - - -')
                linha = (input('Em qual linha voce deseja colocar? ')).upper()
                coluna = input('Em qual coluna voce deseja colocar? ')
                continue
        except KeyError or IndexError or ValueError:
            print('- - - - - - - - - - - -')
            print('Erro!')
            print('Algum valor passado na coluna ou linha esta incorreto')
            print('Tente novamente!')
            print('- - - - - - - - - - - -')
            linha = (input('Em qual linha voce deseja colocar? ')).upper()
            coluna = input('Em qual coluna voce deseja colocar? ')
            continue
            
    return linha,coluna

def colocarNoTab(linha,coluna,conjunto,num):

    #funcao para oolocar no tabuleiro a peca do navio passado
    #pelo jogador
    #e chamado pela funcao
    #funcaoRepetirPecas


    dicioLinhas = {'A':0,'B':1,'C':2,'D':3,'E':4,'F':5,'G':6,'H':7,'I':8,'J':9}
    linha = dicioLinhas[linha]
    coluna = int(coluna)-1
    
    conjunto[linha][coluna] = num

    return conjunto

def transformarString(linha,coluna):

    #funcao para agrupar a linha e a coluna numa
    #string so
  
    string = linha+coluna   

    return string

def funcaoRepetirPecas(navio,dicio,listaTabuleiro):

    #FUNCAO QUE REPETE AS PECAS DOS NAVIOS

    aux = 0
    listaParaAdicionar = []
    pecas = ['primeira','segunda','terceira','quarta','quinta']

    #COLOCANDO AS PECAS DO PORTA AVIOS = SAO 5 PECAS ENTAO REPETE 5 VEZES
    if dicio[navio] == 5:
        for i in range(5):
            print(f'Coloque a {pecas[aux]} peca do seu {navio} ')
            linha = (input('Em qual linha voce deseja colocar? ')).upper()
            coluna = input('Em qual coluna voce deseja colocar? ')
            verificar = verificarValorPassado(linha,coluna)
            while verificar:
                print('- - - - - - - - - - - -')
                print('Valor passado errado!')
                print('Lembre-se que a linha e de -A a J-')
                print('E as colunas de -0 a 12-')
                print('- - - - - - - - - - - -')
                linha = (input('Em qual linha voce deseja colocar? ')).upper()
                coluna = input('Em qual coluna voce deseja colocar? ')
                verificar = verificarValorPassado(linha,coluna)
                continue

            linha,coluna = verificarContemJogador(linha,coluna,listaTabuleiro)
            linhaEcoluna = transformarString(linha,coluna)
            listaParaAdicionar.append(linhaEcoluna)
            listaTabuleiro = colocarNoTab(linha,coluna,listaTabuleiro,dicio[navio])
            mostrarTabuleiro(listaTabuleiro)
            aux += 1
            print('Peca adicionada com sucesso!')
            print('- - - - - - - - - - - -')
        
        return listaTabuleiro,listaParaAdicionar
            
    #COLOCANDO AS PECAS DO CRUZADOR = SAO 4 PECAS ENTAO REPETE 4 VEZES
    elif dicio[navio] == 4:
        for i in range(4):
            print(f'Coloque a {pecas[aux]} peca do seu {navio} ')
            linha = (input('Em qual linha voce deseja colocar? ')).upper()
            coluna = input('Em qual coluna voce deseja colocar? ')
            verificar = verificarValorPassado(linha,coluna)
            while verificar:
                print('- - - - - - - - - - - -')
                print('Valor passado errado!')
                print('Lembre-se que a linha e de -A a J-')
                print('E as colunas de -0 a 12-')
                print('- - - - - - - - - - - -')
                linha = (input('Em qual linha voce deseja colocar? ')).upper()
                coluna = input('Em qual coluna voce deseja colocar? ')
                verificar = verificarValorPassado(linha,coluna)
                continue

            linha,coluna = verificarContemJogador(linha,coluna,listaTabuleiro)
            linhaEcoluna = transformarString(linha,coluna)
            listaParaAdicionar.append(linhaEcoluna)
            listaTabuleiro = colocarNoTab(linha,coluna,listaTabuleiro,dicio[navio])
            mostrarTabuleiro(listaTabuleiro)
            aux += 1
            print('Peca adicionada com sucesso!')
            print('- - - - - - - - - - - -')
        
        return listaTabuleiro,listaParaAdicionar

    #COLOCANDO AS PECAS DO HIDRO AVIAO = SAO 3 PECAS ENTAO REPETE 3 VEZES
    elif dicio[navio] == 3:
        for i in range(3):
            print(f'Coloque a {pecas[aux]} peca do seu {navio} ')
            linha = (input('Em qual linha voce deseja colocar? ')).upper()
            coluna = input('Em qual coluna voce deseja colocar? ')
            verificar = verificarValorPassado(linha,coluna)
            while verificar:
                print('- - - - - - - - - - - -')
                print('Valor passado errado!')
                print('Lembre-se que a linha e de -A a J-')
                print('E as colunas de -0 a 12-')
                print('- - - - - - - - - - - -')
                linha = (input('Em qual linha voce deseja colocar? ')).upper()
                coluna = input('Em qual coluna voce deseja colocar? ')
                verificar = verificarValorPassado(linha,coluna)
                continue

            linha,coluna = verificarContemJogador(linha,coluna,listaTabuleiro)
            linhaEcoluna = transformarString(linha,coluna)
            listaParaAdicionar.append(linhaEcoluna)
            listaTabuleiro = colocarNoTab(linha,coluna,listaTabuleiro,dicio[navio])
            mostrarTabuleiro(listaTabuleiro)
            aux += 1
            print('Peca adicionada com sucesso!')
            print('- - - - - - - - - - - -')
        
        return listaTabuleiro,listaParaAdicionar

    #COLOCANDO AS PECAS DO REBICADIR = SAO 2 PECAS ENTAO REPETE 2 VEZES
    elif dicio[navio] == 2:
        for i in range(2):
            print(f'Coloque a {pecas[aux]} peca do seu {navio} ')
            linha = (input('Em qual linha voce deseja colocar? ')).upper()
            coluna = input('Em qual coluna voce deseja colocar? ')
            verificar = verificarValorPassado(linha,coluna)
            while verificar:
                print('- - - - - - - - - - - -')
                print('Valor passado errado!')
                print('Lembre-se que a linha e de -A a J-')
                print('E as colunas de -0 a 12-')
                print('- - - - - - - - - - - -')
                linha = (input('Em qual linha voce deseja colocar? ')).upper()
                coluna = input('Em qual coluna voce deseja colocar? ')
                verificar = verificarValorPassado(linha,coluna)
                continue

            linha,coluna = verificarContemJogador(linha,coluna,listaTabuleiro)
            linhaEcoluna = transformarString(linha,coluna)
            listaParaAdicionar.append(linhaEcoluna)
            listaTabuleiro = colocarNoTab(linha,coluna,listaTabuleiro,dicio[navio])
            mostrarTabuleiro(listaTabuleiro)
            aux += 1
            print('Peca adicionada com sucesso!')
            print('- - - - - - - - - - - -')
        
        return listaTabuleiro,listaParaAdicionar

    #COLOCANDO AS PECAS DO SUBMARINO = SAO 1 PECA1 ENTAO REPETE 1 VEZ

    else:
        print(f'Coloque a {pecas[aux]} peca do seu {navio} ')
        linha = (input('Em qual linha voce deseja colocar? ')).upper()
        coluna = input('Em qual coluna voce deseja colocar? ')
        verificar = verificarValorPassado(linha,coluna)
        while verificar:
            print('- - - - - - - - - - - -')
            print('Valor passado errado!')
            print('Lembre-se que a linha e de -A a J-')
            print('E as colunas de -0 a 12-')
            print('- - - - - - - - - - - -')
            linha = (input('Em qual linha voce deseja colocar? ')).upper()
            coluna = input('Em qual coluna voce deseja colocar? ')
            verificar = verificarValorPassado(linha,coluna)
            continue

        linha,coluna = verificarContemJogador(linha,coluna,listaTabuleiro)
        linhaEcoluna = transformarString(linha,coluna)
        listaParaAdicionar.append(linhaEcoluna)
        listaTabuleiro = colocarNoTab(linha,coluna,listaTabuleiro,dicio[navio])
        mostrarTabuleiro(listaTabuleiro)
        aux += 1
        print('Peca adicionada com sucesso!')
        print('- - - - - - - - - - - -')
        
    return listaTabuleiro,listaParaAdicionar   

def colocarNavios(tabuleiroJogador,jogador):

    #funcao que organiza todo o tabuleiro do jogador

    limparTela()
    c = ['primeiro','segundo','terceiro']
    dicioPosicaoNaviosJogador = {'porta-avioes':[],'cruzador':[],'hidro-aviao':[],'rebocador':[],'submarino':[]}
    dicioNumPecas = {'porta-avioes':5,'cruzador':4,'hidro-aviao':3,'rebocador':2,'submarino':1}
    print(f'Muito bem! Agora vamos posicionar as')
    print(f'pecas no tabuleiro do {jogador}!')
    print('- - - - - - - - - - - -')
    print('Essas sao os seus navios disponiveis: ')
    print('1 porta-avioes')
    print('2 cruzadores')
    print('2 hidro-aviao')
    print('3 rebocadores')
    print('3 submarinos')
    print('- - - - - - - - - - - -')
    input('Aperte qualquer tecla para continuar! ')
    print('- - - - - - - - - - - -')
    limparTela()


    for navio in dicioNumPecas:
        aux = 0
        if navio == 'porta-avioes':
            #tem que repetir uma vez o porta-avioes
            for i in range(1,2):
                print(f'Posicione o seu {navio}!')
                print(f'Lembre-se: ele tem {dicioNumPecas[navio]} pecas, coloque elas sequencialmente!')
                mostrarTabuleiro(tabuleiroJogador)
                tabuleiroJogador,listaPecas = funcaoRepetirPecas(navio,dicioNumPecas,tabuleiroJogador)
                print(f'Muito bem! Seu {navio} foi adicionado!')
                print('Agora, vamos para os outros navios!')
                print('- - - - - - - - - - - -')
                u = input('Aperte qualquer tecla para continuar! ')
                limparTela()
                dicioPosicaoNaviosJogador[navio] += [listaPecas]


        elif navio == 'cruzador':
            #tem que repetir duas vezes o cruzador
            for i in range(1,3):
                print(f'Posicione o seu {c[aux]} {navio}!')
                print(f'Lembre-se: ele tem {dicioNumPecas[navio]} pecas, coloque elas sequencialmente!')
                mostrarTabuleiro(tabuleiroJogador)
                tabuleiroJogador,listaPecas = funcaoRepetirPecas(navio,dicioNumPecas,tabuleiroJogador)
                print(f'Muito bem! Seu {navio} foi adicionado!')
                print('Agora, vamos para os outros navios!')
                print('- - - - - - - - - - - -')
                u = input('Aperte qualquer tecla para continuar! ')
                aux += 1
                dicioPosicaoNaviosJogador[navio] += [listaPecas]
                limparTela()
                
    
        elif navio == 'hidro-aviao':
            #tem que repetir duas vezes o hidro-aviao
            for i in range(1,3):
                print(f'Posicione o seu {c[aux]} {navio}!')
                print(f'Lembre-se: ele tem {dicioNumPecas[navio]} pecas, coloque elas sequencialmente!')
                mostrarTabuleiro(tabuleiroJogador)
                tabuleiroJogador,listaPecas = funcaoRepetirPecas(navio,dicioNumPecas,tabuleiroJogador)
                print(f'Muito bem! Seu {navio} foi adicionado!')
                print('Agora, vamos para os outros navios!')
                print('- - - - - - - - - - - -')
                u = input('Aperte qualquer tecla para continuar! ')
                aux += 1
                dicioPosicaoNaviosJogador[navio] += [listaPecas]
                limparTela()


        elif navio == 'rebocador':
            #tem que repetir tres vezes o rebocador
            for i in range(1,4):
                print(f'Posicione o seu {c[aux]} {navio}!')
                print(f'Lembre-se: ele tem {dicioNumPecas[navio]} pecas, coloque elas sequencialmente!')
                mostrarTabuleiro(tabuleiroJogador)
                tabuleiroJogador,listaPecas = funcaoRepetirPecas(navio,dicioNumPecas,tabuleiroJogador)
                print(f'Muito bem! Seu {navio} foi adicionado!')
                print('Agora, vamos para os outros navios!')
                print('- - - - - - - - - - - -')
                u = input('Aperte qualquer tecla para continuar! ')
                aux += 1
                dicioPosicaoNaviosJogador[navio] += [listaPecas]
                limparTela()


        elif navio == 'submarino':
            #tem que repetir tres vezes o submarino
            for i in range(1,4):
                print(f'Posicione o seu {c[aux]} {navio}!')
                print(f'Lembre-se: ele tem {dicioNumPecas[navio]} pecas, coloque elas sequencialmente!')
                mostrarTabuleiro(tabuleiroJogador)
                tabuleiroJogador,listaPecas = funcaoRepetirPecas(navio,dicioNumPecas,tabuleiroJogador)
                print(f'Muito bem! Seu {navio} foi adicionado!')
                print('Agora, vamos para os outros navios!')
                print('- - - - - - - -  - - - -')
                u = input('Aperte qualquer tecla para continuar! ')
                aux += 1
                dicioPosicaoNaviosJogador[navio] += [listaPecas]
                limparTela()

    return tabuleiroJogador,dicioPosicaoNaviosJogador
    
if __name__ == '__main__':
    mainJogador()
