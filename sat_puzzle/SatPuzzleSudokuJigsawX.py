from . import SatPuzzleSudokuJigsaw

class SatPuzzleSudokuJigsawX(SatPuzzleSudokuJigsaw):
    '''
    Jigsaw Sudoku with main diagonals.
    '''
    def __init__(self, givens: list[list[int]], areas: list[list[int]]):
        '''
        givens = N x N grid of given numbers, 0 for no given
        areas = N x N grid of area assigned to each number (each area is a unique integer)
        '''
        super().__init__(givens,areas)
        N = len(givens)
        self.areas.append(list(range(0,N*N,N+1)))
        self.areas.append(list(range(N-1,N*N-1,N-1)))
