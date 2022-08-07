from . import SatPuzzleSudokuOverlap

class SatPuzzleSudokuSumo(SatPuzzleSudokuOverlap):
    '''
    Overlapped standard (size 9x9) Sudokus in the following arrangement:
    AXX BXX CXX
    XXX XXX XXX
    XXDXXXEXXXX
      XXX XXX
    FXXXGXXXHXX
    XXX XXX XXX
    XXIXXXJXXXX
      XXX XXX
    KXXXLXXXMXX
    XXX XXX XXX
    XXX XXX XXX
    Each letter is a sub block and ABCDEFGHIJKLM are the top left corners of the standard Sudokus.
    This class only supports 3x3 sub blocks.
    '''
    def __init__(self, givens: list[list[int]]):
        '''
        givens = 33x33 grid
        '''
        super().__init__(3,3,givens,[(0,0),(0,12),(0,24),(6,6),(6,18),(12,0),(12,12),(12,24),(18,6),(18,18),(24,0),(24,12),(24,24)])
