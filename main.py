from random import randint
from collections import Counter


# lista composta por: Turma, Professor, Quantidade de Alunos e Tipo de local (Labin ou Sala de aula)
eventos = [
    ["A1", 1, 27, 1],
    ["A2", 2, 33, 1],
    ["A3", 4, 25, 1],
    ["A4", 4, 25, 0],
    ["A5", 5, 42, 0],
    ["B1", 1, 31, 1],
    ["B2", 2, 26, 1],
    ["B3", 3, 20, 1],
    ["B4", 5, 45, 0],
    ["B5", 6, 42, 0],
    ["C1", 6, 20, 1],
    ["C2", 5, 19, 1],
    ["C3", 1, 43, 1],
    ["C4", 6, 45, 1],
    ["D1", 7, 30, 1],
    ["D2", 2, 20, 1],
    ["D3", 7, 30, 1],
    ["D4", 3, 20, 1],
    ["E1", 7, 27, 0],
    ["E2", 2, 22, 1],
    ["E3", 7, 26, 1],
    ["E4", 4, 25, 1],
    ["E5", 7, 25, 1],
    ["F1", 4, 22, 1],
    ["F2", 6, 30, 1],
    ["F3", 1, 21, 1],
    ["F4", 3, 25, 0],
    ["G1", 3, 25, 1],
    ["G2", 4, 44, 1],
    ["G3", 5, 44, 0],
    ["H1", 1, 25, 1],
    ["H2", 3, 44, 1],
    ["H3", 5, 44, 0],
]
horarios = ["segunda", "terça", "quarta", "quinta", "sexta"]

locais = [
    ["L1", 50],
    ["L2", 0],
    ["L3", 20],
    ["L4", 30],
    ["L5", 40],
    ["L6", 40],
    ["S1", 50],
    ["S2", 50],
    ["S3", 40],
]


def gerar_gene():
    """Gera a estrutura usada em cada gene.
    A estrutura é a seguinte:
        |Disciplina(0-32)|Professor(0-6)|Alunos(0-50)|Tipo(0-1)|Dia(0-4)|Local(0-8)|Aptidao = 0|
    """
    return [randint(0, 32), randint(0, 6), randint(0, 50), randint(0, 1)]


def gerar_cromossomo():
    """
    Estrutura do cromossomo é um vetor (HxL) Horários, Locais.
    Cada gene do cromossomo é corresponde a um evento.
    """
    cromossomo = []
    horarios = 5
    locais = 9

    for i in range(horarios*locais):
        cromossomo.append(gerar_gene())

    return cromossomo


#print('Estrutura cromossomo',gerar_cromossomo(),'\n---------------')


def gerar_populacao():
    """
    Gera a população inicial.
    O tamanho dela é dado pelo produto entre Horários, Locais e Eventos.
    """
    #tamanho_populacao = 5 * 9 * 32
    tamanho_populacao = 2
    populacao_inicial = []
    for i in range(0, tamanho_populacao):
        populacao_inicial.append(gerar_cromossomo())

    return populacao_inicial


def calcular_aptidao(cromossomo):
    restricoes_duras = 100
    restricoes_leves = 15
    lista_horarios_professor = []
    penalidade_colisao_professor = 0
    penalidade_colisao_turma = 0

    lista_horarios_turma = []

    for i in range(len(cromossomo)):
        professor = eventos[cromossomo[i][0]][1]
        turma = eventos[cromossomo[i][0]][0]
        if i <= 8:
            lista_horarios_professor.append(str(professor) + 'seg')
            lista_horarios_turma.append(str(turma) + 'seg')
        elif i <= 17:
            lista_horarios_professor.append(str(professor) + ' ter')
            lista_horarios_turma.append(str(turma) + ' ter')
        elif i <= 26:
            lista_horarios_professor.append(str(professor) + ' qua')
            lista_horarios_turma.append(str(turma) + ' qua')
        elif i <= 35:
            lista_horarios_professor.append(str(professor) + 'qui')
            lista_horarios_turma.append(str(turma) + 'qui')
        elif i <= 44:
            lista_horarios_professor.append(str(professor) + 'sex')
            lista_horarios_turma.append(str(turma) + 'sex')
        else:
            break
    colisoes_professores = Counter(lista_horarios_professor).values()
    colisoes_turmas = Counter(lista_horarios_turma).values()

    for elemento in colisoes_professores:
        if elemento > 1:
            penalidade_colisao_professor += elemento * restricoes_duras

    for elemento in colisoes_turmas:
        if elemento > 1:
            penalidade_colisao_turma += elemento * restricoes_duras

    print(penalidade_colisao_professor)

    return cromossomo


cromo = [[15, 3, 22, 1], [15, 1, 35, 0], [26, 4, 35, 0], [20, 5, 33, 1], [14, 6, 24, 0], [15, 1, 36, 0], [26, 2, 46, 1], [20, 5, 20, 1], [10, 1, 31, 1], [27, 4, 32, 0], [9, 6, 14, 0], [2, 2, 5, 1], [21, 2, 25, 1], [27, 5, 14, 1], [19, 3, 37, 1], [10, 5, 13, 0], [11, 2, 25, 1], [5, 3, 15, 0], [22, 1, 42, 1], [32, 4, 34, 0], [13, 5, 30, 0], [19, 5, 39, 0], [15, 6, 24, 1], [7, 4, 49, 0], [15, 0, 44, 0], [15, 5, 40, 0], [7, 3, 15, 0], [9, 5, 14, 0], [32, 4, 5, 0], [31, 5, 18, 0], [7, 6, 37, 0], [30, 0, 6, 1], [28, 5, 39, 1], [29, 4, 45, 0], [15, 0, 18, 1], [15, 3, 48, 0], [30, 4, 9, 0], [27, 6, 37, 0], [17, 2, 50, 1], [23, 3, 35, 1], [11, 6, 17, 0], [28,
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               5, 49, 1], [19, 2, 11, 1], [3, 5, 47, 0], [12, 2, 12, 1]]

calcular_aptidao(cromo)


def selecao_torneio(populacao):
    pass


def crossover_ponto_unico(primeiro_pai, segundo_pai):
    pass


def multacao_com_mascara(cromossomo):
    pass


def executar():
    populacao = gerar_populacao()
    t = 0
    lista_schedule_viaveis = []

    while t < 1:
        for cromossomo in populacao:
            calcular_aptidao(cromossomo)

        t += 1
    return populacao


# print(len(executar()))
executar()
