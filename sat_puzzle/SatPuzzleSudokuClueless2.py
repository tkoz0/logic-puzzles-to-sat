from . import SatPuzzleSudokuCluelessBase

class SatPuzzleSudokuClueless2(SatPuzzleSudokuCluelessBase):
    '''
    The 10th grid is made of the center blocks of each sub puzzle.
    '''
    def __init__(self, givens: list[list[int]]):
        super().__init__(givens)
        indexes = [3,4,5,12,13,14,21,22,23]
        for i in indexes:
            self.areas.append([27*i+c for c in indexes]) # row
            self.areas.append([27*r+i for r in indexes]) # col
        # blocks are redundant since they are part of other sub puzzles
