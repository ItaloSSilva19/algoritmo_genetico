from calendar import c
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

    lista_horarios_professor = []
    penalidade_colisao_professor = 0

    penalidade_colisao_turma = 0
    lista_horarios_turma = []

    penalidade_capacidade_sala_insuficiente = 0

    penalidade_tipo_local_incompativel = 0

    restricoes_leves = 1

    penalidade_local_indisponivel = 0

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

        quantidade_alunos = eventos[cromossomo[i][0]][2]
        tipo_local = eventos[cromossomo[i][0]][3]

        if i == 0 or i == 9 or i == 18 or i == 27 or i == 36:  # L1
            if quantidade_alunos < locais[0][1]:
                penalidade_capacidade_sala_insuficiente += 1
        elif i == 1 or i == 10 or i == 19 or i == 28 or i == 37:  # L2
            penalidade_local_indisponivel += 1
            if quantidade_alunos < locais[1][1]:
                penalidade_capacidade_sala_insuficiente += 1

        elif i == 2 or i == 11 or i == 20 or i == 29 or i == 38:  # L3
            if quantidade_alunos < locais[2][1]:
                penalidade_capacidade_sala_insuficiente += 1

        elif i == 3 or i == 12 or i == 21 or i == 30 or i == 39:  # L4
            if quantidade_alunos < locais[3][1]:
                penalidade_capacidade_sala_insuficiente += 1

        elif i == 4 or i == 13 or i == 22 or i == 31 or i == 40:  # L5
            if quantidade_alunos < locais[4][1]:
                penalidade_capacidade_sala_insuficiente += 1

        elif i == 5 or i == 14 or i == 23 or i == 32 or i == 41:  # L6
            if quantidade_alunos < locais[5][1]:
                penalidade_capacidade_sala_insuficiente += 1
        elif i == 6 or i == 15 or i == 24 or i == 33 or i == 42:  # S1
            if quantidade_alunos < locais[6][1]:
                penalidade_capacidade_sala_insuficiente += 1

        elif i == 7 or i == 16 or i == 25 or i == 34 or i == 43:  # S2
            if tipo_local == 1:
                penalidade_tipo_local_incompativel += 1
            if quantidade_alunos < locais[7][1]:
                penalidade_capacidade_sala_insuficiente += 1

        elif i == 8 or i == 17 or i == 26 or i == 35 or i == 44:  # S3
            if tipo_local == 1:
                penalidade_tipo_local_incompativel += 1
            if quantidade_alunos < locais[8][1]:
                penalidade_capacidade_sala_insuficiente += 1

    colisoes_professores = Counter(lista_horarios_professor).values()
    colisoes_turmas = Counter(lista_horarios_turma).values()

    for elemento in colisoes_professores:
        if elemento > 1:
            penalidade_colisao_professor += elemento * restricoes_duras

    for elemento in colisoes_turmas:
        if elemento > 1:
            penalidade_colisao_turma += elemento * restricoes_duras

    penalidade_capacidade_sala_insuficiente *= restricoes_duras

    penalidade_tipo_local_incompativel *= restricoes_duras

    penalidade_local_indisponivel *= restricoes_leves

    somatorio_penalidades = penalidade_local_indisponivel + penalidade_capacidade_sala_insuficiente + \
        penalidade_colisao_professor + penalidade_colisao_turma + \
        penalidade_tipo_local_incompativel

    aptidao = 1 / (1 + somatorio_penalidades)

    cromossomo.append(aptidao)

    return cromossomo


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
