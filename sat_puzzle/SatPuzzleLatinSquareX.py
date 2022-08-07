from . import SatPuzzleLatinSquare

class SatPuzzleLatinSquareX(SatPuzzleLatinSquare):
    '''
    Latin Square also requiring the diagonals to contain each number once.
    '''
    def __init__(self, givens: list[list[int]]):
        '''
        givens = N x N grid of given numbers, 0 for no value given
        '''
        N = len(givens)
        super().__init__(givens)
        self.areas.append(list(range(0,N*N,N+1)))
        self.areas.append(list(range(N-1,N*N-1,N-1)))
