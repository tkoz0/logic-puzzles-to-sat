from . import SatPuzzleSudokuGeneral

class SatPuzzleLatinSquare(SatPuzzleSudokuGeneral):
    '''
    An N x N grid requiring 1,2,...,N in each row/column. Similar to normal
    Sudoku but without the sub blocks.
    Square grid of side length N
    - each row/col must contain 1,2,..,N
    '''
    def __init__(self, givens: list[list[int]]):
        '''
        givens = N x N grid of given numbers, 0 for no value given
        '''
        N = len(givens)
        assert N > 0
        assert len(givens) == N and all(len(row) == N for row in givens) and all(0 <= n <= N for n in sum(givens,[]))
        areas = []
        for r in range(N): # rows
            areas.append(list(range(r*N,r*N+N)))
        for c in range(N): # cols
            areas.append(list(range(c,N*N,N)))
        super().__init__(N*N,N,areas,sum(givens,[]))
    def toSol(self, satSol: list[int]) -> list[list[int]]: # change structure to square
        sol = super().toSol(satSol)
        return [sol[i:i+self.nums] for i in range(0,self.cells,self.nums)]
