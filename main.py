from ast import IsNot
from operator import contains, is_not
from random import randint

# lista composta por: Turma, Professor, Quantidade de Alunos e Tipo de local (Labin ou Sala de aula)
eventos = [
    ['A1', 1, 27, 1],
    ['A2', 2, 33, 1],
    ['A3', 4, 25, 1],
    ['A4', 4, 25, 0],
    ['A5', 5, 42, 0],
    ['B1', 1, 31, 1],
    ['B2', 2, 26, 1],
    ['B3', 3, 20, 1],
    ['B4', 5, 45, 0],
    ['B5', 6, 42, 0],
    ['C1', 6, 20, 1],
    ['C2', 5, 19, 1],
    ['C3', 1, 43, 1],
    ['C4', 6, 45, 1],
    ['D1', 7, 30, 1],
    ['D2', 2, 20, 1],
    ['D3', 7, 30, 1],
    ['D4', 3, 20, 1],
    ['E1', 7, 27, 0],
    ['E2', 2, 22, 1],
    ['E3', 7, 26, 1],
    ['E4', 4, 25, 1],
    ['E5', 7, 25, 1],
    ['F1', 4, 22, 1],
    ['F2', 6, 30, 1],
    ['F3', 1, 21, 1],
    ['F4', 3, 25, 0],
    ['G1', 3, 25, 1],
    ['G2', 4, 44, 1],
    ['G3', 5, 44, 0],
    ['H1', 1, 25, 1],
    ['H2', 3, 44, 1],
    ['H3', 5, 44, 0]
]
locais = [
    ['L1', 50],
    ['L2', 0],
    ['L3', 20],
    ['L4', 30],
    ['L5', 40],
    ['L6', 40],
    ['S1', 50],
    ['S2', 50],
    ['S3', 40]
]

dias_semana = ['segunda', 'terça', 'quarta', 'quinta', 'sexta']

tamanho_populacao = 33*7*50*4*9


def gerador_cromossomo():
    '''
        gerador de cromossomo, estrutura é a seguinte:
        |Disciplina(0-32)|Professor(0-6)|Alunos(0-50)|Tipo(0-1)|Dia(0-4)|Local(0-8)|Aptidao = 0

        essa função retorna essa estrutura como uma lista.
    '''
    return [randint(0, 32), randint(0, 6), randint(0, 50), randint(0, 1), randint(0, 4), randint(0, 8), 0]


def gerar_populacao_inicial():
    '''
        população inicial será composta por 100 cromossomos
    '''
    lista_populacao_inicial = []
    for i in range(tamanho_populacao):
        lista_populacao_inicial.append(gerador_cromossomo())
    return lista_populacao_inicial


def calcular_aptidao(cromossomo):
    cromossomo_aux = cromossomo.copy()
    cromossomo_aux[0] = eventos[cromossomo[0]][0]
    if cromossomo_aux[0:4] in eventos:
        return True
    else:
        return False

def dizimacao(populacao):
    horarios_indisponiveis = []
    turmas_indisponiveis = []
    populacao_dizimada = []
    for cromossomo in populacao:
        horario = cromossomo[4:6]
        turma = cromossomo[0]
        if turma not in turmas_indisponiveis:
            turmas_indisponiveis.append(turma)
            #verifica se tem o horario e se não é no labin 2
            if horario not in horarios_indisponiveis and cromossomo[5] != 1:
                horarios_indisponiveis.append(horario)
                populacao_dizimada.append(cromossomo)
    

    return populacao_dizimada


def crossover(populacao):
    tamanho_populacao = len(populacao)
    populacao_cruzada= []

    if tamanho_populacao % 2 == 0:
        for i in range(1,tamanho_populacao,2):
            primeiro_filho = []
            segundo_filho = []
            primeira_parte_pai_1 = populacao[i-1][:4]
            segunda_parte_pai_1 = populacao[i-1][-3:]
            primeira_parte_pai_2 = populacao[i][:4]
            segunda_parte_pai_2 = populacao[i][-3:]
            
            primeiro_filho.extend(primeira_parte_pai_1)
            primeiro_filho.extend(segunda_parte_pai_2)
            segundo_filho.extend(primeira_parte_pai_2)
            segundo_filho.extend(segunda_parte_pai_1)
            
            populacao_cruzada.append(primeiro_filho)
            populacao_cruzada.append(segundo_filho)
    else:
        for i in range(1, (tamanho_populacao),2):
            primeiro_filho = []
            segundo_filho = []
            primeira_parte_pai_1 = populacao[i-1][:4]
            segunda_parte_pai_1 = populacao[i-1][-3:]
            primeira_parte_pai_2 = populacao[i][:4]
            segunda_parte_pai_2 = populacao[i][-3:]
            
            primeiro_filho.extend(primeira_parte_pai_1)
            primeiro_filho.extend(segunda_parte_pai_2)
            segundo_filho.extend(primeira_parte_pai_2)
            segundo_filho.extend(segunda_parte_pai_1)
            
            populacao_cruzada.append(primeiro_filho)
            populacao_cruzada.append(segundo_filho)
        
        populacao_cruzada.append(populacao[-1])        

    return populacao_cruzada

def multacao_gene(populacao):
    for cromossomo in populacao:
        aleatoriedade = randint(0,100)
        if aleatoriedade < 10:
            cromossomo[4] = randint(0,4)
        elif aleatoriedade >=10 and aleatoriedade < 20:
            cromossomo[5] = randint(0,8)
        else:
            cromossomo[0] = randint(0,32)
    return populacao

def encontrar_solucao():
    populacao_inicial = gerar_populacao_inicial()
    populacao_compativel = []
    t = 0
    nao_solucionou_problema = True

    print(f'Geração: {t} \nPopulação: {len(populacao_inicial)}')


    for cromossomo in populacao_inicial:
        if calcular_aptidao(cromossomo):
            cromossomo[-1] = cromossomo[-1] +1
            populacao_compativel.append(cromossomo)
    

    while nao_solucionou_problema:
        t += 1
        proxima_geracao = dizimacao(populacao_compativel)
        
        if len(proxima_geracao) < 35:
            print(f'Geração: {t} \nPopulação: {len(proxima_geracao)}') 
            proxima_geracao_aux = crossover(populacao_inicial)
            proxima_geracao_aux = multacao_gene(populacao_inicial)
            populacao_compativel = proxima_geracao_aux
        else:
            print(f'Geração: {t} \Solução: {proxima_geracao}') 
            nao_solucionou_problema = False
            populacao_compativel.extend(proxima_geracao)
        

encontrar_solucao()
