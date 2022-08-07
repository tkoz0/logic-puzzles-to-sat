from . import SatPuzzleBase

class SatPuzzleSuguruGeneral(SatPuzzleBase):
    '''
    A generalization of of Suguru similar to the generalization of Sudoku. There
    are C > 0 cells divided into areas (specified by a number unique to each
    area). Each area (of size N) must have the numbers 1, 2, ..., N.
    '''
    def __init__(self, cells: int, areas: list[int], givens: list[int]):
        '''
        cells = number of cells, numbered from 0
        areas = list of area numbers assigned to each cell
        givens = list of given values, 0 for no value given
        '''
        assert cells > 0
        assert len(areas) == cells
        assert len(givens) == cells
        area_symbols = set(areas)
        areas_dict: dict[int,list[int]] = dict() # map symbol to list of cell indexes
        for symb in area_symbols:
            areas_dict[symb] = [i for i,a in enumerate(areas) if a == symb]
        assert all(0 <= n <= len(areas_dict[areas[i]]) for i,n in enumerate(givens))
        self.cells = cells
        self.areas = areas[:]
        self.areasmap = areas_dict
        self.givens = givens[:]
        # variable map for CNF conversion (i,n) -> var (i = cell num)
        self.varmap: dict[tuple[int,int],int] = dict()
        self.varmaprev: dict[int,tuple[int,int]] = dict() # reverse of above
        last_var = 0 # last variable number used in the next loop
        for i,area in enumerate(areas):
            area_size = len(self.areasmap[area])
            for n in range(1,area_size+1):
                self.varmap[(i,n)] = last_var+n
                self.varmaprev[last_var+n] = (i,n)
            last_var += area_size
    def toCnf(self) -> list[list[int]]:
        '''
        These look very similar to the Sudoku clauses, except the area size and
        amount of possible numbers is constrained by area sizes.
        '''
        result: list[list[int]] = []
        for c in range(self.cells): # each cell
            area_size = len(self.areasmap[self.areas[c]])
            result.append([self.varmap[(c,n)] for n in range(1,area_size+1)]) # has a value
            for n1 in range(1,area_size+1): # and it is unique
                for n2 in range(n1+1,area_size+1):
                    result.append([-self.varmap[(c,n1)],-self.varmap[(c,n2)]])
        for area in self.areasmap: # each area
            cells = self.areasmap[area]
            area_size = len(cells)
            for n in range(1,area_size+1): # has each number
                result.append([self.varmap[(c,n)] for c in cells])
                for i,c1 in enumerate(cells): # that number is in a unique cell (redundant)
                    for c2 in cells[i+1:]:
                        result.append([-self.varmap[(c1,n)],-self.varmap[(c2,n)]])
            for c,n in enumerate(self.givens): # use clues
                if n != 0:
                    result.append([self.varmap[(c,n)]])
        return result
    def toSol(self, satSol: list[int]) -> list[int]:
        result = [0]*self.cells
        for v in filter(lambda x : x > 0, satSol):
            c,n = self.varmaprev[v]
            assert result[c] == 0 # only 1 value assigned to a cell
            result[c] = n
        assert all(n > 0 for n in result)
        return result
