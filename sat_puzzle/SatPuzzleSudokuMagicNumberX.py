from . import SatPuzzleLatinSquareX

class SatPuzzleSudokuMagicNumberX(SatPuzzleLatinSquareX):
    '''
    Latin Square with thick lines between cells indicating they must sum to the
    given magic number.
    '''
    def __init__(self, givens: list[list[int]], magic: int, pairs: set[tuple[tuple[int,int],tuple[int,int]]]):
        '''
        givens = N x N grid of given values, 0 for no given value
        magic = magic number
        pairs = set of (r1,c1),(r2,c2) cell pairs that must sum to magic number
        '''
        N = len(givens)
        super().__init__(givens)
        self.magic = magic
        assert all(0 <= r1 < N and 0 <= c1 < N and 0 <= r2 < N and 0 <= c2 < N for (r1,c1),(r2,c2) in pairs)
        self.pairs = set(p for p in pairs)
    def toCnf(self) -> list[list[int]]:
        '''
        Add constraints for orthogonally adjacent cells similar to in
        Consecutive Sudoku where clauses are added for each pair that is not
        allowed in the 2 cells.
        '''
        result = super().toCnf()
        N = self.nums
        x = lambda r,c,n : 1 + (r*N+c)*N + (n-1) # get variable number
        not_magic_sum = [(a,b) for a in range(1,N+1) for b in range(1,N+1) if a != b and a+b != self.magic]
        for (r1,c1),(r2,c2) in self.pairs:
            for a,b in not_magic_sum: # at least 1 of these must not be set
                result.append([-x(r1,c1,a),-x(r2,c2,b)])
        return result
