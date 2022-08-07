from . import SatPuzzleLatinSquare

class SatPuzzleSudokuConsecutive(SatPuzzleLatinSquare):
    '''
    Latin Square with edge markings for orthogonally adjacent cells that must
    have consecutive values. This does not have sub blocks like normal Sudoku.
    '''
    def __init__(self, givens: list[list[int]], consec_pairs: set[tuple[tuple[int,int],tuple[int,int]]]):
        '''
        givens = N x N grid of given numbers
        consec_pairs = list of (r1,c1),(r2,c2) specifying 2 cells that must have consecutive values
            these should only be orthogonally adjacent
        '''
        N = len(givens)
        super().__init__(givens)
        assert all(0 <= r1 < N and 0 <= c1 < N and 0 <= r2 < N and 0 <= c2 < N for (r1,c1),(r2,c2) in consec_pairs)
        self.consec_pairs = set(p for p in consec_pairs)
    def toCnf(self) -> list[list[int]]: # extend to add extra constraints
        '''
        Add constraints for orthogonally adjacent cells
        Let c1,c2 be the cells and x(c,n) mean the variable for n assigned to
        cell c. The possible assignments are 2 distinct values to these cells.
        If we constrain the values to be consecutive, then we add the clauses:
        - not x(c1,a) or not x(c2,b) (for each non consecutive pair a,b)
        If c1,c2 are assigned consecutive values, then all these clauses will be
        true. Otherwise, one of them will be false. For requiring 2 cells to be
        non consecutive, use clauses of the same form for consecutive pairs a,b.
        The reasoning is similar.
        '''
        result = super().toCnf()
        N = self.nums
        x = lambda r,c,n : 1 + (r*N+c)*N + (n-1) # get variable number
        consec = [(a,b) for a in range(1,N+1) for b in range(1,N+1) if abs(a-b) == 1]
        nonconsec = [(a,b) for a in range(1,N+1) for b in range(1,N+1) if abs(a-b) > 1]
        for r in range(N-1): # horizontal markers - (r,c) and (r+1,c)
            for c in range(N):
                # if must be consecutive, then for any pair of nonconsecutive numbers, either cell is not equal to it
                # if must not be consecutive, then for any pair of consecutive numbers, either cell is not equal to it
                for a,b in nonconsec if ((r,c),(r+1,c)) in self.consec_pairs else consec:
                    result.append([-x(r,c,a),-x(r+1,c,b)])
        for r in range(N): # vertical markers - (r,c) and (r,c+1)
            for c in range(N-1):
                for a,b in nonconsec if ((r,c),(r,c+1)) in self.consec_pairs else consec:
                    result.append([-x(r,c,a),-x(r,c+1,b)])
        return result
