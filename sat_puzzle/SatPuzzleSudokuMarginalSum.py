from . import SatPuzzleSudokuStandard
from typing import Generator

class SatPuzzleSudokuMarginalSum(SatPuzzleSudokuStandard):
    '''
    Sudoku grid with no given cell clues. The clues given are the sum of the
    first 3 numbers from the edges. This class extends to other sub block sizes.
    '''
    def __init__(self, blockR: int, blockC: int, top: list[int], bottom: list[int], left: list[int], right: list[int]):
        '''
        blockR = rows per sub block
        blockC = cols per sub block
        top = sum of top blockR numbers in each column
        bottom = sum of bottom blockR numbers in each column
        left = sum of left blockC numbers in each row
        righth = sum of right blockC numbers in each row
        '''
        N = blockR*blockC
        super().__init__(blockR,blockC,[[0]*N for _ in range(N)])
        assert len(top) == len(bottom) == len(left) == len(right) == N
        self.top = top[:]
        self.bottom = bottom[:]
        self.left = left[:]
        self.right = right[:]
    def toCnf(self) -> list[list[int]]:
        '''
        The marginal sum constraints can be represented as clauses for the
        permutations of numbers not allowed (not n1 or not n2 or ...). If the
        numbers are assigned one of the disallowed permutations, there will be
        a false clause. Otherwise, all these clauses will be true. This grows
        exponentially in the blockR and blockC parameters so it is not a proper
        reduction.
        TODO research ways to make this reduction polynomial time and space
        '''
        result = super().toCnf()
        N = self.nums
        br = self.blockR
        bc = self.blockC
        x = lambda r,c,n : 1 + (r*N+c)*N + (n-1)
        # generator for all permutations of some of the numbers
        def recur(size: int, partial: list[int] = []) -> Generator[list[int],None,None]:
            if len(partial) == size:
                yield partial[:]
            else:
                for n in range(1,N+1):
                    if n not in partial:
                        yield from recur(size,partial+[n])
        # these clauses for the marginal sum grow exponentially with puzzle size
        for i in range(N):
            for perm in recur(br): # top
                if sum(perm) != self.top[i]:
                    result.append([-x(j,i,perm[j]) for j in range(br)])
            for perm in recur(br): # bottom
                if sum(perm) != self.bottom[i]:
                    result.append([-x(N-br+j,i,perm[j]) for j in range(br)])
            for perm in recur(bc): # left
                if sum(perm) != self.left[i]:
                    result.append([-x(i,j,perm[j]) for j in range(bc)])
            for perm in recur(bc): # right
                if sum(perm) != self.right[i]:
                    result.append([-x(i,N-bc+j,perm[j]) for j in range(bc)])
        return result
