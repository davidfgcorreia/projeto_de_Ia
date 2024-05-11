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

    def place_piece(self, row: int, col: int, value: int) -> "PipeManiaState":
        """Devolve um novo estado com o valor colocado na posição indicada."""
        return PipeManiaState(self.board.place_piece(row, col, value))
    
    def board_is_correct(self):
        """Devolve True se o tabuleiro estiver correto."""

        return self.board.board_is_correct()


class Board:
    
    def __init__(self, table, correct_table):
        self.table = table
        self.correct_table = correct_table
        self.tamanho = len(self.table)
        self.correct_pieces = 0

    def get_value(self, row: int, col: int) -> str:
        """Devolve o valor na respetiva posição do tabuleiro."""
        return Board.decode(Board.get_value_num(self, row, col))
    
    def get_value_num(self, row: int, col: int) -> int:
        """Devolve o valor na respetiva posição do tabuleiro."""
        tamanho=len(self.table)
        if (row<0 or row>tamanho-1 or col<0 or col>tamanho-1):
            return -1
        return self.table[row][col]
    
    def get_value_correct(self, row: int, col: int) -> int:
        """Devolve se a peça está na posição correcta no tabuleiro."""
        tamanho=len(self.table)
        if (row<0 or row>tamanho-1 or col<0 or col>tamanho-1):
            return 1
        return self.correct_table[row][col]

    def adjacent_top_value(self, row: int, col: int) -> int:
        """Devolve o valor imediatamente acima."""
        top_value = -1
        if not (row > self.tamanho | row <= 0 | col > self.tamanho | col < 0):
            top_value = self.table[row-1][col]
            return top_value%100//10
        return top_value
    
    def adjacent_top_correct_value(self, row: int, col: int) -> int:
        """Devolve se o valor imediatamente acima está na posição certa."""
        if not (row > self.tamanho | row <= 0 | col > self.tamanho | col < 0):
            return self.correct_table[row-1][col]
        return -1

    def adjacent_down_value(self, row: int, col: int) -> int:
        """Devolve o valor imediatamente abaixo."""
        down_value = -1
        if not (row > self.tamanho - 1 | row < 0 | col > self.tamanho | col < 0):
            down_value = self.table[row+1][col]
            return down_value//1000
        return down_value
    
    def adjacent_down_correct_value(self, row: int, col: int) -> int:
        """Devolve se o valor imediatamente abaixo está na posição certa."""
        if not (row > self.tamanho | row <= 0 | col > self.tamanho | col < 0):
            return self.correct_table[row+1][col]
        return -1

    def adjacent_left_value(self, row: int, col: int) -> int:
        """Devolve o valor imediatamente à esquerda."""
        left_value = -1
        if not (row > self.tamanho | row < 0 | col > self.tamanho | col < 1):
            left_value = self.table[row][col-1]
            return left_value%1000//100
        return left_value
    
    def adjacent_left_correct_value(self, row: int, col: int) -> int:
        """Devolve se o valor imediatamente à esquerda está na posição correta."""
        if not (row > self.tamanho | row <= 0 | col > self.tamanho | col < 0):
            return self.correct_table[row][col-1]
        return -1

    def adjacent_right_value(self, row: int, col: int) -> int:
        """Devolve o valor imediatamente à direita."""
        right_value = -1
        if not (row > self.tamanho | row < 0 | col > self.tamanho - 1 | col < 0):
            right_value = self.table[row][col+1]
            return right_value%10
        return right_value
    
    def adjacent_right_correct_value(self, row: int, col: int) -> int:
        """Devolve se o valor imediatamente à direita está correto."""
        if not (row > self.tamanho | row <= 0 | col > self.tamanho | col < 0):
            return self.correct_table[row][col+1]
        return -1
    
    def piece_is_correct(self) -> int:
        """Devolve se a peça está na posição correta."""
        total_pieces = self.tamanho * self.tamanho
        return self.correct_pieces == total_pieces
    
    def board_is_correct(self) -> int:
        """Devolve se o número de peças na posição correta é igual ao número das peças."""
        total_pieces = self.tamanho * self.tamanho
        return self.correct_pieces == total_pieces
    
    def place_piece(self, row: int, col: int, value: int) -> "Board":
        """Devolve um novo tabuleiro com o valor colocado na posição indicada."""
        new_table = [[value if (i == row and j == col) else self.table[i][j] for j in range(self.tamanho)]
                      for i in range(self.tamanho)]
        
        new_correct_table = [[1 if (i == row and j == col) else self.correct_table[i][j] for j in range(self.tamanho)]
                             for i in range(self.tamanho)]

        new_board = Board(new_table, new_correct_table)

        return new_board

    def rotate(self, row: int , col: int , rotacao: int):
        """Devolve a peça rodada."""
        peca = self.table[row][col]

        if rotacao == 1:
            nova = peca%10*1000+ peca//1000*100+peca%1000//100*10+peca%100//10
        if rotacao == 2:
            nova = peca//1000*10+ peca%1000//100+ peca%100//10*1000 +peca%10*100
        if rotacao == 3:
            nova = peca//1000+ peca%1000//100*1000+peca%100//10*100+peca%10*10

        return nova
    
    def roda(self, row: int , col: int , rotacao: int,estado:int ):
        peca=self.tablel[row][col]
        if rotacao == 1:
            nova = peca%10*1000+ peca//1000*100+peca%1000//100*10+peca%100//10
        if rotacao == 2:
            nova = peca//1000*10+ peca%1000//100+ peca%100//10*1000 +peca%10*100
        if rotacao == 3:
            nova = peca//1000+ peca%1000//100*1000+peca%100//10*100+peca%10*10

        self.tablel[row][col] = [nova]
    

    def hipostese(self,row:int,col:int):
        peca=self.tablel[row][col][0]
        dirpeca=[peca//1000,peca%1000//100,peca%100//10,peca%10]
        ligacao=dirpeca[0]+dirpeca[1]+dirpeca[2]+dirpeca[3]

        if ligacao==2:
            if (dirpeca[0]==dirpeca[2]|dirpeca[1]==dirpeca[3]):
                ligacao=4
        if ligacao==3:
            if row==0:
                self.tablel[row][col]=[111,1]
            elif row== self.tamanho:
                self.tablel[row][col]=[1101,1]
            elif col==0:
                self.tablel[row][col]=[1110,1]
            elif col==self.tamanho:
                self.tablel[row][col]=[1011,1]
        elif ligacao==4:
            if row==0 or row == self.tamanho:
                self.tablel[row][col]=[101,1]
            elif col==0 or col == self.tamanho:
                self.tablel[row][col]=[1010,1]
        elif ligacao==2:
            if (row==0 and col==0):
                self.tablel[row][col]=[110,1]
            if (row==0 and col==self.tamanho):
                self.tablel[row][col]=[11,1]
            if (row==self.tamanho and col==0):
                self.tablel[row][col]=[1100,1]
            if (row==self.tamanho and col==self.tamanho):
                self.tablel[row][col]=[1001,1]
        
    def busca_tipos(self,row:int,col:int):
        ligacao=[[-1,-1,-1,-1],[0,0,0,0]]
        if not(row > self.tamanho | row-1 < 0 | col > self.tamanho | col<0):
            ligacao[0][0]= self.tablel[row-1][col]
            ligacao[1][0]=(str(ligacao[0][0][0]).count('1')==1)
        if not (row+1 > self.tamanho | row < 0 | col > self.tamanho | col<0):
            ligacao[0][1]= self.tablel[row+1][col][0]
            ligacao[1][1]=(str(ligacao[0][0][0]).count('1')==1)
        if not (row > self.tamanho | row < 0 | col+1 > self.tamanho | col<0):
            ligacao[0][2]= self.tablel[row][col+1]
            ligacao[1][2]=(str(ligacao[0][0][0]).count('1')==1)
        if not (row > self.tamanho | row < 0 | col > self.tamanho | col-1<0):
            ligacao[0][3]= self.tablel[row][col-1]
            ligacao[1][3]=(str(ligacao[0][0][0]).count('1')==1)
        return ligacao



    def hipostese_int(self,row:int,col:int):
        peca=self.tablel[row][col]
        if (peca[1]==1):
            return
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
            elif(direcoes[i]==-1):
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


            
        contador=0
        for i in postos:
            if (i==1):
                contador+=1
        
        if (contador==ligacao):
            self.roda(self,row,col,q,1)
        else:
            self.roda(self,row,col,q,0)


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


    def encode(piece:str) -> int :
        """Devolve o valor numérico associado à peça."""
        if piece == "FC":
            return 1000
        elif piece == "FB":
            return 100
        elif piece == "FE":
            return 10
        elif piece == "FD":
            return 1
        elif piece == "BC":
            return 1101
        elif piece == "BB":
            return 1110
        elif piece == "BE":
            return 111
        elif piece == "BD":
            return 1011
        elif piece == "VC":
            return 1001
        elif piece == "VB":
            return 110
        elif piece == "VE":
            return 11
        elif piece == "VD":
            return 1100
        elif piece == "LH":
            return 101
        elif piece == "LV":
            return 1010


    def decode(piece:int) -> str :
        """Devolve a string associada à peça."""
        if piece == 1000:
            return "FC"
        elif piece == 100:
            return "FB"
        elif piece == 10:
            return "FE"
        elif piece == 1:
            return "FD"
        elif piece == 1101:
            return "BC"
        elif piece == 1110:
            return "BB"
        elif piece == 111:
            return "BE"
        elif piece == 1011:
            return "BD"
        elif piece == 1001:
            return "VC"
        elif piece == 110:
            return "VB"
        elif piece == 11:
            return "VE"
        elif piece == 1100:
            return "VD"
        elif piece == 101:
            return "LH"
        elif piece == 1010:
            return "LV"


    @staticmethod
    def parse_instance():
        table = []
        correct_table = []
        while 1:
            line = sys.stdin.readline().split()
            if line == []:
                break
            row = []
            correct_row = []
            for i in line:
                piece = Board.encode(i)
                row.append(piece)
                correct_row.append(0)
            table.append(row)
            correct_table.append(correct_row)

        return Board(table, correct_table)

    # TODO: outros metodos da classe


class PipeMania(Problem):
    def __init__(self, board: Board):
        """O construtor especifica o estado inicial."""
        initial_state = PipeManiaState(board)
        super().__init__(initial_state)
    
    def actions(self, state: PipeManiaState, row: int, col: int):
        """Retorna uma lista de ações que podem ser executadas a
        partir do estado passado como argumento."""
        actions_list = []

        if state.board_is_correct():
            return actions_list
        
        actions_list.append(board.table[row][col])
        actions_list.append(board.rotate(self, row, col, 1))
        actions_list.append(board.rotate(self, row, col, 2))
        actions_list.append(board.rotate(self, row, col, 3))

        return actions_list


    def result(self, state: PipeManiaState, action) -> PipeManiaState:
        """Retorna o estado resultante de executar a 'action' sobre
        'state' passado como argumento. A ação a executar deve ser uma
        das presentes na lista obtida pela execução de
        self.actions(state)."""
        (row, col, value) = action
        return state.place_piece(row, col, value)

    def goal_test(self, state: PipeManiaState) -> bool:
        """Retorna True se e só se o estado passado como argumento é
        um estado objetivo. Deve verificar se todas as posições do tabuleiro
        estão preenchidas de acordo com as regras do problema."""
        return state.board_is_correct() == 0

    def h(self, node: Node):
        """Função heuristica utilizada para a procura A*."""
        # TODO
        pass

    # TODO: outros metodos da classe


if __name__ == "__main__":
    # Ler o ficheiro do standard input,
    # Usar uma técnica de procura para resolver a instância,
    # Retirar a solução a partir do nó resultante,
    # Imprimir para o standard output no formato indicado.
    board = Board.parse_instance()
    pipeMania = PipeMania(board)
    goal_node = breadth_first_tree_search(pipeMania)
    print(goal_node.state.board)