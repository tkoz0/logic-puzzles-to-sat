from . import SatPuzzleSudokuStandard

class SatPuzzleSudokuOddEven(SatPuzzleSudokuStandard):
    '''
    Sudoku variant that marks all odd numbers with circles and leaves all even
    numbers unmarked.
    '''
    def __init__(self, blockR: int, blockC: int, givens: list[list[int]], odds: list[list[bool]]):
        '''
        blockR = rows per sub block
        blockC = cols per sub block
        givens = N x N grid (N = blockR*blockC)
        odds = boolean array, True for numbers marked with circles
        '''
        super().__init__(blockR,blockC,givens)
        N = len(givens)
        assert len(odds) == N and all(len(row) == N for row in odds)
        self.odds = [row[:] for row in odds]
    def toCnf(self) -> list[list[int]]:
        '''
        Add constraints for odd and even cells. These are expressed as negations
        of assigning the opposite parity to cells.
        '''
        result = super().toCnf()
        N = self.nums
        x = lambda r,c,n : 1 + (r*N+c)*N + (n-1) # get variable number
        for r,row in enumerate(self.odds):
            for c,odd in enumerate(row):
                if odd:
                    for n in range(2,N+1,2): # cannot be even
                        result.append([-x(r,c,n)])
                else:
                    for n in range(1,N+1,2): # cannot be odd
                        result.append([-x(r,c,n)])
        return result
