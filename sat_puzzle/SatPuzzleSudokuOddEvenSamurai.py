from . import SatPuzzleSudokuSamurai

class SatPuzzleSudokuOddEvenSamurai(SatPuzzleSudokuSamurai):
    '''
    Odd Even Sudoku in the Samurai overlapping layout.
    '''
    def __init__(self, givens: list[list[int]], odds: list[list[bool]]):
        '''
        givens = 15x15 grid
        odds = 15x15 grid
        '''
        super().__init__(givens)
        assert len(odds) == 21 and all(len(row) == 21 for row in odds)
        self.odds = [row[:] for row in odds]
    def toCnf(self) -> list[list[int]]:
        '''
        Handle these constraints with a more restrictive clause of possible
        values which makes the all value clauses redundant.
        '''
        result = super().toCnf()
        x = lambda r,c,n : 1 + (r*21+c)*9 + (n-1)
        unused_blocks = set([(0,3),(1,3),(3,0),(3,1),(3,5),(3,6),(5,3),(6,3)])
        for r,row in enumerate(self.odds): # constrain number parity in used blocks
            for c,odd in enumerate(row):
                if (r//self.blockR,c//self.blockC) in unused_blocks:
                    continue
                elif odd: # cell must be odd
                    result.append([x(r,c,n) for n in range(1,10,2)])
                else: # cell must be even
                    result.append([x(r,c,n) for n in range(2,10,2)])
        return result
