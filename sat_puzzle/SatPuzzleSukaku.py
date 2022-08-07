from . import SatPuzzleSudokuStandard

class SatPuzzleSukaku(SatPuzzleSudokuStandard):
    '''
    Standard Sudoku with a candidate set given for each cell.
    '''
    def __init__(self, blockR: int, blockC: int, candidates: list[list[list[int]]]):
        '''
        blockR = rows per sub block
        blockC = cols per sub block
        candidates = N x N grid of candidate list for each cell
        '''
        N = blockR*blockC
        super().__init__(blockR,blockC,[[0]*N for _ in range(N)])
        assert len(candidates) == N and all(len(row) == N for row in candidates)
        assert all(all(len(set(values)) == len(values) and all(1 <= value <= N for value in values) for values in row) for row in candidates)
        self.candidates = [[values[:] for values in row] for row in candidates]
    def toCnf(self) -> list[list[int]]:
        '''
        The additional constraints added constrain cell values to those in the
        candidate sets. This makes the original constraints redundant for
        assigning a value to a cell.
        '''
        result = super().toCnf()
        N = self.nums
        x = lambda r,c,n : 1 + (r*N+c)*N + (n-1)
        for r in range(N):
            for c in range(N):
                result.append([x(r,c,n) for n in self.candidates[r][c]])
        return result
