from . import SatPuzzleSudokuStandard

class SatPuzzleSudokuKropki(SatPuzzleSudokuStandard):
    '''
    Standard Sudoku with some circles on the edges. White circles mean the 2
    values must be consecutive. Black circles mean one value is double of the
    other. No circle means the numbers are neither.
    '''
    def __init__(self, blockR: int, blockC, white: set[tuple[tuple[int,int],tuple[int,int]]], black: set[tuple[tuple[int,int],tuple[int,int]]]):
        '''
        blockR = rows per sub block
        blockC = cols per sub block
        white = set of (r1,c1),(r2,c2) cell pairs with a white circle
        black = set of (r1,c1),(r2,c2) cell pairs with a black circle
        '''
        N = blockR*blockC
        super().__init__(blockR,blockC,[[0]*N for _ in range(N)])
        assert all(0 <= r1 < N and 0 <= c1 < N and 0 <= r2 < N and 0 <= c2 < N for (r1,c1),(r2,c2) in white)
        assert all(0 <= r1 < N and 0 <= c1 < N and 0 <= r2 < N and 0 <= c2 < N for (r1,c1),(r2,c2) in black)
        assert white & black == set()
        self.white = set(p for p in white)
        self.black = set(p for p in black)
    def toCnf(self) -> list[list[int]]: # extend to add extra constraints
        '''
        These constraints are handled similarly to those in Consecutive Sudoku.
        For each pair of cells c1,c2 and each pair a,b of (distinct) cell values
        that are not allowed in these 2 cells, add the clause:
        - not x(c1,a) or not x(c2,b)
        '''
        result = super().toCnf()
        N = self.nums
        x = lambda r,c,n : 1 + (r*N+c)*N + (n-1) # get variable number
        # sets of possible pairs
        consec = set((a,b) for a in range(1,N+1) for b in range(1,N+1) if abs(a-b) == 1)
        double = set((a,b) for a in range(1,N+1) for b in range(1,N+1) if a == 2*b or a*2 == b)
        neither = set((a,b) for a in range(1,N+1) for b in range(1,N+1) if a != b and ((a,b) not in consec) and ((a,b) not in double))
        all_pairs = set((a,b) for a in range(1,N+1) for b in range(1,N+1) if a != b)
        # complements for adding clauses
        c_consec = all_pairs - consec
        c_double = all_pairs - double
        c_neither = all_pairs - neither
        for r in range(N-1): # circles on horizontal (vertical pair)
            for c in range(N):
                pairs = c_consec if ((r,c),(r+1,c)) in self.white else (c_double if ((r,c),(r+1,c)) in self.black else c_neither)
                for a,b in pairs:
                    result.append([-x(r,c,a),-x(r+1,c,b)])
        for r in range(N): # circles on vertical (horizontal pair)
            for c in range(N-1):
                pairs = c_consec if ((r,c),(r,c+1)) in self.white else (c_double if ((r,c),(r,c+1)) in self.black else c_neither)
                for a,b in pairs:
                    result.append([-x(r,c,a),-x(r,c+1,b)])
        return result
