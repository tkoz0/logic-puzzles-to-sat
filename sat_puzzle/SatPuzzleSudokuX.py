from . import SatPuzzleSudokuStandard

class SatPuzzleSudokuX(SatPuzzleSudokuStandard):
    '''
    Standard Sudoku also requiring the diagonals to contain each number once.
    '''
    def __init__(self, blockR: int, blockC: int, givens: list[list[int]]):
        '''
        blockR = number of rows in each sub block
        blockC = number of columns in each sub block
        givens = N x N grid of given numbers, 0 for no given (N = blockR*blockC)
        '''
        super().__init__(blockR,blockC,givens)
        N = blockR*blockC
        self.areas.append(list(range(0,N*N,N+1)))
        self.areas.append(list(range(N-1,N*N-1,N-1)))
