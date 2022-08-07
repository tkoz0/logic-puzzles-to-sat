from . import SatPuzzleBase

class SatPuzzleSudokuGeneral(SatPuzzleBase):
    '''
    A generalization of Sudoku, representing a puzzle as C > 0 cells (numbered
    0, 1, ..., C-1), a parameter N > 0, and sets of N cells (areas) which are
    constrained to contain the numbers 1, 2, ..., N, each exactly once.
    '''
    def __init__(self, cells: int, nums: int, areas: list[list[int]], givens: list[int]):
        '''
        cells = number of cells, numbered starting from 0
        nums = symbols in puzzle, represented as 1, 2, .., N
        areas = list of cells constrained to contain 1..N, each of size N
        givens = list of values given, 0 for no given value
        '''
        assert cells > 0
        assert nums > 0
        assert all(len(set(a)) == len(a) == nums for a in areas) # correct size
        assert all(all(0 <= c < cells for c in a) for a in areas) # valid index
        assert all(0 <= n <= nums for n in givens)
        self.cells = cells
        self.nums = nums
        self.areas = [a[:] for a in areas]
        self.givens = givens[:]
    def toCnf(self) -> list[list[int]]:
        '''
        variables: x(c,n) (0 <= c < cells, 1 <= n <= N)
        constraints:
        - each cell (c) has >= 1 value
          - x(c,1) or x(c,2) or ... or x(c,n)
        - each cell (c) has <= 1 value
          - express as for any pair, either number is not assigned to cell c
          - not x(c,a) or not x(c,b) (for 1 <= a < b <= N)
        - each area (cells a1,a2,..,aN) contains each number
          - x(a1,i) or x(a2,i) or ... or x(an,i) (for 1 <= i <= N)
        - each area (cells a1,a2,..,aN)) does not have a duplicate (redundant,
          necessary for efficiency) (for any 2 cells, either does not have n)
          - not x(a_i,n) or not x(a_j,n) (for each 1 <= n <= N and 1 <= i < j <= N)
        - use the given clues
          - x(c,i) (for each cell c with a given value i)
        '''
        result: list[list[int]] = []
        x = lambda c,n : 1 + c*self.nums + (n-1)
        for c in range(self.cells): # each cell has a value
            result.append([x(c,n) for n in range(1,self.nums+1)])
        for c in range(self.cells): # each cell has at most 1 value (for any 2 distinct values, one is not assigned to that cell)
            for n1 in range(1,self.nums+1):
                for n2 in range(n1+1,self.nums+1):
                    result.append([-x(c,n1),-x(c,n2)])
        for area in self.areas: # for each area
            for n in range(1,self.nums+1): # has each number
                result.append([x(c,n) for c in area])
                # add redundant clauses for efficiency
                for i,c1 in enumerate(area): # for any 2 cells, one does not have n (no duplicated numbers in an area)
                    for c2 in area[i+1:]:
                        result.append([-x(c1,n),-x(c2,n)])
        for c,n in enumerate(self.givens): # use the given clues
            if n != 0:
                result.append([x(c,n)])
        return result
    def toSol(self, satSol: list[int]) -> list[int]:
        result = [0]*self.cells
        to_c_n = lambda v : ((v-1)//self.nums, (v-1)%self.nums + 1)
        for v in filter(lambda x : x > 0, satSol):
            c,n = to_c_n(v)
            assert result[c] == 0 # only 1 value assigned to a cell
            result[c] = n
        assert all(n > 0 for n in result) # every cell has a value
        return result
