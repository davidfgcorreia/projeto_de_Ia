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

#posso fazer um try exept em vez dos ifs de borda
def quero_cima(table:list, row: int, col: int) -> int:
    tamanho=len(table)-1
    ligacao= [-1,-1]
    if not (row > tamanho or row-1 < 0 or col > tamanho or col<0):
        ligacao= table[row-1][col]
        return [ligacao[0]%100//10,ligacao[1]]
    return ligacao
    # TODO
    pass
def quero_baixo(table:list ,row: int, col: int) -> int:
    ligacao= [-1,-1]
    tamanho=len(table)-1
    if not (row+1 > tamanho or row < 0 or col > tamanho or col<0):
        ligacao= table[row+1][col]
        return [ligacao[0]//1000,ligacao[1]]
    return ligacao
    # TODO
    pass
def quero_esquerda(table:list, row: int, col: int) -> int:
    ligacao= [-1,-1]
    tamanho=len(table)-1
    if not (row > tamanho or row < 0 or col > tamanho or col-1<0):
        ligacao= table[row][col-1]
        return [ligacao[0]%1000//100,ligacao[1]]
    return ligacao
    pass
def quero_direita(table:list, row: int, col: int) -> int:
    ligacao= [-1,-1]
    tamanho=len(table)-1
    if not (row > tamanho or row < 0 or col+1 > tamanho or col<0):
        ligacao= table[row][col+1]
        return [ligacao[0]%10,ligacao[1]]
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
    elif rotacao==0:
        nova=peca

    table[row][col]=[nova,estado]


def hipostese(table:list,row:int,col:int,lista_proximo:list,bons:list):
    peca=table[row][col][0]
    dirpeca=[peca//1000,peca%1000//100,peca%100//10,peca%10]
    ligacao=dirpeca[0]+dirpeca[1]+dirpeca[2]+dirpeca[3]
    if ligacao==2:
        if (dirpeca[0]==dirpeca[2] and dirpeca[1]==dirpeca[3]):
            ligacao=4
    if ligacao==3:
        if row==0:
            table[row][col]=[111,1]
            lista_proximo.append([row+1,col])
            lista_proximo.append([row,col+1])
            lista_proximo.append([row,col-1])
            lista_proximo.append([row-1,col])
            bons[0]+=1
        elif row== len(table)-1:
            table[row][col]=[1101,1]
            lista_proximo.append([row+1,col])
            lista_proximo.append([row,col+1])
            lista_proximo.append([row,col-1])
            lista_proximo.append([row-1,col])
            bons[0]+=1
        elif col==0:
            table[row][col]=[1110,1]
            lista_proximo.append([row+1,col])
            lista_proximo.append([row,col+1])
            lista_proximo.append([row,col-1])
            lista_proximo.append([row-1,col])
            bons[0]+=1
        elif col==len(table)-1:
            table[row][col]=[1011,1]
            lista_proximo.append([row+1,col])
            lista_proximo.append([row,col+1])
            lista_proximo.append([row,col-1])
            lista_proximo.append([row-1,col])
            bons[0]+=1
    elif ligacao==4:
        if row==0 or row == len(table)-1:
            table[row][col]=[101,1]
            lista_proximo.append([row+1,col])
            lista_proximo.append([row,col+1])
            lista_proximo.append([row,col-1])
            lista_proximo.append([row-1,col])
            bons[0]+=1
        elif col==0 or col == len(table)-1:
            table[row][col]=[1010,1]
            lista_proximo.append([row+1,col])
            lista_proximo.append([row,col+1])
            lista_proximo.append([row,col-1])
            lista_proximo.append([row-1,col])
            bons[0]+=1
    elif ligacao==2:
        if (row==0 and col==0):
            if(table[row][col][1]==0):
                table[row][col]=[110,1]
                lista_proximo.append([row+1,col])
                lista_proximo.append([row,col+1])
                lista_proximo.append([row,col-1])
                lista_proximo.append([row-1,col])
                bons[0]+=1
        if (row==0 and col==len(table)-1):
            if(table[row][col][1]==0):
                table[row][col]=[11,1]
                lista_proximo.append([row+1,col])
                lista_proximo.append([row,col+1])
                lista_proximo.append([row,col-1])
                lista_proximo.append([row-1,col])
                bons[0]+=1
        if (row==len(table) -1 and col==0):
            if(table[row][col][1]==0):
                table[row][col]=[1100,1]
                lista_proximo.append([row+1,col])
                lista_proximo.append([row,col+1])
                lista_proximo.append([row,col-1])
                lista_proximo.append([row-1,col])
                bons[0]+=1
        if (row==len(table) -1 and col==len(table)-1 ):
            if(table[row][col][1]==0):
                table[row][col]=[1001,1]
                lista_proximo.append([row+1,col])
                lista_proximo.append([row,col+1])
                lista_proximo.append([row,col-1])
                lista_proximo.append([row-1,col])
                bons[0]+=1
    
def busca_tipos(table:list,row:int,col:int):#posso fazer um try exept em vez dos ifs
    tamanho=len(table)-1
    ligacao=[[[-1,-1],[-1,-1],[-1,-1],[-1,-1]],[0,0,0,0]]
    if not(row > tamanho or row-1 < 0 or col > tamanho or col<0):
        ligacao[0][0]= [table[row-1][col][0]%100//10,table[row-1][col][1]]
        ligacao[1][0]=(str(table[row-1][col][0]).count('1'))
    if not (row > tamanho or row < 0 or col+1 > tamanho or col<0):
        ligacao[0][1]= [table[row][col+1][0]%10,table[row][col+1][1]]
        ligacao[1][1]=(str(table[row][col+1][0]).count('1'))
    if not (row+1 > tamanho or row < 0 or col > tamanho or col<0):
        ligacao[0][2]= [table[row+1][col][0]//1000,table[row+1][col][1]]
        ligacao[1][2]=(str(table[row+1][col][0]).count('1'))
    if not (row > tamanho or row < 0 or col > tamanho or col-1<0):
        ligacao[0][3]= [table[row][col-1][0]%1000//100,table[row][col-1][1]]
        ligacao[1][3]=(str(table[row][col-1][0]).count('1'))

    return ligacao



def hipostese_2(table:list,row:int,col:int, list_actions: list,lista_proximo:list,bons:list):
    pecat=table[row][col]
    if (pecat[1]==1 or row<0 or col<0):
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
        return
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
            if tipos[i]==1:
                postos[i]=-1
    

        
    lista=[]
    for i in range(4):
        for j in range(4):
            t=j+i
            if(t>3):
                t-=4
            if postos[t]==1 and dirpeca[j]!=1:
                break
            if postos[t]==-1 and dirpeca[j]!=0:
                break
            if j==3:
                lista.append(i)
    
    if (peca==1010 or peca==101)and len(lista)==2:
        lista.pop()
        


    if (len(lista)==1):
        roda(table,row,col,lista[0],1)
        lista_proximo.append([row+1,col])
        lista_proximo.append([row,col+1])
        lista_proximo.append([row,col-1])
        lista_proximo.append([row-1,col])
        bons[0]+=1
    else:
        list_actions.append([lista,[row,col]])

def hipostese_int(table:list,row:int,col:int, list_actions: list,lista_proximo:list,bons:list):
    try:
        pecat=table[row][col]
    except IndexError:
        return
    if (pecat[1]==1 or row<0 or col<0):
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
            if tipos[i]==1:
                postos[i]=-1
    

        
    lista=[]
    for i in range(4):
        for j in range(4):
            t=j+i
            if(t>3):
                t-=4
            if postos[t]==1 and dirpeca[j]!=1:
                break
            if postos[t]==-1 and dirpeca[j]!=0:
                break
            if j==3:
                lista.append(i)
    
    if (peca==1010 or peca==101)and len(lista)==2:
        lista.pop()
        


    if (len(lista)==1):
        roda(table,row,col,lista[0],1)
        lista_proximo.append([row+1,col])
        lista_proximo.append([row,col+1])
        lista_proximo.append([row,col-1])
        lista_proximo.append([row-1,col])
        bons[0]+=1
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



def place_piece(board:list,action:list ) ->list:#temos que fazer o copy normal nao podemos usar o deep
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
    while True:
        line= sys.stdin.readline().split()
        if line== "":
            break
        if not line:  # Check if line is empty (end of file)
            break
        table_lig.append([])
        for i in line:
            if i== "FC":
                table_lig[j].append([1000,0])
            elif i== "FB":
                table_lig[j].append([10,0])
            elif i== "FE":
                table_lig[j].append([1,0])
            elif i== "FD":
                table_lig[j].append([100,0])
            elif i== "BC":
                table_lig[j].append([1101,0])
            elif i== "BB":
                table_lig[j].append([111,0])
            elif i== "BE":
                table_lig[j].append([1011,0])
            elif i== "BD":
                table_lig[j].append([1110,0])
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

def mostra(table:list):
    texto=""
    for i in table:
        for j in i:
            if j[0]== 1000:
                texto+="FC\t"
            elif j[0]==10:
                texto+="FB\t"
            elif j[0]==1:
                texto+="FE\t"
            elif j[0]==100:
                texto+="FD\t"
            elif j[0]==1101:
                texto+="BC\t"
            elif j[0]==111:
                texto+="BB\t"
            elif j[0]==1011:
                texto+="BE\t"
            elif j[0]==1110:
                texto+="BD\t"
            elif j[0]==1001:
                texto+="VC\t"
            elif j[0]==110:
                texto+="VB\t"
            elif j[0]==11:
                texto+="VE\t"
            elif j[0]==1100:
                texto+="VD\t"
            elif j[0]==101:
                texto+="LH\t"
            elif j[0]==1010:
                texto+="LV\t"
        texto = texto[:-1]
        texto+="\n"
    return texto

                


def procura(table:list,node,pilha:list):
    # Iterar sobre a lista de listas e adicionar os nós ao grafo
    row=node[0]
    col=node[1]
    
    peca=table[row][col][0]
    direcoes=[quero_cima(table,row,col),quero_direita(table,row,col),quero_baixo(table,row,col),quero_esquerda(table,row,col)]
    # Adicionar conexões com os elementos adjacentes
    if (direcoes[0][0]==peca//1000==1):
        pilha.append((row-1,col))
    if (direcoes[1][0]==peca%1000//100==1):
        pilha.append((row,col+1))
    if (direcoes[2][0]==peca%100//10==1):
        pilha.append((row+1,col))
    if(direcoes[3][0]==peca%10==1):
        pilha.append((row,col-1))   


def dfs_iterativa(table, inicio, visitados):
    pilha = [inicio]
    
    while pilha:
        vertice = pilha.pop()
        if vertice not in visitados:
            visitados.add(vertice)
            procura(table,vertice,pilha)

def verifica_conexao_total(table):
    visitados = set()
    
    # Realiza a busca em profundidade iterativa a partir de qualquer nó
    dfs_iterativa(table,(0,0), visitados)
    # Verifica se todos os nós foram visitados
    return len(visitados) == len(table)**2



def inferencia1(state:list,bons:list):#isto em vez de board tem que se usar o pipestate
    tamanho=len(state)
    lista_proximo=[]
    for i in range(tamanho):
        hipostese(state,0,i,lista_proximo,bons)
        hipostese(state,tamanho-1,i,lista_proximo,bons)
        hipostese(state,i,0,lista_proximo,bons)
        hipostese(state,i,tamanho-1,lista_proximo,bons)
    return lista_proximo

def inferencia2(table:list ,lista_proximo:list,list_actions:list,bons:list):
    while(len(lista_proximo)!=0):
        ponto=lista_proximo.pop(0)
        hipostese_int(table, ponto[0],ponto[1],list_actions,lista_proximo,bons)

    

    """Retorna uma lista de ações que podem ser executadas a
    partir do estado passado como argumento."""
    # TODO
    pass

def inferencia3(table:list ,lista_proximo:list,list_actions:list,bons:list):
    for i in range(len(table)-1):
        for j in range(len(table)-1):
            hipostese_2(table,i,j,list_actions,lista_proximo,bons)

    

    """Retorna uma lista de ações que podem ser executadas a
    partir do estado passado como argumento."""
    # TODO
    pass


def actions(table:list,list_actions:list):
    for i in range(len(list_actions)-2):
        if (table[list_actions[i][1][0]][list_actions[i][1][1]][1]==1):
            list_actions.pop(i)
            pass
        elif(len(list_actions[i][0])==2):
            return list_actions[i]
    if len(list_actions)>0:
        return list_actions[0]  
    else:
        return [] 
    """Retorna uma lista de ações que podem ser executadas a
    partir do estado passado como argumento."""
    # TODO
    pass

def result(state: list, action:list):

    new_board= place_piece(state,action)
    return new_board
    """Retorna o estado resultante de executar a 'action' sobre
    'state' passado como argumento. A ação a executar deve ser uma
    das presentes na lista obtida pela execução de
    self.actions(state)."""
    # TODO
    pass


def goal_test(table:list):
    return verifica_conexao_total(table)
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

def expande(node:int,tree:dict,contador_nos:int,lista_nos:list):
    if(node==0):
        return
    table=lista_nos[node][0]
    action=lista_nos[node][1]
    new_table=result(table,action)
    lista_proximo=[]
    row=action[1][0]
    col=action[1][1]
    lista_proximo.append([row+1,col])
    lista_proximo.append([row,col+1])
    lista_proximo.append([row,col-1])
    lista_proximo.append([row-1,col])
    list_actions=[]
    bons=[lista_nos[node][2][0]+1]
    inferencia2(new_table,lista_proximo,list_actions,bons)
    lista_nos[node][0]=new_table
    tree[node]=[]
    if (bons[0]==len(tabel)**2):
        if (goal_test(new_table)):
            return new_table
        else:
            return
    else:
        list_action=actions(new_table,list_actions)
        if list_action!= []:
            for i in list_action[0]:
                contador_nos+=1
                add_children(node,new_table,[i,action[1]],tree,contador_nos,bons,lista_nos)


def add_children(node:int , table:list,action:list ,tree:dict,contador:int,bons:list,lista_nos:list):
    lista_nos.append([table,action,bons])
    tree[node].append(contador)


def dfs_iterative(root:int,tree:dict,contador_nos:int,lista_nos:list):
    stack = [root]
    visited = set()

    while stack:
        node = stack.pop(0)
        if node not in visited:
            expande(node,tree,contador_nos,lista_nos)
            #print(node)
            visited.add(node)
            # Adiciona os filhos do nó atual à pilha
            stack.extend(child for child in tree[node] if child not in visited)


if __name__ == "__main__":
    # TODO:
    tabel=parse_instance()
    tree ={}
    lista_nos=[]
    contador_nos=0
    bons=[0]# os bons esta mal feito em hiposteses 1 repeticao de pontas 
    lista_proximos=inferencia1(tabel,bons)
    list_actions=[]
    inferencia2(tabel,lista_proximos,list_actions,bons)
    #print(tabel)
    action=actions(tabel,list_actions)
    tree ={}
    lista_nos=[]
    contador_nos=0
    lista_nos.append([tabel,[],bons])
    tree[0]=[]
    if(len(action)>0):
        for i in action[0]:
            contador_nos+=1
            tree[0].append(contador_nos)
            lista_nos.append([tabel,[i,action[1]],bons])
    final=dfs_iterative(0,tree,contador_nos,lista_nos)


    



    # Ler o ficheiro do standard input,
    # Usar uma técnica de procura para resolver a instância,
    # Retirar a solução a partir do nó resultante,
    # Imprimir para o standard output no formato indicado.
    pass
