from . import SatPuzzleSudokuOverlap

class SatPuzzleSudokuShogun(SatPuzzleSudokuOverlap):
    '''
    Overlapped standard (size 9x9) Sudokus in the following arrangement:
    AXX BXX CXX DXX
    XXX XXX XXX XXX
    XXEXXXFXXXGXXXX
      XXX XXX XXX
    HXXXIXXXJXXXKXX
    XXX XXX XXX XXX
    XXX XXX XXX XXX
    Each letter is a sub block and ABCDEFGHIJK are the top left corners of the standard Sudokus.
    This class only supports 3x3 sub blocks.
    '''
    def __init__(self, givens: list[list[int]]):
        '''
        givens = 21x45 grid
        '''
        super().__init__(3,3,givens,[(0,0),(0,12),(0,24),(0,36),(6,6),(6,18),(6,30),(12,0),(12,12),(12,24),(12,36)])
