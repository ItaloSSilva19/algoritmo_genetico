# Algoritmo Genético
Implementação em python

Esta atividade foi realizada na disciplina de **FUNDAMENTOS DE INTELIGÊNCIA ARTIFICIAL**, que é ministrada pelo professor **Fabiano Fagundes**.  
A função deste algoritmo é resolver o **problema de calendário de aulas (Timetabling Problem)**

## Equipe:
- Anna Julia Cardoso Lira
- Gabriel Vitor Silva Barbosa
- Ítalo de Souza Silva
- Julio Alexandre Costa Neto
- Maria Eduarda Alves Bottega
- Rayanna Quirino De Sousa
- Wesley Miranda Novaes

# Atividade

## Problema
Como alocar os professores e suas disciplinas nos dias da semana e laboratórios de forma a respeitar:

### Restrições duras:
- Professor não pode dar duas ou mais aulas no mesmo período
- Mesma turma não pode ter duas ou mais aulas no mesmo período
- Os tamanhos das salas e laboratórios devem estar adequados aos tamanhos das turmas
- turmas práticas devem ser em laboratório(Labin)

### Restrições leves:
- Professor não pode dar aula em determinado dia
- Determinado laboratório ou sala não está disponível em determinado dia

<sub>Obs: as aulas são de 2ª a 6ª</sub>

## Informações sobre laboratórios e salas:
**Labin 1:** **50** lugares  
**Labin 2:** não pode ser reservado  
**Labin 3:** **20** lugares  
**Labin 4:** **30** lugares  
**Labin 5:** **40** lugares  
**Labin 6:** **40** lugares  
**Sala de aula 1:** **50** lugares  
**Sala de aula 2:** **50** lugares  
**Sala de aula 3:** **40** lugares  

## Turmas:
Turma **A1** -- professor **1** -- **27** alunos -- **P**  
Turma **A2** -- professor **2** -- **33** alunos -- **P**  
Turma **A3** -- professor **4** -- **25** alunos -- **P**  
Turma **A4** -- professor **4** -- **25** alunos -- **T**  
Turma **A5** -- professor **5** -- **42** alunos -- **T**  
Turma **B1** -- professor **1** -- **31** alunos -- **P**  
Turma **B2** -- professor **2** -- **26** alunos -- **P**  
Turma **B3** -- professor **3** -- **20** alunos -- **P**  
Turma **B4** -- professor **5** -- **45** alunos -- **T**  
Turma **B5** -- professor **6** -- **42** alunos -- **T**  
Turma **C1** -- professor **6** -- **20** alunos -- **P**  
Turma **C2** -- professor **5** -- **19** alunos -- **P**  
Turma **C3** -- professor **1** -- **43** alunos -- **P**  
Turma **C4** -- professor **6** -- **45** alunos -- **P**  
Turma **D1** -- professor **7** -- **30** alunos -- **P**  
Turma **D2** -- professor **2** -- **20** alunos -- **P**  
Turma **D3** -- professor **7** -- **30** alunos -- **P**  
Turma **D4** -- professor **3** -- **20** alunos -- **P**  
Turma **E1** -- professor **7** -- **27** alunos -- **T**  
Turma **E2** -- professor **2** -- **22** alunos -- **P**  
Turma **E3** -- professor **7** -- **26** alunos -- **P**  
Turma **E4** -- professor **4** -- **25** alunos -- **P**  
Turma **E5** -- professor **7** -- **25** alunos -- **P**  
Turma **F1** -- professor **4** -- **22** alunos -- **P**  
Turma **F2** -- professor **6** -- **30** alunos -- **P**  
Turma **F3** -- professor **1** -- **21** alunos -- **P**  
Turma **F4** -- professor **3** -- **25** alunos -- **T**  
Turma **G1** -- professor **3** -- **25** alunos -- **P**  
Turma **G2** -- professor **4** -- **44** alunos -- **P**  
Turma **G3** -- professor **5** -- **44** alunos -- **T**  
Turma **H1** -- professor **1** -- **25** alunos -- **P**  
Turma **H2** -- professor **3** -- **44** alunos -- **P**  
Turma **H3** -- professor **5** -- **44** alunos -- **T**  
