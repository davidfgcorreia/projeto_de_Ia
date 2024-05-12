# pipe.py: Template para implementação do projeto de Inteligência Artificial 2023/2024.
# Devem alterar as classes e funções neste ficheiro de acordo com as instruções do enunciado.
# Além das funções e classes sugeridas, podem acrescentar outras que considerem pertinentes.

# Grupo 00:
# 00000 Nome1
# 00000 Nome2
import sys
import copy
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


class Board:
    
    def __init__(self,tablel):
        self.tablel=tablel
        self.tamanho=len(self.tablel)
        self.lista_proximo=[]  
    """Representação interna de um tabuleiro de PipeMania."""

    def get_value(self, row: int, col: int) -> str:
            tamanho=len(self.table)
            if (row<0 or row>tamanho-1 or col<0 or col>tamanho-1):
                return 0
            if self.table[row][col]/10 == 11:
                return "FC"
            elif self.table[row][col]/10 == 12:
                return "FB"
            elif self.table[row][col]/10 == 13:
                return "FE"
            elif self.table[row][col]/10 == 14:
                return "FD"
            elif self.table[row][col]/10 == 31:
                return "BC"
            elif self.table[row][col]/10 == 32:
                return "BB"
            elif self.table[row][col]/10 == 33:
                return "BE"
            elif self.table[row][col]/10 == 34:
                return "BD"
            elif self.table[row][col]/10 == 21:
                return "VC"
            elif self.table[row][col]/10 == 22:
                return "VB"
            elif self.table[row][col]/10 == 23:
                return "VE"
            elif self.table[row][col]/10 == 24:
                return "VD"
            elif self.table[row][col]/10 == 41:
                return "LH"
            elif self.table[row][col]/10 == 42:
                return "LV"
            
            pass
    
    def get_value_num_l(self, row: int, col: int) -> tuple[int,int]:
        tamanho=len(self.tablel)
        if (row<0 or row>tamanho-1 or col<0 or col>tamanho-1):
            return 0
        return self.tablel[row][col]
    """Devolve o valor na respetiva posição do tabuleiro."""

    def table_len(self) -> int:
        return self.tamanho
    
    # TODO
    pass
    def quero_cima(self, row: int, col: int) -> int:
        ligacao= -1
        if not (row > self.tamanho | row-1 < 0 | col > self.tamanho | col<0):
            ligacao= self.tablel[row-1][col]
            return [ligacao[0]%100//10,ligacao[1]]
        return ligacao
        # TODO
        pass
    def quero_baixo(self, row: int, col: int) -> int:
        ligacao= -1
        if not (row+1 > self.tamanho | row < 0 | col > self.tamanho | col<0):
            ligacao= self.tablel[row+1][col]
            return [ligacao[0]//1000,ligacao[1]]
        return ligacao
        # TODO
        pass
    def quero_direita(self, row: int, col: int) -> int:
        ligacao= -1
        if not (row > self.tamanho | row < 0 | col+1 > self.tamanho | col<0):
            ligacao= self.tablel[row][col+1]
            return [ligacao[0]%10,ligacao[1]]
        return ligacao
        pass
    def quero_esquerda(self, row: int, col: int) -> int:
        ligacao= -1
        if not (row > self.tamanho | row < 0 | col > self.tamanho | col-1<0):
            ligacao= self.tablel[row][col-1]
            return [ligacao[0]%1000//100,ligacao[1]]
        return ligacao
        # TODO
        pass


    def roda(self, row: int , col: int , rotacao: int,estado:int ):
        peca=self.tablel[row][col][0]
        if rotacao==1:
            nova=peca%10*1000+ peca//1000*100+peca%1000//100*10+peca%100//10
        if rotacao==2:
            nova= peca//1000*10+ peca%1000//100+ peca%100//10*1000 +peca%10*100
        if rotacao==3:
            nova=peca//1000+ peca%1000//100*1000+peca%100//10*100+peca%10*10

        self.tablel[row][col]=[nova,estado]
    

    def hipostese(self,row:int,col:int):
        peca=self.tablel[row][col][0]
        dirpeca=[peca//1000,peca%1000//100,peca%100//10,peca%10]
        ligacao=dirpeca[0]+dirpeca[1]+dirpeca[2]+dirpeca[3]

        if ligacao==2:
            if (dirpeca[0]==dirpeca[2]|dirpeca[1]==dirpeca[3]):
                ligacao=4
                self.lista_proximo.append([row,col])
        if ligacao==3:
            if row==0:
                self.tablel[row][col]=[111,1]
                self.lista_proximo.append([row,col])
            elif row== self.tamanho:
                self.tablel[row][col]=[1101,1]
                self.lista_proximo.append([row,col])
            elif col==0:
                self.tablel[row][col]=[1110,1]
                self.lista_proximo.append([row,col])
            elif col==self.tamanho:
                self.tablel[row][col]=[1011,1]
                self.lista_proximo.append([row,col])
        elif ligacao==4:
            if row==0 or row == self.tamanho:
                self.tablel[row][col]=[101,1]
                self.lista_proximo.append([row,col])
            elif col==0 or col == self.tamanho:
                self.tablel[row][col]=[1010,1]
                self.lista_proximo.append([row,col])
        elif ligacao==2:
            if (row==0 and col==0):
                self.tablel[row][col]=[110,1]
                self.lista_proximo.append([row,col])
            if (row==0 and col==self.tamanho):
                self.tablel[row][col]=[11,1]
                self.lista_proximo.append([row,col])
            if (row==self.tamanho and col==0):
                self.tablel[row][col]=[1100,1]
                self.lista_proximo.append([row,col])
            if (row==self.tamanho and col==self.tamanho):
                self.tablel[row][col]=[1001,1]
                self.lista_proximo.append([row,col])
        
    def busca_tipos(self,row:int,col:int):
        ligacao=[[[-1,-1],-[-1,-1],[-1,-1],[-1,-1]],[False,False,False,False]]
        if not(row > self.tamanho | row-1 < 0 | col > self.tamanho | col<0):
            ligacao[0][0]= self.tablel[row-1][col]
            ligacao[1][0]=(str(ligacao[0][0][0]).count('1')==True)
        if not (row+1 > self.tamanho | row < 0 | col > self.tamanho | col<0):
            ligacao[0][1]= self.tablel[row+1][col][0]
            ligacao[1][1]=(str(ligacao[0][0][0]).count('1')==True)
        if not (row > self.tamanho | row < 0 | col+1 > self.tamanho | col<0):
            ligacao[0][2]= self.tablel[row][col+1]
            ligacao[1][2]=(str(ligacao[0][0][0]).count('1')==True)
        if not (row > self.tamanho | row < 0 | col > self.tamanho | col-1<0):
            ligacao[0][3]= self.tablel[row][col-1]
            ligacao[1][3]=(str(ligacao[0][0][0]).count('1')==True)
        return ligacao



    def hipostese_int(self,row:int,col:int, list_actions: list):
        pecat=self.tablel[row][col]
        if (peca[1]==1):
            return
        peca=pecat[0]
        dirpeca=[peca//1000,peca%1000//100,peca%100//10,peca%10]
        ligacao=dirpeca[0]+dirpeca[1]+dirpeca[2]+dirpeca[3]
        postos=[0,0,0,0]
        if ligacao==1:
            direcoesl=self.busca_tipos(self,row,col)
            direcoes=direcoesl[0]
            tipos=direcoesl[1]
        else:
            direcoes=[self.quero_cima(self,row,col),self.quero_direita(self,row,col),self.quero_baixo(self,row,col),self.quero_esquerda(self,row,col)]
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


        if (len(lista)==1):
            self.roda(self,row,col,lista[0],1)
            self.lista_proximo.append([row,col])
        else:
            list_actions.append([lista,[row,col]])

                

    def get_lista_proximo(self):
        return self.lista_proximo
                



    def ligacoes(self,row:int , col:int)->int :
        peca=self.tablel[row][col]
        direcoes=[self.quero_cima(self,row,col),self.quero_direita(self,row,col),self.quero_baixo(self,row,col),self.quero_esquerda(self,row,col)]
        dirpeca=[peca//1000,peca%1000//100,peca%100//10,peca%10]
        lig=0
        lig_total=0
        for i in range(4):
                if (direcoes[i]==1 & dirpeca[i]==1):
                    lig+=1
                if (dirpeca[i]==1):
                    lig_total+=1
        return lig/lig_total



    def place_piece(self, row: int, col: int, value: int) -> "Board":
            """Devolve um novo tabuleiro com o valor colocado na posição indicada."""
            new_table  = copy.deepcopy(self.tablel)
            new_board = Board(new_table)
            new_board.roda(new_board,row,col,value,1)

            return new_board









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

        return Board(Board,table_lig)

    # TODO: outros metodos da classe


class PipeMania(Problem):
    def __init__(self, board: Board):
        """O construtor especifica o estado inicial."""
        self.Board =Board
        # TODO
        pass

    def inferencia(self, state1: PipeManiaState,state:Board):#isto em vez de board tem que se usar o pipestate
        tamanho=self.Board.table_len(self.Board)
        for i in range(tamanho):
            state.hipostese(state,0,i)
            state.hipostese(state,tamanho,i)
            state.hipostese(state,i,0)
            state.hipostese(state,i,tamanho)
        lista_proximo= state.get_lista_proximo
        while(len(lista_proximo)!=0):
            ponto=lista_proximo.pop(0)
            state.hipostese_int(state, ponto[0],ponto[1],lista_proximo)

        

        """Retorna uma lista de ações que podem ser executadas a
        partir do estado passado como argumento."""
        # TODO
        pass
    

    def actions(self, state1: PipeManiaState,row:int,col:int,state:Board):
        lista_proximo=state.get_lista_proximo
        for i in range(len(lista_proximo)):
            if (state.get_value(lista_proximo[i][1][0],lista_proximo[i][1][1])[1]==1):
                lista_proximo.pop(i)
            if(len(lista_proximo[i][0])==2):
                return lista_proximo[i]
        return lista_proximo[0]   
        """Retorna uma lista de ações que podem ser executadas a
        partir do estado passado como argumento."""
        # TODO
        pass
    def result(self, state: PipeManiaState, action):
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
