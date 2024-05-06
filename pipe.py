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
    
    def __init__(self, table,tablel):
        self.table = table
        self.tablel=tablel

    
        
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
        tamanho=len(self.table)
        if (row<0 or row>tamanho-1 or col<0 or col>tamanho-1):
            return 0
        return self.table[row][col]
    
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
        return len(self.table)
    
    # TODO
    pass

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
                    table[j].append(110)
                    table_lig[j].append(1000)
                elif i== "FB":
                    table[j].append(120)
                    table_lig[j].append(100)
                elif i== "FE":
                    table[j].append(130)
                    table_lig[j].append(10)
                elif i== "FD":
                    table[j].append(140)
                    table_lig[j].append(1)
                elif i== "BC":
                    table[j].append(310)
                    table_lig[j].append(1101)
                elif i== "BB":
                    table[j].append(320)
                    table_lig[j].append(1110)
                elif i== "BE":
                    table[j].append(330)
                    table_lig[j].append(111)
                elif i== "BD":
                    table[j].append(340)
                    table_lig[j].append(1011)
                elif i== "VC":
                    table[j].append(210)
                    table_lig[j].append(1001)
                elif i== "VB":
                    table[j].append(220)
                    table_lig[j].append(110)
                elif i== "VE":
                    table[j].append(230)
                    table_lig[j].append(11)
                elif i== "VD":
                    table[j].append(240)
                    table_lig[j].append(1100)
                elif i== "LH":
                    table[j].append(410)
                    table_lig[j].append(101)
                elif i== "LV":
                    table[j].append(420)
                    table_lig[j].append(1010)
            j=j+1

        return Board(Board,table,table_lig)

    # TODO: outros metodos da classe


class PipeMania(Problem):
    def __init__(self, board: Board):
        """O construtor especifica o estado inicial."""
        self.Board =Board
        # TODO
        pass

    def inferencia(self, state: PipeManiaState):
        tamanho=range(len(self.Board.table_len(self.Board)))
        for i in range(tamanho) :
            for j in range(tamanho):
                if (i== 0 or i==tamanho-1 or j==0 or j==tamanho-1):
                    lateral=1
                pecat=PipeMania.get_value_num(PipeMania,i,j)
                peca=pecat/100
                if pecat%100 == 0:
                    vertical= self.Board.adjacent_vertical_values_num(self.Board,i,j)
                    horizontal= self.Board.adjacent_horizontal_values_num(self.Board,i,j)
                    top=vertical[0]
                    bot=vertical[1]
                    dir=horizontal[0]
                    esq=horizontal[1]
                    if  peca==1:
                        pass
                    elif  peca==2:
                        if i==0:
                                if j==0:
                                    self.Board.change_value_num(self.Board,i,j,221)
                                elif j==tamanho:
                                    self.Board.change_value_num(self.Board,i,j,231)
                        elif i==tamanho:
                                if j==0:
                                    self.Board.change_value_num(self.Board,i,j,241)
                                elif j==tamanho:
                                    self.Board.change_value_num(self.Board,i,j,211)


                        pass
                    elif  peca==3:
                            if i==0:
                                self.Board.change_value_num(self.Board,i,j,331)
                            elif i==tamanho:
                                self.Board.change_value_num(self.Board,i,j,311)
                            elif j==tamanho:
                                self.Board.change_value_num(self.Board,i,j,341)
                            elif j==0:
                                self.Board.change_value_num(self.Board,i,j,311)
                    elif  peca==4:
                            if i==0:
                                self.Board.change_value_num(self.Board,i,j,411)
                            elif i==tamanho:
                                self.Board.change_value_num(self.Board,i,j,411)
                            elif j==tamanho:
                                self.Board.change_value_num(self.Board,i,j,421)
                            elif j==0:
                                self.Board.change_value_num(self.Board,i,j,421)

                break
            break

                
                

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
