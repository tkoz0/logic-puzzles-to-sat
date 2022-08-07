from . import SatPuzzleSudokuOverlap

class SatPuzzleSudokuButterfly(SatPuzzleSudokuOverlap):
    '''
    Overlapped standard (size 9x9) Sudokus in the following arrangement:
        ABXX
        CDXX
        XXXX
        XXXX
    Each letter is a sub block and ABCD ore the top left corners of the standard Sudokus.
    This class only supports 3x3 sub blocks.
    '''
    def __init__(self, givens: list[list[int]]):
        '''
        givens = 12x12 grid
        '''
        super().__init__(3,3,givens,[(0,0),(0,3),(3,0),(3,3)])
