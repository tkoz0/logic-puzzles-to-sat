from . import SatPuzzleLatinSquare

class SatPuzzleSudokuJigsaw(SatPuzzleLatinSquare):
    '''
    Sudoku with irregularly shaped areas instead of rectangles.
    '''
    def __init__(self, givens: list[list[int]], areas: list[list[int]]):
        '''
        givens = N x N grid of given numbers, 0 for no given
        areas = N x N grid of area assigned to each number (each area is a unique integer)
        '''
        N = len(givens)
        assert N > 0
        assert len(areas) == N
        assert all(len(row) == N for row in areas)
        super().__init__(givens)
        for symb in set(sum(areas,[])): # add areas
            self.areas.append([i for i,a in enumerate(sum(areas,[])) if a == symb])
