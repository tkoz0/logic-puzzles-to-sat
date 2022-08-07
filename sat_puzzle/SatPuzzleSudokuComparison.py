from . import SatPuzzleSudokuStandard

class SatPuzzleSudokuComparison(SatPuzzleSudokuStandard):
    '''
    Empty Sudoku grid with all cell borders inside the sub blocks showing a less
    than relation between adjacent cell pairs (within the same sub block).
    '''
    def __init__(self, blockR: int, blockC: int, relations: set[tuple[tuple[int,int],tuple[int,int]]]):
        '''
        blockR = rows per sub block
        blockC = cols per sub block
        relations = cell pairs (r1,c1),(r2,c2) where r1,c1 value < r2,c2 value
        '''
        N = blockR*blockC
        super().__init__(blockR,blockC,[[0]*(N) for _ in range(N)])
        assert all(0 <= r1 < N and 0 <= c1 < N and 0 <= r2 < N and 0 <= c2 < N for (r1,c1),(r2,c2) in relations)
        self.relations = set(p for p in relations)
    def toCnf(self) -> list[list[int]]:
        '''
        For each cell pair c1,c2 with c1 value < c2 value, add clauses:
        not x(c1,b) or not x(c2,a) for 1 <= a < b <= N
        This disallows all assignments that violate the less than constraint.
        '''
        result = super().toCnf()
        N = self.nums
        x = lambda r,c,n : 1 + (r*N+c)*N + (n-1) # get variable number
        for (r1,c1),(r2,c2) in self.relations:
            # must have a not equal in invalid pairs (r1,c1) > (r2,c2)
            for a in range(1,N+1):
                for b in range(a+1,N+1):
                    result.append([-x(r1,c1,b),-x(r2,c2,a)])
        return result
