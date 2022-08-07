from . import SatPuzzleSudokuCluelessBase

class SatPuzzleSudokuClueless1(SatPuzzleSudokuCluelessBase):
    '''
    The 10th grid is made of the centers of the 81 sub blocks.
    '''
    def __init__(self, givens: list[list[int]]):
        super().__init__(givens)
        for r in range(1,27,3):
            self.areas.append(list(range(27*r+1,27*r+27,3)))
        for c in range(1,27,3):
            self.areas.append(list(range(27*1+c,27*27+c,27*3)))
        for r in range(1,27,9):
            for c in range(1,27,9):
                self.areas.append([27*(r+rr)+(c+cc) for rr in range(0,9,3) for cc in range(0,9,3)])
