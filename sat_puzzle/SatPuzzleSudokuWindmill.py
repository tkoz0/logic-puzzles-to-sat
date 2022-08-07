from . import SatPuzzleSudokuOverlap

class SatPuzzleSudokuWindmill(SatPuzzleSudokuOverlap):
    '''
    Overlapped standard (size 9x9) Sudokus in the following arrangement:
     AXX
     XXXBXX
     XCXXXX
    DXXXXXX
    XXXEXX
    XXXXXX
       XXX
    Each letter is a sub block and ABCDE are the top left corners of the standard Sudokus.
    This class only supports 3x3 sub blocks.
    '''
    def __init__(self, givens: list[list[int]]):
        '''
        givens = 21x21 grid
        '''
        super().__init__(3,3,givens,[(0,3),(3,12),(6,6),(9,0),(12,9)])
