from . import SatPuzzleSudokuOverlap

class SatPuzzleSudokuFlower(SatPuzzleSudokuOverlap):
    '''
    Overlapped standard (size 9x9) Sudokus in the following arrangement:
         AXX
        BXCXX
        XDXXX
        XXXXX
         XXX
    Each letter is a sub block and ABCD are the top left corners of the standard Sudokus.
    This class only supports 3x3 sub blocks.
    '''
    def __init__(self, givens: list[list[int]]):
        '''
        givens = 15x15 grid
        '''
        super().__init__(3,3,givens,[(0,3),(3,0),(3,3),(3,6),(6,3)])
