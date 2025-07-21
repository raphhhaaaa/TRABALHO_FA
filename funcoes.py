from dataclasses import dataclass

@dataclass
class Time:
    nome: str
    vitorias: int
    pontos: int
    tot_gols: int

#jogos = ['Sao-Paulo 1 Atletico-MG 2', 'Flamengo 2 Palmeiras 1', 'Palmeiras 0 Sao-Paulo 0', 'Atletico-MG 1 Flamengo 2']    
#jogos = ['Flamengo 2 Gremio 0', 'Palmeiras 1 Corinthians 1', 'Sao-Paulo 0 Flamengo 1', 'Gremio 1 Palmeiras 3']
jogos = ['Atletico-PR 2 Coritiba 1', 'Londrina 1 Parana-Clube 1', 'Atletico-PR 1 Londrina 0', 'Coritiba 3 Parana-Clube 0',
          'Atletico-PR 2 Parana-Clube 2', 'Coritiba 1 Londrina 1', 'Coritiba 1 Atletico-PR 0', 'Parana-Clube 0 Londrina 1',
           'Londrina 2 Atletico-PR 2', 'Parana-Clube 1 Coritiba 2', 'Parana-Clube 0 Atletico-PR 3', 'Londrina 1 Coritiba 1']

def time_anfitriao(resultado: str) -> str:
    '''
    Dado uma string *resultado* de jogo entre dois times, retorna o nome do time 
    anfitrião (mais a esquerda).

    Exemplos: 

    >>> time_anfitriao('Sao-Paulo 2 Flamengo 1')
    'Sao-Paulo'
    '''
    ind_espaco = 0
    while resultado[ind_espaco] != ' ':
        ind_espaco = ind_espaco + 1
    return resultado[:ind_espaco]
def time_visitante(resultado: str) -> str:
    '''
    Dado uma string *resultado* de jogo entre dois times, retorna o nome do time
    visitante (mais a direita).

    Exemplos:

    >>> time_visitante('Sao-Paulo 2 Flamengo 1')
    'Flamengo'
    '''
    prim_espaco = 0
    while resultado[prim_espaco] != ' ':
        prim_espaco = prim_espaco + 1

    for c in range(0, len(resultado) - 1):
        if resultado[c] == ' ':
            ult_espaco = c
    return resultado[prim_espaco + 3:ult_espaco]

def gols_anfitriao(resultado: str) -> int:
    '''
    Identifica e retorna a pontuação do time anfitrião com base no *resultado* de um determinado jogo.

    Exemplos: 

    >>> gols_anfitriao('Flamengo 2 Palmeiras 1')
    2
    >>> gols_anfitriao('Palmeiras 0 Sao-Paulo 0')
    0
    >>> gols_anfitriao('Atletico-MG 1 Flamengo 2')
    1
    '''
    ind_espaco = 0
    while resultado[ind_espaco] != ' ':
        ind_espaco = ind_espaco + 1
    return int(resultado[ind_espaco + 1])
def gols_visitante(resultado: str) -> int:

    '''
    Identifica e retorna a pontuação do time visitante com base no *resultado* de um determinado jogo.

    Exemplos: 

    >>> gols_visitante('Flamengo 2 Palmeiras 1')
    1
    >>> gols_visitante('Palmeiras 0 Sao-Paulo 0')
    0
    >>> gols_visitante('Atletico-MG 1 Flamengo 2')
    2
    '''
    for c in range(0, len(resultado) - 1):
        if resultado[c] == ' ':
            ult_espaco = c
    return int(resultado[ult_espaco + 1])  

def vitoria(resultado: str) -> str:
    '''
    Retorna qual foi o time vencedor com base no *resultado* de uma partida.
    Retorna 'EMPATE' caso os gols do time anfitrião e do time visitante sejam iguais.
    Exemplos:

    >>> vitoria('Flamengo 2 Palmeiras 1')
    'Flamengo'
    >>> vitoria('Palmeiras 0 Sao-Paulo 0')
    'EMPATE'
    >>> vitoria('Sao-Paulo 1 Atletico-MG 2')
    'Atletico-MG'
    '''
    if gols_anfitriao(resultado) > gols_visitante(resultado):
        vitoria = time_anfitriao(resultado)
    elif gols_visitante(resultado) > gols_anfitriao(resultado):
        vitoria = time_visitante(resultado)
    else:
        vitoria = 'EMPATE'
    return vitoria

def conta_vitorias(time: str, jogos: list) -> int:
    '''
    Recebe o nome de um *time* e *jogos* com o resultado de várias partidas, 
    e retorna o número de vitórias que *time* conquistou.
    Se o resultado de *jogo* for empatado retorna 'EMPATE'.

    Exemplos:

    >>> conta_vitorias('Flamengo', ['Sao-Paulo 1 Atletico-MG 2', 'Flamengo 2 Palmeiras 1', 'Palmeiras 0 Sao-Paulo 0', 'Atletico-MG 1 Flamengo 2'])
    2
    >>> conta_vitorias('Atletico-MG', ['Sao-Paulo 1 Atletico-MG 2', 'Flamengo 2 Palmeiras 1', 'Palmeiras 0 Sao-Paulo 0', 'Atletico-MG 1 Flamengo 2'])
    1
    >>> conta_vitorias('Sao-Paulo', ['Sao-Paulo 1 Atletico-MG 2', 'Flamengo 2 Palmeiras 1', 'Palmeiras 0 Sao-Paulo 0', 'Atletico-MG 1 Flamengo 2'])
    0
    '''
    time_vencedores = []
    for jogo in jogos:
        time_vencedores.append(vitoria(jogo))
    cont = 0
    for v in time_vencedores:
        if time == v:
            cont = cont + 1
    return cont

def saldo_gols(time: str, jogos: list) -> int:
    '''
    Determina o saldo de gols de determinado *time* a partir da diferença de quantos gols foram feitos por
    quantos gols foram sofridos. Basedo em uma lista de *jogos*.

    Exemplos:

    >>> saldo_gols('Flamengo', ['Sao-Paulo 1 Atletico-MG 2', 'Flamengo 2 Palmeiras 1', 'Palmeiras 0 Sao-Paulo 0', 'Atletico-MG 1 Flamengo 2'])
    2
    >>> saldo_gols('Sao-Paulo', ['Sao-Paulo 1 Atletico-MG 2', 'Flamengo 2 Palmeiras 1', 'Palmeiras 0 Sao-Paulo 0', 'Atletico-MG 1 Flamengo 2'])
    -1
    >>> saldo_gols('Atletico-MG', ['Sao-Paulo 1 Atletico-MG 2', 'Flamengo 2 Palmeiras 1', 'Palmeiras 0 Sao-Paulo 0', 'Atletico-MG 1 Flamengo 2'])
    0
    '''
    gols = 0
    sofreu = 0
    for jogo in jogos:
        if jogo[:prim_espaco(jogo)] == time:
            gols = gols + int(jogo[prim_espaco(jogo) + 1])
        elif jogo[prim_espaco(jogo) + 3:ulti_espaco(jogo)] == time:
            gols = gols + int(jogo[ulti_espaco(jogo) + 1])
        if jogo[:prim_espaco(jogo)] == time:
            sofreu = sofreu + int(jogo[ulti_espaco(jogo) + 1])
        elif jogo[prim_espaco(jogo) + 3:ulti_espaco(jogo)] == time:
            sofreu = sofreu + int(jogo[prim_espaco(jogo) + 1])
    return gols - sofreu
def empate(time: str, jogo: str) -> bool:
    '''
    Determina se determinado *time* empatou em um *jogo*. Retorna True caso sim, e False caso contrário.

    >>> empate('Sao-Paulo', 'Sao-Paulo 1 Atletico-MG 2')
    False
    >>> empate('Sao-Paulo', 'Palmeiras 0 Sao-Paulo 0')
    True
    >>> empate('Palmeiras', 'Palmeiras 0 Sao-Paulo 0')
    True
    '''
    empate = False
    if gols_anfitriao(jogo) == gols_visitante(jogo):
        if time == time_anfitriao(jogo) or time == time_visitante(jogo):
            empate = True
    return empate

def calcula_pontos(time: str) -> int:
    '''
    Calcula a quantidade de pontos que determinado *time* possui com base em suas vitórias e empates.

    Exemplos:

    >>> calcula_pontos('Flamengo')
    6
    '''
    pontos = conta_vitorias(time, jogos) * 3
    for jogo in jogos:
        if empate(time, jogo) == True:
            pontos = pontos + 1
    return pontos

def ulti_espaco(jogo: str) -> int:
    '''
    Identifica o índice do último espaço em branco de uma string *jogo*.

    Exemplos:

    >>> ulti_espaco('Sao-Paulo 1 Atletico-MG 2')
    23
    >>> ulti_espaco('Palmeiras 0 Sao-Paulo 0')
    21
    >>> ulti_espaco('Flamengo 2 Palmeiras 1')
    20
    '''
    idx = 0
    for c in range(0, len(jogo)): 
        if jogo[c] == ' ':
            idx = c
    return idx

def prim_espaco(jogo: str) -> int:
    '''
    Identifica o índice do primeiro espaço em branco de uma string *jogo*.

    Exemplo: 

    >>> prim_espaco('Sao-Paulo 1 Atletico-MG 2')
    9
    >>> prim_espaco('Flamengo 2 Palmeiras 1')
    8
    >>> prim_espaco('Atletico-MG 1 Flamengo 2')
    11
    '''
    idx = 0
    while jogo[idx] != ' ':
        idx = idx + 1
    return idx

def times_compostos(jogos: list) -> list:
    '''
    Organiza todos os dados (nome, vitorias, pontos, saldo de gols) dos times da lista *jogos* em um tipo composto e os coloca em uma lista.
    Remove os excedentes de times repetidos se houver.

    Exemplos:

    >>> times_compostos(['Sao-Paulo 1 Atletico-MG 2', 'Flamengo 2 Palmeiras 1', 'Palmeiras 0 Sao-Paulo 0', 'Atletico-MG 1 Flamengo 2'])
    [Time(nome='Sao-Paulo', vitorias=0, pontos=1, tot_gols=-1), Time(nome='Flamengo', vitorias=2, pontos=6, tot_gols=2), Time(nome='Palmeiras', vitorias=0, pontos=1, tot_gols=-1), Time(nome='Atletico-MG', vitorias=1, pontos=3, tot_gols=0)]
    '''
    aux = []
    times = []
    for j in range(0, len(jogos)):
        aux.append(Time(time_anfitriao(jogos[j]), conta_vitorias(time_anfitriao(jogos[j]), jogos), calcula_pontos(time_anfitriao(jogos[j])), saldo_gols(time_anfitriao(jogos[j]), jogos)))
    for time in aux:
        if acha_x(times, time.nome) == False:
            times.append(time)
    return times

def maior_nome(jogos: list[str]) -> str:
    '''
    Identifica e retorna o time com maior quantidade de caracteres.

    Exemplos: 

    >>> maior_nome(['Sao-Paulo 1 Atletico-MG 2', 'Flamengo 2 Palmeiras 1', 'Palmeiras 0 Sao-Paulo 0', 'Atletico-MG 1 Flamengo 2'])
    'Atletico-MG'
    '''
    maior = len(time_anfitriao(jogos[0]))
    nome = time_anfitriao(jogos[0])
    for j in range(0, len(jogos)):
        if len(time_anfitriao(jogos[j])) > maior:
            maior = len(time_anfitriao(jogos[j]))
            nome = time_anfitriao(jogos[j])
    return nome        

def classifica_times(dados: list[Time]) -> str:
    '''
    Classifica os times em uma tabela com base em seus *pontos* e outros critérios de classificação.
    
    Exemplos:

    >>> t1 = [Time(nome='Flamengo', vitorias=2, pontos=6, tot_gols=2), Time(nome='Atletico-MG', vitorias=1, pontos=3, tot_gols=0), Time(nome='Sao-Paulo', vitorias=0, pontos=1, tot_gols=-1), Time(nome='Palmeiras', vitorias=0, pontos=1, tot_gols=-1)]

    >>> classifica_times(t1)
    TIME        P V  S
    Flamengo    6 2  2
    Atletico-MG 3 1  0
    Sao-Paulo   1 0  -1
    Palmeiras   1 0  -1
    ''
    '''
    espaco = len(maior_nome(jogos)) - 4
    print('=-=-' * 10)
    print('TIME' + ' ' * espaco , 'P', 'V',' ' 'S')
    for time in dados:
        print(time.nome + ' ' *(len(maior_nome(jogos)) - len(time.nome)), time.pontos, time.vitorias,'', time.tot_gols)
    return '=-=-' * 10

def ordena_pontos(dados: list[Time]) -> list[Time]:
    '''
	Ordena a lista de tipo composto *dados* dos times em ordem decrescente, do time que mais pontuou ao time que menos pontou.
	
	Exemplos:
	
	>>> t1 = [Time(nome='Sao-Paulo', vitorias=0, pontos=1, tot_gols=-1), Time(nome='Flamengo', vitorias=2, pontos=6, tot_gols=2), Time(nome='Palmeiras', vitorias=0, pontos=1, tot_gols=-1), Time(nome='Atletico-MG', vitorias=1, pontos=3, tot_gols=0)]
				
	>>> ordena_pontos(t1)
	[Time(nome='Flamengo', vitorias=2, pontos=6, tot_gols=2), Time(nome='Atletico-MG', vitorias=1, pontos=3, tot_gols=0), Time(nome='Sao-Paulo', vitorias=0, pontos=1, tot_gols=-1), Time(nome='Palmeiras', vitorias=0, pontos=1, tot_gols=-1)]
    '''
    houve_troca = True
    aux = dados[0]
    while houve_troca == True:
        houve_troca = False
        for i in range(len(dados) - 1):
            if dados[i].pontos < dados[i + 1].pontos:
                aux = dados[i]
                dados[i] = dados[i + 1]
                dados[i + 1] = aux
                houve_troca = True
    return dados

def acha_x(times: list[Time], string: str) -> bool:
    '''
    Identifica se uma *string* existe em *lista*. Retorna True caso exista
    e False caso não exista.

    Exemplos:

    >>> acha_x([], 'Atletico-PR')
    False
    >>> acha_x(['Atletico-PR', 'Londrina', 'Coritiba'], 'Atletico-PR')
    True
    >>> acha_x(['Atletico-PR', 'Londrina', 'Coritiba'], 'Flamengo')
    False
    >>> acha_x(['Flamengo', 'Corinthians', 'Palmeiras', 'Botafogo'], 'Palmeiras')
    True
    '''
    encontrou = False
    for time in times:
        if time.nome == string:
            encontrou = True
    return encontrou

def tira_n(resultados: list[str]):
    '''
    função pra tirar o \n da lista que vem depois sys ler o txt. (EM ANDAMENTO)
    '''
    jogos = []
     
    return jogos
print(tira_n(['Sao-Paulo 1 Atletico-MG 2\n', 'Flamengo 2 Palmeiras 1\n', 'Palmeiras 0 Sao-Paulo 0\n', 'Atletico-MG 1 Flamengo 2\n']))
#print(classifica_times(ordena_pontos(times_compostos(jogos))))
#print(times_compostos(jogos))