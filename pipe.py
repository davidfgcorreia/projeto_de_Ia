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


class Board:
    
    def __init__(self,tablel):
        self.tablel=tablel
        self.tamanho=len(self.tablel)

    
        
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
    
    def get_value_num(self, row: int, col: int) -> int:
        tamanho=len(self.table)
        if (row<0 or row>tamanho-1 or col<0 or col>tamanho-1):
            return 0
        return self.table[row][col]
    
    def get_value_num_l(self, row: int, col: int) -> int:
        tamanho=len(self.tablel)
        if (row<0 or row>tamanho-1 or col<0 or col>tamanho-1):
            return 0
        return self.tablel[row][col]
    
    def change_value_num(self, row: int, col: int,peca: int):
        tamanho=len(self.table)
        if (row<0 or row>tamanho-1 or col<0 or col>tamanho-1):
            return 0
        self.table[row][col]=peca

    """Devolve o valor na respetiva posição do tabuleiro."""
    # TODO
    pass

    def adjacent_vertical_values(self, row: int, col: int) -> tuple[str, str]:
        return (self.get_value(self,row-1,col),self.get_value(self,row+1,col))

        """Devolve os valores imediatamente acima e abaixo,
        respectivamente."""
        # TODO
        pass

    def adjacent_horizontal_values(self, row: int, col: int) -> tuple[str, str]:
        return (self.get_value(self,row,col-1),self.get_value(self,row,col+1))
        """Devolve os valores imediatamente à esquerda e à direita,
        respectivamente."""
        # TODO
        pass
    
    def adjacent_vertical_values_num(self, row: int, col: int) -> tuple[tuple[int, int],tuple[int,int]]:
        return ((self.get_value_num(self,row-1,col),self.get_value_num_l(self,row-1,col)),(self.get_value_num(self,row+1,col),self.get_value_num_l(self,row+1,col)))

        """Devolve os valores imediatamente acima e abaixo,
        respectivamente."""
        # TODO
        pass

    def adjacent_horizontal_values_num(self, row: int, col: int) -> tuple[tuple[int, int],tuple[int,int]]:
        return ((self.get_value_num(self,row,col-1),self.get_value_num_l(self,row,col-1)),(self.get_value_num(self,row,col+1),self.get_value_num_l(self,row,col+1)))
        """Devolve os valores imediatamente à esquerda e à direita,
        respectivamente."""
        # TODO
        pass
    


    def table_len(self) -> int:
        return self.tamanho
    
    # TODO
    pass
    def quero_cima(self, row: int, col: int) -> int:
        ligacao= -1
        if not (row > self.tamanho | row-1 < 0 | col > self.tamanho | col<0):
            ligacao= self.tablel[row-1][col]
            return ligacao%100//10
        return ligacao
        # TODO
        pass
    def quero_baixo(self, row: int, col: int) -> int:
        ligacao= -1
        if not (row+1 > self.tamanho | row < 0 | col > self.tamanho | col<0):
            ligacao= self.tablel[row+1][col]
            return ligacao//1000
        return ligacao
        # TODO
        pass
    def quero_direita(self, row: int, col: int) -> int:
        ligacao= -1
        if not (row > self.tamanho | row < 0 | col+1 > self.tamanho | col<0):
            ligacao= self.tablel[row][col+1]
            return ligacao%10
        return ligacao
        pass
    def quero_esquerda(self, row: int, col: int) -> int:
        ligacao= -1
        if not (row > self.tamanho | row < 0 | col > self.tamanho | col-1<0):
            ligacao= self.tablel[row][col-1]
            return ligacao%1000//100
        return ligacao
        # TODO
        pass


    def roda(self, row: int , col: int , rotacao: int ):
        peca=self.tablel[row][col]
        if rotacao==1:
            nova=peca%10*1000+ peca//1000*100+peca%1000//100*10+peca%100//10
        if rotacao==2:
            nova= peca//1000*10+ peca%1000//100+ peca%100//10*1000 +peca%10*100
        if rotacao==3:
            nova=peca//1000+ peca%1000//100*1000+peca%100//10*100+peca%10*10

        self.tablel[row][col]=nova

    def hipostese(self,row:int,col:int):
        peca=self.tablel[row][col]
        direcoes=[self.quero_cima(self,row,col),self.quero_direita(self,row,col),self.quero_baixo(self,row,col),self.quero_esquerda(self,row,col)]
        dirpeca=[peca//1000,peca%1000//100,peca%100//10,peca%10]
        mal=1
        while(mal==1):
            for i in range(4):
                if (direcoes[i]==-1 & dirpeca[i]==1):
                    self.roda(self,row,col,1)
                    peca=self.tablel[row][col]
                else:
                    mal=0
                    break

        
    def ligacoes(self,row:int , col:int)->int :
        peca=self.tablel[row][col]
        direcoes=[self.quero_cima(self,row,col),self.quero_direita(self,row,col),self.quero_baixo(self,row,col),self.quero_esquerda(self,row,col)]
        dirpeca=[peca//1000,peca%1000//100,peca%100//10,peca%10]
        lig=0
        for i in range(4):
                if (direcoes[i]==1 & dirpeca[i]==1):
                    lig+=1
        return lig








    @staticmethod
    def parse_instance():
        table = []
        table_lig=[]
        j=0
        while 1:
            line= sys.stdin.readline().split()
            if line== "":
                break
            table.append([])
            for i in line:
                if i== "FC":
                    table_lig[j].append(1000)
                elif i== "FB":
                    table_lig[j].append(100)
                elif i== "FE":
                    table_lig[j].append(10)
                elif i== "FD":
                    table_lig[j].append(1)
                elif i== "BC":
                    table_lig[j].append(1101)
                elif i== "BB":
                    table_lig[j].append(1110)
                elif i== "BE":
                    table_lig[j].append(111)
                elif i== "BD":
                    table_lig[j].append(1011)
                elif i== "VC":
                    table_lig[j].append(1001)
                elif i== "VB":
                    table_lig[j].append(110)
                elif i== "VE":
                    table_lig[j].append(11)
                elif i== "VD":
                    table_lig[j].append(1100)
                elif i== "LH":
                    table_lig[j].append(101)
                elif i== "LV":
                    table_lig[j].append(1010)
            j=j+1

        return Board(Board,table_lig)

    # TODO: outros metodos da classe


class PipeMania(Problem):
    def __init__(self, board: Board):
        """O construtor especifica o estado inicial."""
        self.Board =Board
        # TODO
        pass

    def inferencia(self, state: PipeManiaState):
        tamanho=range(len(self.Board.table_len(self.Board)))
            #cantos
        for i in range(tamanho):
            self.Board.hipostese(self.Board,0,i)
            self.Board.hipostese(self.Board,tamanho,i)
            self.Board.hipostese(self.Board,i,0)
            self.Board.hipostese(self.Board,i,tamanho)

        """Retorna uma lista de ações que podem ser executadas a
        partir do estado passado como argumento."""
        # TODO
        pass
    

    def actions(self, state: PipeManiaState):
        list_actions=[]
        
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
