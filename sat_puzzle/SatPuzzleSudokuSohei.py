from . import SatPuzzleSudokuOverlap

class SatPuzzleSudokuSohei(SatPuzzleSudokuOverlap):
    '''
    Overlapped standard (size 9x9) Sudokus in the following arrangement:
      AXX
      XXX
    BXXXCXX
    XXX XXX
    XXDXXXX
      XXX
      XXX
    Each letter is a sub block and ABCD are the top left corners of the standard Sudokus.
    This class only supports 3x3 sub blocks.
    '''
    def __init__(self, givens: list[list[int]]):
        '''
        givens = 21x21 grid
        '''
        super().__init__(3,3,givens,[(0,6),(6,0),(6,12),(12,6)])
