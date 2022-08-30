import time
import JogoVsComputador
import inicioJogoComputador
import inicioJogoJogador
import JogoVsJogador


def menuDaTelaInicial():
    
    print('- - - - - - - - - - - -')
    print('1 - Jogar ')
    print('2 - Ver pontuacao ')
    print('3 - Carregar um jogo ')
    print('4 - Instrucoes ' )
    print('5 - Sair ' )
    print('- - - - - - - - - - - -')

def main():

    #Funcao principal do arquivo
    
    while True:
        menuDaTelaInicial()
        rsp = input('Digite a sua opcao: ')
        if rsp == '1':
            menuJogar()
        elif rsp == '2':
            mostrarPontuacao()
        elif rsp == '3':
            carregarJogo()
        elif rsp == '4':
            instrucoes()
        elif rsp == '5':
            print('- '*12)
            print('Saindo do programa, obrigado por jogar!')
            print('Programa fechado.')
            break
        else:
            print('Opcao invalida')
            print('Tente novamente!')
            continue
    
def menuJogar():

    #Menu apos o usuario clicar em 'jogar'
    
    while True:
        print('- - - - - - - - - - - -')
        print('Qual o modo de jogo voce deseja?')
        print('1 - Contra o computador')
        print('2 - Com duas pessoas')
        print('3 - Voltar')
        print('- - - - - - - - - - - -')
        opcaoJogar = input('Digite a sua opcao: ')
        #Ccodigo para Jogar contra o computador
        if opcaoJogar == '1':
            print('- - - - - - - -  - - - -')
            print('Certo, a opcao jogar contra o computador foi escolhida.')
            print('Aguarde alguns instantes, estamos preparando o seu tabuleiro!')
            print('- - - - - - - -  - - - -')
            time.sleep(6)
            print('Certo! Esta tudo preparado! Vamos comecar??!')
            time.sleep(3)

            tabuleiroMostrar = [[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0]]

            tabuleiroJogador,dicioPosicaoNaviosJogador,tabuleiroComputador,dicioPosicaoNaviosComputador = inicioJogoComputador.mainContraComputador()

            print('Seu tabuleiro foi finalizado!')
            print('- - - - - - - - - - - -')
            for i in range(5):
                print('\n')
            print('Aguarde alguns instantes para que o tabuleiro da maquina seja computado...')
            time.sleep(5)
            print('Muito bem! O tabuleiro do computador também já foi gerado!')
            print('- - - - - - - - - - - -')
            input('Aperte qualquer tecla para iniciarmos o jogo!')

            JogoVsComputador.mainJogarVsComputador(tabuleiroJogador,tabuleiroComputador,dicioPosicaoNaviosComputador,\
                                                   dicioPosicaoNaviosJogador,tabuleiroMostrar)
            break

        #Ccodigo jogar com duas pessoas
        elif opcaoJogar == '2':
            print('- - - - - - - -  - - - -')
            print('Certo, a opcao jogar com dois jogadores foi escolhida.')
            print('Aguarde alguns instantes, estamos preparando o tabuleiro dos dois jogadores!')
            print('- - - - - - - -  - - - -')
            time.sleep(6)
            print('Certo! Esta tudo preparado! Vamos comecar??!')
            time.sleep(3)
            
            tabuleiroMostrar1 = [[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0]]
            tabuleiroMostrar2 = [[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0]]

            tabuleiroJogador1,dicioNavios1,tabuleiroJogador2,dicioNavios2 = inicioJogoJogador.mainJogador()

            for i in range(5):
                print('\n')
            print('Muito bem! O tabuleiro dos dois jogadores foram feitos!')     
            print('- - - - - - - - - - - -')
            input('Aperte qualquer tecla para iniciarmos o jogo!')

            JogoVsJogador.mainJogarVsJogador(tabuleiroJogador1,tabuleiroJogador2,\
                                             dicioNavios1,dicioNavios2,tabuleiroMostrar1,tabuleiroMostrar2)
            break
        elif opcaoJogar == '3':
            break            
        else:
            print('- - - - - - - - - - - -')
            print('Opcao invalida')
            print('Tente novamente!')        

def carregarJogo():
    c1 = False
    c2 = False  
    #Codigo para carregar um jogo ja salvo
    while True:
        try:
            print('- - - - - - - - - - - -')
            print('Qual o modo de jogo voce carregar?')
            print('1 - Contra o computador')
            print('2 - Com duas pessoas')
            print('3 - Voltar')
            print('- - - - - - - - - - - -')
            op = input('Digite a sua opcao: ')

            if op == '1':              
                arq = open('Salvar Jogo1.txt','r')
                tabuleiroJogador = []
                tabuleiroComputador = []
                tabuleiroMostrar = []
                conteudo = arq.readline()
                aux = 0
                while aux < 33:
                    #Transcrevendo o Tabuleiro Jogador
                    if aux <= 9:
                        tabuleiroJogador.append(eval(conteudo))
                        conteudo = arq.readline()
                        aux += 1
                    #Transcrevendo o Dicio Jogador
                    elif aux == 10:
                        dicioNaviosJogador = eval(conteudo)
                        conteudo = arq.readline()
                        aux += 1
                    #Transcrevendo a Nota
                    elif aux == 11:
                        nota = int(conteudo)
                        conteudo = arq.readline()
                        aux += 1
                    #Transcrevendo o Tabuleiro Computador
                    elif aux > 11 and aux <= 21:
                        tabuleiroComputador.append(eval(conteudo))
                        conteudo = arq.readline()
                        aux += 1
                    #Transcrevendo o Dicio
                    elif aux == 22:
                        dicioNaviosComputador = eval(conteudo)
                        conteudo = arq.readline()
                        aux += 1
                    #Transcrevendo o Tabuleiro Mostrar
                    elif aux > 22 and aux <= 32:
                        tabuleiroMostrar.append(eval(conteudo))
                        conteudo = arq.readline()
                        aux += 1
                print('Carregando conteudo...')
                print('- - - - - - - - - - - -')
                time.sleep(4)
                print('Carregado com sucesso!')
                for z in range(4):
                    print('\n')
                arq.close()
                c1 = True
                break
                

            if op == '2':
                aux = 0
                tabuleiroJog1 = []
                tabuleiroJog2 = []
                tabuleiroMostrar1 = []
                tabuleiroMostrar2 = []
                arq = open('Salvar Jogo2.txt','r')
                conteudo = arq.readline()

                while aux < 44:
                    #Transcrevendo o Tabuleiro Jogador1
                    if aux <= 9:
                        tabuleiroJog1.append(eval(conteudo))
                        conteudo = arq.readline()
                        aux += 1
                    #Transcrevendo o Tabuleiro Jogador2
                    elif aux > 9 and aux <=19:
                        tabuleiroJog2.append(eval(conteudo))
                        conteudo = arq.readline()
                        aux += 1
                    #Transcrevendo o Dicio Jogador1
                    elif aux == 20:
                        dicioNaviosJogador1 = eval(conteudo)
                        conteudo = arq.readline()
                        aux += 1
                    #Transcrevendo o Dicio Jogador2    
                    elif aux == 21:
                        dicioNaviosJogador2 = eval(conteudo)
                        conteudo = arq.readline()
                        aux += 1
                    #Transcrevendo o Tabuleiro Mostrar1
                    elif aux > 21 and aux <= 31:
                        tabuleiroMostrar1.append(eval(conteudo))
                        conteudo = arq.readline()
                        aux += 1
                    #Transcrevendo o Tabuleiro Mostrar2
                    elif aux > 31 and aux<=41:
                        tabuleiroMostrar2.append(eval(conteudo))
                        conteudo = arq.readline()
                        aux += 1
                    #Transcrevendo Notas
                    elif aux == 42:
                        notaJog1 = int(conteudo)
                        conteudo = arq.readline()
                        aux += 1
                    elif aux == 43:
                        notaJog2 = int(conteudo)
                        aux += 1
                print('Carregando conteudo...')
                print('- - - - - - - - - - - -')
                time.sleep(4)
                print('Carregado com sucesso!')
                for z in range(4):
                    print('\n')  
                arq.close()
                c2 = True
                break

            if op == '3':
                break
                                                                                                                                                                                                                                                              
        except FileNotFoundError or SyntaxError:
            for i in range(3):
                print('\n')
            print('Arquivo vazio ou inexistente')
            for i in range(3):
                print('\n')
            break
    if c1:
        JogoVsComputador.mainJogarVsComputador(tabuleiroJogador,tabuleiroComputador,dicioNaviosComputador,\
                                                       dicioNaviosJogador,tabuleiroMostrar,nota)
    elif c2:
        JogoVsJogador.mainJogarVsJogador(tabuleiroJog1,tabuleiroJog2,\
                                    dicioNaviosJogador1,dicioNaviosJogador2,tabuleiroMostrar1,tabuleiroMostrar2,notaJog1,notaJog2)

def mostrarPontuacao():

    #Funcao para mostrar as pontuacoes
    try:
        for i in range(3):
            print('\n')
        arq = open('pontuacao.txt','r')
        aux = 1
        conteudo = arq.readline()
        dicio = eval(conteudo)
        pont = list(dicio.keys())
        pont.sort()
        pont.reverse()
        print('Ranking:')
        arq.close()
        for ponto in pont:
            print(f'{aux} - {ponto} ; Jogador: {dicio[ponto]}')
            aux += 1
        for i in range(3):
            print('\n')
        input('Pressione qualquer tecla para voltar ao menu: ')
    except FileNotFoundError or SyntaxError:
        print('Arquivo vazio ou inexistente.')
        for i in range(3):
            print('\n')

def instrucoes():

    for i in range(10):
        print('\n')
    print('- '*10)
    print('Os numeros de 1 a 5 sao referentes')
    print('as pecas dos navios')
    print('1 - submarino')
    print('2 - rebocador')
    print('3 - hidro-aviao')
    print('4 - cruzador')
    print('5 - porta-avioes')
    print('- '*12)
    print('O numero 7 nos tabuleiros significam que o')
    print('tiro foi mal-sucedido')
    print('- '*12)
    print('O numero 8 nos tabuleiros significam que')
    print('algum tiro foi acertado com sucesso')
    print('- '*12)
    for i in range(7):
        print('\n')
    input('Aperte qualquer tecla para voltar ao menu: ')

main()
