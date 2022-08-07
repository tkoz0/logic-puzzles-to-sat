from . import SatPuzzleSudokuOverlap

class SatPuzzleSudokuCluelessBase(SatPuzzleSudokuOverlap):
    '''
    Shared part of the Clueless Sudoku types (9 non overlapping standard grids)
    AXXBXXCXX
    XXXXXXXXX
    XXXXXXXXX
    DXXEXXFXX
    XXXXXXXXX
    XXXXXXXXX
    GXXHXXIXX
    XXXXXXXXX
    XXXXXXXXX
    Each letter is a sub block and ABCDEFGHI are the top left corners of the standard Sudokus.
    This class only supports 3x3 sub blocks.
    '''
    def __init__(self, givens: list[list[int]]):
        '''
        givens = 27x27 grid
        '''
        super().__init__(3,3,givens,[(0,0),(0,9),(0,18),(9,0),(9,9),(9,18),(18,0),(18,9),(18,18)])
