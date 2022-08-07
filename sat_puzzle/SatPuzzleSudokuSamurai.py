from . import SatPuzzleSudokuOverlap

class SatPuzzleSudokuSamurai(SatPuzzleSudokuOverlap):
    '''
    Overlapped standard (size 9x9) Sudokus in the following arrangement:
    AXX BXX
    XXX XXX
    XXCXXXX
      XXX
    DXXXEXX
    XXX XXX
    XXX XXX
    Each letter is a sub block and ABCDE are the top left corners of the standard Sudokus.
    This class only supports 3x3 sub blocks.
    '''
    def __init__(self, givens: list[list[int]]):
        '''
        givens = 21x21 grid
        '''
        super().__init__(3,3,givens,[(0,0),(0,12),(6,6),(12,0),(12,12)])
