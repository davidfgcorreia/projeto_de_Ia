# pipe.py: Template para implementação do projeto de Inteligência Artificial 2023/2024.
# Devem alterar as classes e funções neste ficheiro de acordo com as instruções do enunciado.
# Além das funções e classes sugeridas, podem acrescentar outras que considerem pertinentes.

# Grupo 00:
# 00000 Nome1
# 00000 Nome2
import sys
from search import (
    Problem,
    Node,
    astar_search,
    breadth_first_tree_search,
    depth_first_tree_search,
    greedy_search,
    recursive_best_first_search,
)
from numpy import(
    ndarray,array,
)

class PipeManiaState:
    state_id = 0

    def __init__(self, board):
        self.board = board
        self.id = PipeManiaState.state_id
        PipeManiaState.state_id += 1

    def __lt__(self, other):
        return self.id < other.id

    # TODO: outros metodos da classe





def get_value_num_l(self:list, row: int, col: int) -> tuple[int,int]:
    tamanho=len(self)
    if (row<0 or row>tamanho-1 or col<0 or col>tamanho-1):
        return 0
    return self[row][col]
"""Devolve o valor na respetiva posição do tabuleiro."""


# TODO
pass
def quero_cima(table:list, row: int, col: int) -> int:
    tamanho=len(table)
    ligacao= [-1,-1]
    if not (row > tamanho | row-1 < 0 | col > tamanho | col<0):
        ligacao= table[row-1][col]
        return [ligacao[0]%100//10,ligacao[1]]
    return ligacao
    # TODO
    pass
def quero_baixo(table:list ,row: int, col: int) -> int:
    ligacao= [-1,-1]
    tamanho=len(table)
    if not (row+1 > tamanho | row < 0 | col > tamanho | col<0):
        ligacao= table[row+1][col]
        return [ligacao[0]//1000,ligacao[1]]
    return ligacao
    # TODO
    pass
def quero_direita(table:list, row: int, col: int) -> int:
    ligacao= [-1,-1]
    tamanho=len(table)
    if not (row > tamanho | row < 0 | col+1 > tamanho | col<0):
        ligacao= table[row][col+1]
        return [ligacao[0]%10,ligacao[1]]
    return ligacao
    pass
def quero_esquerda(table:list, row: int, col: int) -> int:
    ligacao= [-1,-1]
    tamanho=len(table)
    if not (row > tamanho | row < 0 | col > tamanho | col-1<0):
        ligacao= table[row][col-1]
        return [ligacao[0]%1000//100,ligacao[1]]
    return ligacao
    # TODO
    pass


def roda(table:list , row: int , col: int , rotacao: int,estado:int ):
    peca=table[row][col][0]
    if rotacao==1:
        nova=peca%10*1000+ peca//1000*100+peca%1000//100*10+peca%100//10
    elif rotacao==2:
        nova= peca//1000*10+ peca%1000//100+ peca%100//10*1000 +peca%10*100
    elif rotacao==3:
        nova=peca//1000+ peca%1000//100*1000+peca%100//10*100+peca%10*10
    elif rotacao==4:
        nova=peca

    table[row][col]=[nova,estado]


def hipostese(table:list,row:int,col:int,lista_proximo:list):
    peca=table[row][col][0]
    dirpeca=[peca//1000,peca%1000//100,peca%100//10,peca%10]
    ligacao=dirpeca[0]+dirpeca[1]+dirpeca[2]+dirpeca[3]

    if ligacao==2:
        if (dirpeca[0]==dirpeca[2]|dirpeca[1]==dirpeca[3]):
            ligacao=4
            lista_proximo.append([row,col])
    if ligacao==3:
        if row==0:
            table[row][col]=[111,1]
            lista_proximo.append([row,col])
        elif row== len(table):
            table[row][col]=[1101,1]
            lista_proximo.append([row,col])
        elif col==0:
            table[row][col]=[1110,1]
            lista_proximo.append([row,col])
        elif col==len(table):
            table[row][col]=[1011,1]
            lista_proximo.append([row,col])
    elif ligacao==4:
        if row==0 or row == len(table):
            table[row][col]=[101,1]
            lista_proximo.append([row,col])
        elif col==0 or col == len(table):
            table[row][col]=[1010,1]
            lista_proximo.append([row,col])
    elif ligacao==2:
        if (row==0 and col==0):
            table[row][col]=[110,1]
            lista_proximo.append([row,col])
        if (row==0 and col==len(table)):
            table[row][col]=[11,1]
            lista_proximo.append([row,col])
        if (row==len(table) and col==0):
            table[row][col]=[1100,1]
            lista_proximo.append([row,col])
        if (row==len(table) and col==len(table)):
            table[row][col]=[1001,1]
            lista_proximo.append([row,col])
    
def busca_tipos(table:list,row:int,col:int):
    tamanho=len(table)
    ligacao=[[[-1,-1],-[-1,-1],[-1,-1],[-1,-1]],[False,False,False,False]]
    if not(row > tamanho | row-1 < 0 | col > tamanho | col<0):
        ligacao[0][0]= table[row-1][col]
        ligacao[1][0]=(str(ligacao[0][0][0]).count('1')==True)
    if not (row+1 > tamanho | row < 0 | col > tamanho | col<0):
        ligacao[0][1]= table[row+1][col][0]
        ligacao[1][1]=(str(ligacao[0][0][0]).count('1')==True)
    if not (row > tamanho | row < 0 | col+1 > tamanho | col<0):
        ligacao[0][2]= table[row][col+1]
        ligacao[1][2]=(str(ligacao[0][0][0]).count('1')==True)
    if not (row > tamanho | row < 0 | col > tamanho | col-1<0):
        ligacao[0][3]= table[row][col-1]
        ligacao[1][3]=(str(ligacao[0][0][0]).count('1')==True)
    return ligacao



def hipostese_int(table:list,row:int,col:int, list_actions: list,lista_proximo:list):
    pecat=table[row][col]
    if (peca[1]==1):
        return
    peca=pecat[0]
    dirpeca=[peca//1000,peca%1000//100,peca%100//10,peca%10]
    ligacao=dirpeca[0]+dirpeca[1]+dirpeca[2]+dirpeca[3]
    postos=[0,0,0,0]
    if ligacao==1:
        direcoesl=busca_tipos(table,row,col)
        direcoes=direcoesl[0]
        tipos=direcoesl[1]
    else:
        direcoes=[quero_cima(table,row,col),quero_direita(table,row,col),quero_baixo(table,row,col),quero_esquerda(table,row,col)]
    for i in range(4):
        if(direcoes[i]==[1,1]):
            postos[i]=1
        elif(direcoes[i]==[1,0]):
            postos[i]=0
        elif(direcoes[i]==[0,1]):
            postos[i]=-1
        elif(direcoes[i]==[-1,-1]):
            postos[i]=-1
        if ligacao==1:
            if tipos[i]:
                postos[i]=-1
        
    lista=[]
    for i in range(4):
        for j in range(4):
            t=j+i
            if(t>3):
                t-=3
            if postos[t]==1 and dirpeca[j]!=1:
                break
            elif postos[t]==-1 and dirpeca[j]!=0:
                break
            lista.append(i)
    
    if (peca==1010 or peca==101)and len(lista)==2:
        lista.pop()
        


    if (len(lista)==1):
        roda(table,row,col,lista[0],1)
        lista_proximo.append([row,col])
    else:
        list_actions.append([lista,[row,col]])

            
            

def ligacoes(table:list,row:int , col:int)->int :
    peca=table[row][col]
    direcoes=[quero_cima(table,row,col),quero_direita(table,row,col),quero_baixo(table,row,col),quero_esquerda(table,row,col)]
    dirpeca=[peca//1000,peca%1000//100,peca%100//10,peca%10]
    lig=0
    lig_total=0
    for i in range(4):
            if (direcoes[i]==1 & dirpeca[i]==1):
                lig+=1
            if (dirpeca[i]==1):
                lig_total+=1
    return lig/lig_total



def place_piece(action:list,board:list ) ->list:#temos que fazer o copy normal nao podemos usar o deep
        """Devolve um novo tabuleiro com o valor colocado na posição indicada."""
        new_table  = []
        for i in board:
            intern=[]
            for j in i:
                novo=[j[0],j[1]]
                intern.append(novo)
            new_table.append(intern)

        roda(new_table,action[1][0],action[1][1],action[0],1)

        return new_table









@staticmethod
def parse_instance():
    table_lig=[]
    j=0
    while 1:
        line= sys.stdin.readline().split()
        if line== "":
            break
        table_lig.append([])
        for i in line:
            if i== "FC":
                table_lig[j].append([1000,0])
            elif i== "FB":
                table_lig[j].append([100,0])
            elif i== "FE":
                table_lig[j].append([10,0])
            elif i== "FD":
                table_lig[j].append([1,0])
            elif i== "BC":
                table_lig[j].append([1101,0])
            elif i== "BB":
                table_lig[j].append([1110,0])
            elif i== "BE":
                table_lig[j].append([111,0])
            elif i== "BD":
                table_lig[j].append([1011,0])
            elif i== "VC":
                table_lig[j].append([1001,0])
            elif i== "VB":
                table_lig[j].append([110,0])
            elif i== "VE":
                table_lig[j].append([11,0])
            elif i== "VD":
                table_lig[j].append([1100,0])
            elif i== "LH":
                table_lig[j].append([101,0])
            elif i== "LV":
                table_lig[j].append([1010,0])
        j=j+1

    return table_lig

# TODO: outros metodos da classe



def criar_grafo(lista_de_listas:list):
    grafo = {}
    
    # Iterar sobre a lista de listas e adicionar os nós ao grafo
    for i in range(len(lista_de_listas)):
        for j in range(len(lista_de_listas[i])):
            node = (i,j)  # Converter lista em tupla
            if node not in grafo:
                grafo[node] = set()
            peca=lista_de_listas[i][j][0]
            direcoes=[quero_cima(lista_de_listas,i,j),quero_direita(lista_de_listas,i,j),quero_baixo(lista_de_listas,i,j),quero_esquerda(lista_de_listas,i,j)]
            # Adicionar conexões com os elementos adjacentes
            if (direcoes[0]==peca//1000):
                grafo[node].add((i-1,j))
            if (direcoes[0]==peca%1000//100):
                grafo[node].add((i+1,j))
            if(direcoes[0]==peca%100//10):
                grafo[node].add((i,j-1))
            if (direcoes[0]==peca%10):
                grafo[node].add((i,j+1))
                
    return grafo


def dfs_iterativa(grafo, inicio, visitados):
    pilha = [inicio]
    
    while pilha:
        vertice = pilha.pop()
        if vertice not in visitados:
            visitados.add(vertice)
            pilha.extend(grafo[vertice] - visitados)

def verifica_conexao_total(grafo):
    todos_nos = set(grafo.keys())
    visitados = set()
    
    # Realiza a busca em profundidade iterativa a partir de qualquer nó
    for i in todos_nos:
        if i not in visitados:
            dfs_iterativa(grafo,i, visitados)
            break
    # Verifica se todos os nós foram visitados
    return visitados == todos_nos



def inferencia1(state:list):#isto em vez de board tem que se usar o pipestate
    tamanho=len(state)
    lista_proximo=[]
    for i in range(tamanho):
        hipostese(state,0,i,lista_proximo)
        hipostese(state,tamanho,i,lista_proximo)
        hipostese(state,i,0,lista_proximo)
        hipostese(state,i,tamanho,lista_proximo)
    return lista_proximo

def inferencia2(table:list ,lista_proximo:list):
    while(len(lista_proximo)!=0):
        ponto=lista_proximo.pop(0)
        hipostese_int(table, ponto[0],ponto[1],lista_proximo)

    

    """Retorna uma lista de ações que podem ser executadas a
    partir do estado passado como argumento."""
    # TODO
    pass


def actions(state:list,list_actions:list):
    for i in range(len(list_actions)):
        if (state.get_value(list_actions[i][1][0],list_actions[i][1][1])[1]==1):
            list_actions.pop(i)
        elif(len(list_actions[i][0])==2):
            return list_actions[i]
    return list_actions[0]   
    """Retorna uma lista de ações que podem ser executadas a
    partir do estado passado como argumento."""
    # TODO
    pass

def result(self, state: PipeManiaState, action:list):

    new_board= place_piece(state,action)
    """Retorna o estado resultante de executar a 'action' sobre
    'state' passado como argumento. A ação a executar deve ser uma
    das presentes na lista obtida pela execução de
    self.actions(state)."""
    # TODO
    pass


def goal_test(self, state: PipeManiaState):
    """Retorna True se e só se o estado passado como argumento é
    um estado objetivo. Deve verificar se todas as posições do tabuleiro
    estão preenchidas de acordo com as regras do problema."""
    # TODO
    pass

def h(self, node: Node):
    """Função heuristica utilizada para a procura A*."""
    # TODO
    pass

# TODO: outros metodos da classe




if __name__ == "__main__":
    # TODO:
    # Ler o ficheiro do standard input,
    # Usar uma técnica de procura para resolver a instância,
    # Retirar a solução a partir do nó resultante,
    # Imprimir para o standard output no formato indicado.
    pass
