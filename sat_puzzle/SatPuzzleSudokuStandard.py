from . import SatPuzzleLatinSquare

class SatPuzzleSudokuStandard(SatPuzzleLatinSquare):
    '''
    Standard Sudoku is a Latin Square with rectangular sub blocks.
    '''
    def __init__(self, blockR: int, blockC: int, givens: list[list[int]]):
        '''
        blockR = number of rows in each sub block
        blockC = number of columns in each sub block
        givens = N x N grid of given numbers, 0 for no given (N = blockR*blockC)
        '''
        assert blockR > 0 and blockC > 0
        N = blockR*blockC
        assert len(givens) == N
        super().__init__(givens)
        for r in range(blockC): # blocks
            for c in range(blockR):
                self.areas.append([(r*blockR+rr)*N+(c*blockC+cc) for rr in range(blockR) for cc in range(blockC)])
        self.blockR = blockR
        self.blockC = blockC
