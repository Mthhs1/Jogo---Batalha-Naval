import random

def mainContraComputador():

    tabuleiroJogador = [[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],\
                       [0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],\
                       [0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0]]

    tabuleiroComputador = [[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],\
                    [0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],\
                    [0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0]]
    
    
    tabuleiroJogador,dicioPosicaoNaviosJogador = colocarNavios(tabuleiroJogador)
    tabuleiroComputador,dicioPosicaoNaviosComputador = sortearTabuleiroComputador(tabuleiroComputador)

    return tabuleiroJogador,dicioPosicaoNaviosJogador,tabuleiroComputador,dicioPosicaoNaviosComputador
    

def verificarLinhaColuna(linha,coluna):

    #Essa funcao verifica se os valores passados na
    #coluna e na linha na funcao 'funcaoRepetirPecas'
    #esta correto
    
    verificar = False
    linha.upper()
    setLinha = ['A','B','C','D','E','F','G','H','I','J']
    setColuna = ['1','2','3','4','5','6','7','8','9','10','11','12']
    if linha not in setLinha:
        verificar = True
    if coluna not in setColuna:
        verificar = True
    
    return verificar    
    

def limparTela():
    
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
        

def transformarString(linha,coluna):

    #funcao para agrupar a linha e a coluna numa
    #string so
  
    string = linha+coluna   

    return string

def verificarContemJogador(linha,coluna,tabuleiro):

    #verificar se a posicao que passou ja contem uma peca

    booleano = True
    dicioLinhas = {'A':0,'B':1,'C':2,'D':3,'E':4,'F':5,'G':6,'H':7,'I':8,'J':9}

    while booleano:

        linhaAux = dicioLinhas[linha]
        colunaAux = int(coluna)-1
        
        if tabuleiro[linhaAux][colunaAux] == 0:
            booleano = False
            continue
        else:
            print('- - - - - - - - - - - -')
            print('Erro!')
            print('Essa posicao ja contem uma peca!')
            print('Insira outra!')
            print('- - - - - - - - - - - -')
            while True:
                linha = (input('Em qual linha voce deseja colocar? ')).upper()
                coluna = input('Em qual coluna voce deseja colocar? ')
                verificar = verificarLinhaColuna(linha,coluna)
                if verificar:
                    print('- - - - - - - - - - - -')
                    print('Erro!')
                    print('Valor passado errado!')
                    print('Insira outro!')
                    print('- - - - - - - - - - - -')
                else:
                    break            
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
            verificar = verificarLinhaColuna(linha,coluna)
            while verificar:
                print('- - - - - - - - - - - -')
                print('Valor passado errado!')
                print('Lembre-se que a linha e de -A a J-')
                print('E as colunas de -0 a 12-')
                print('- - - - - - - - - - - -')
                linha = (input('Em qual linha voce deseja colocar? ')).upper()
                coluna = input('Em qual coluna voce deseja colocar? ')
                verificar = verificarLinhaColuna(linha,coluna)
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
            verificar = verificarLinhaColuna(linha,coluna)
            while verificar:
                print('- - - - - - - - - - - -')
                print('Valor passado errado!')
                print('Lembre-se que a linha e de -A a J-')
                print('E as colunas de -0 a 12-')
                print('- - - - - - - - - - - -')
                linha = (input('Em qual linha voce deseja colocar? ')).upper()
                coluna = input('Em qual coluna voce deseja colocar? ')
                verificar = verificarLinhaColuna(linha,coluna)
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
            verificar = verificarLinhaColuna(linha,coluna)
            while verificar:
                print('- - - - - - - - - - - -')
                print('Valor passado errado!')
                print('Lembre-se que a linha e de -A a J-')
                print('E as colunas de -0 a 12-')
                print('- - - - - - - - - - - -')
                linha = (input('Em qual linha voce deseja colocar? ')).upper()
                coluna = input('Em qual coluna voce deseja colocar? ')
                verificar = verificarLinhaColuna(linha,coluna)
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

    #COLOCANDO AS PECAS DO REBOCADIR = SAO 2 PECAS ENTAO REPETE 2 VEZES
    elif dicio[navio] == 2:
        for i in range(2):
            print(f'Coloque a {pecas[aux]} peca do seu {navio} ')
            linha = (input('Em qual linha voce deseja colocar? ')).upper()
            coluna = input('Em qual coluna voce deseja colocar? ')
            verificar = verificarLinhaColuna(linha,coluna)
            while verificar:
                print('- - - - - - - - - - - -')
                print('Valor passado errado!')
                print('Lembre-se que a linha e de -A a J-')
                print('E as colunas de -0 a 12-')
                print('- - - - - - - - - - - -')
                linha = (input('Em qual linha voce deseja colocar? ')).upper()
                coluna = input('Em qual coluna voce deseja colocar? ')
                verificar = verificarLinhaColuna(linha,coluna)
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
        verificar = verificarLinhaColuna(linha,coluna)
        while verificar:
            print('- - - - - - - - - - - -')
            print('Valor passado errado!')
            print('Lembre-se que a linha e de -A a J-')
            print('E as colunas de -0 a 12-')
            print('- - - - - - - - - - - -')
            linha = (input('Em qual linha voce deseja colocar? ')).upper()
            coluna = input('Em qual coluna voce deseja colocar? ')
            verificar = verificarLinhaColuna(linha,coluna)
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

def colocarNavios(tabuleiroJogador):

    #funcao que organiza todo o tabuleiro do jogador
    
    limparTela()
    c = ['primeiro','segundo','terceiro']
    dicioPosicaoNaviosJogador = {'porta-avioes':[],'cruzador':[],'hidro-aviao':[],'rebocador':[],'submarino':[]}
    dicioNumPecas = {'porta-avioes':5,'cruzador':4,'hidro-aviao':3,'rebocador':2,'submarino':1}
    
    print('Muito bem! Agora vamos posicionar as')
    print('pecas no seu tabuleiro!')
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
            #tem que repetir tres vezes o submrino
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
    
def sortearTabuleiroComputador(tabuleiroComputador,c=False):

    #funcao que organiza todo o tabuleiro do computador

    aux = 0
    dicioPosicaoNaviosComputador = {'porta-avioes':[],'cruzador':[],'hidro-aviao':[],'rebocador':[],'submarino':[]}
    v = {5:'porta-avioes',4:'cruzador',3:'hidro-aviao',2:'rebocador',1:'submarino'}
    
    
    while True:
        dicioPecas = [5,4,4,3,3,2,2,2,1,1,1,0]
        linha,coluna,escolherPosicao = sortearPosicao(tabuleiroComputador)
        
        if dicioPecas[aux] == 0:            
            break

        # SUBMARINO / 1 PECA / 3 NAVIOS
        if dicioPecas[aux] == 1:
            tabuleiroComputador[linha][coluna] = 1
            listaSub = []
            listaParaAdicionar = transformarLinhaColunaComputador(linha,coluna,listaSub)
            dicioPosicaoNaviosComputador[v[dicioPecas[aux]]] += [listaParaAdicionar]
            aux=aux+1
            
         

        # RECOBADOR / 2 PECAS / 3 NAVIOS
        if dicioPecas[aux] == 2:
            if escolherPosicao == 'horizontal':
                condicao,tabuleiroComputador,listaParaAdicionar = colocarNaHorizontal(linha,coluna,tabuleiroComputador,dicioPecas[aux])
                if condicao:
                    continue
                dicioPosicaoNaviosComputador[v[dicioPecas[aux]]] += [listaParaAdicionar]
                aux=aux+1
        
            if escolherPosicao == 'vertical':
                condicao,tabuleiroComputador,listaParaAdicionar = colocarNaVertical(linha,coluna,tabuleiroComputador,dicioPecas[aux])
                if condicao:
                    continue
                dicioPosicaoNaviosComputador[v[dicioPecas[aux]]] += [listaParaAdicionar]
                aux=aux+1          
                    

        # HIDRO AVIAO / 3 PECAS / 2 NAVIOS
        if dicioPecas[aux] == 3:
            if escolherPosicao == 'horizontal':
                condicao,tabuleiroComputador,listaParaAdicionar = colocarNaHorizontal(linha,coluna,tabuleiroComputador,dicioPecas[aux])
                if condicao:
                    continue
                dicioPosicaoNaviosComputador[v[dicioPecas[aux]]] += [listaParaAdicionar]
                aux=aux+1
                    
                
            if escolherPosicao == 'vertical':
                condicao,tabuleiroComputador,listaParaAdicionar = colocarNaVertical(linha,coluna,tabuleiroComputador,dicioPecas[aux])
                if condicao:
                    continue
                dicioPosicaoNaviosComputador[v[dicioPecas[aux]]] += [listaParaAdicionar]
                aux=aux+1
                  

        # CRUZADOR / 4 PECAS / 2 NAVIOS     
        if dicioPecas[aux] == 4:
            if escolherPosicao == 'horizontal':
                condicao,tabuleiroComputador,listaParaAdicionar = colocarNaHorizontal(linha,coluna,tabuleiroComputador,dicioPecas[aux])
                if condicao:
                    continue
                dicioPosicaoNaviosComputador[v[dicioPecas[aux]]] += [listaParaAdicionar]
                aux=aux+1
                
                
            if escolherPosicao == 'vertical':
                condicao,tabuleiroComputador,listaParaAdicionar = colocarNaVertical(linha,coluna,tabuleiroComputador,dicioPecas[aux])
                if condicao:
                    continue
                dicioPosicaoNaviosComputador[v[dicioPecas[aux]]] += [listaParaAdicionar]
                aux=aux+1               
            

        # PORTA-AVIOES / 5 PECAS / 1 NAVIO
        if dicioPecas[aux] == 5:
            if escolherPosicao == 'horizontal':
                condicao,tabuleiroComputador,listaParaAdicionar = colocarNaHorizontal(linha,coluna,tabuleiroComputador,dicioPecas[aux])
                if condicao:
                    continue
                dicioPosicaoNaviosComputador[v[dicioPecas[aux]]] += [listaParaAdicionar]
                aux=aux+1
            

            if escolherPosicao == 'vertical':
                condicao,tabuleiroComputador,listaParaAdicionar = colocarNaVertical(linha,coluna,tabuleiroComputador,dicioPecas[aux])
                if condicao:    
                    continue
                dicioPosicaoNaviosComputador[v[dicioPecas[aux]]] += [listaParaAdicionar]
                aux=aux+1

    if c:
        mostrarTabuleiro(tabuleiroComputador)

    return tabuleiroComputador,dicioPosicaoNaviosComputador
            


def colocarNaHorizontal(linha,coluna,tabuleiroComputador,numPecas):

    #braco da funcao principal que organiza o tabuleiro do jogador

    condicao = False
    listaParaAdicionar = []

    #COLOCAR DA ESQUERDA PARA A DIREITA
    if (coluna+(numPecas-1)) > 11:

        #COLOCAR DA DIREITA PARA A ESQUERDA
        if (coluna-(numPecas-1)) < 0:  
            condicao = True
            return condicao,tabuleiroComputador,listaParaAdicionar

        #VERIFICAR SE NA LINHA DA DIREITA PARA ESQUERDA POSSUI POSICOES JA OCUPADAS
        for i in range(coluna,coluna-numPecas,-1):
            if tabuleiroComputador[linha][i] != 0:
                condicao = True
                return condicao,tabuleiroComputador,listaParaAdicionar

        #COLOCANDO AS PECAS DA DIREITA PARA A ESQUERDA
        for i in range(coluna,coluna-numPecas,-1): 
            tabuleiroComputador[linha][i] = numPecas
            listaParaAdicionar = transformarLinhaColunaComputador(coluna=i,linha=linha,lista=listaParaAdicionar)
        return condicao,tabuleiroComputador,listaParaAdicionar


    #VERIFICAR SE NA LINHA DA ESQUERDA PARA DIREITA POSSUI POSICOES JA OCUPADAS
    for i in range(coluna,coluna+numPecas): 
        if tabuleiroComputador[linha][i] != 0:
            condicao = True
            return condicao,tabuleiroComputador,listaParaAdicionar

    #COLOCANDO AS PECAS DA ESQUERDA PARA A DIREITA
    for i in range(coluna,coluna+numPecas):
        tabuleiroComputador[linha][i] = numPecas
        listaParaAdicionar = transformarLinhaColunaComputador(coluna=i,linha=linha,lista=listaParaAdicionar)
    return condicao,tabuleiroComputador,listaParaAdicionar


def colocarNaVertical(linha,coluna,tabuleiroComputador,numPecas):

    #segundo braco da funcao principal que organiza o tabuleiro do jogador

    condicao = False
    listaParaAdicionar = []
    #DE CIMA PARA BAIXO
    if (linha+(numPecas-1)) > 9: 

        #DE BAIXO PARA CIMA
        if (linha-(numPecas-1)) < 0:  
            condicao = True
            return condicao,tabuleiroComputador,listaParaAdicionar
        
        #VERIFICAR SE DE BAIXO PARA CIMA TEM PECAS
        for i in range(linha,linha-numPecas,-1): 
            if tabuleiroComputador[i][coluna] != 0:
                condicao = True
                return condicao,tabuleiroComputador,listaParaAdicionar

        #COLOCANDO PECAS DE BAIXO PARA CIMA
        for i in range(linha,linha-numPecas,-1): 
            tabuleiroComputador[i][coluna] = numPecas
            listaParaAdicionar = transformarLinhaColunaComputador(linha=i,coluna=coluna,lista=listaParaAdicionar)
        return condicao,tabuleiroComputador,listaParaAdicionar

    #VERIFICAR SE DE CIMA PARA BAIXO TEM PECAS
    for i in range(linha,linha+numPecas): 
        if tabuleiroComputador[i][coluna]!= 0:
            condicao = True
            return condicao,tabuleiroComputador,listaParaAdicionar

    #COLOCANDO COLOCANDO AS PECAS DE CIMA PARA BAIXO
    for i in range(linha,linha+numPecas): 
        tabuleiroComputador[i][coluna] = numPecas
        listaParaAdicionar = transformarLinhaColunaComputador(linha=i,coluna=coluna,lista=listaParaAdicionar)
    return condicao,tabuleiroComputador,listaParaAdicionar

def transformarLinhaColunaComputador(linha,coluna,lista):

    #Transformar em uma so string a linha e a coluna
    #pois as string passadas sao sao numeros

    Linhas = {0:'A',1:'B',2:'C',3:'D',4:'E',5:'F',6:'G',7:'H',8:'I',9:'J'}
    coluna = coluna+1
    coluna = str(coluna)
    s = Linhas[linha] + coluna
    lista.append(s)

    return lista

def sortearPosicao(tabuleiro):

    #terceiro braco da funcao principal que organiza o tabuleiro do jogador

    while True:
        linha = random.randint(0,9)
        coluna = random.randint(0,11)

        if tabuleiro[linha][coluna] != 0:
            continue

        escolher = ['horizontal','vertical']
        escolherPosicao = random.choice(escolher)

        return linha,coluna,escolherPosicao

if __name__ == '__main__':

    lista1 = [[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],\
         [0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0]]

    lista2 = [[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],\
         [0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0]]

    
    colocarNavios(lista1)
    
    tab,dicio = sortearTabuleiroComputador(lista2,c=True)
