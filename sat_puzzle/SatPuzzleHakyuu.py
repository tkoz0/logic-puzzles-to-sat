from . import SatPuzzleSuguruGeneral

class SatPuzzleHakyuu(SatPuzzleSuguruGeneral):
    '''
    A Suguru variant that uses a different rule for restricting number
    placement. Within each row/col, all occurrences of a number n must have at
    least n cells between them.
    '''
    def __init__(self, givens: list[list[int]], areas: list[list[int]]):
        '''
        givens = grid of given numbers, 0 for none, otherwise they must not be
            larger than their area size
        areas = area for each cell, each area represented by a unique symbol
        '''
        R = len(givens)
        C = len(givens[0])
        self.rows = R
        self.cols = C
        assert R > 0 and C > 0
        assert all(len(row) == C for row in givens)
        assert len(areas) == R and all(len(row) == C for row in areas)
        super().__init__(R*C,sum(areas,[]),sum(givens,[]))
    def toCnf(self) -> list[list[int]]:
        '''
        For each cell c1 and a number n, x(c1,n) implies n is not assigned to
        some cells in the same row/col depending on n. For each cell c2 from 1
        to n away from c1 in the same row/col, add this constraint if n is <=
        the size of the area(s) of c1 and c2:
        - not x(c1,n) or not x(c2,n)
        '''
        result = super().toCnf()
        for r in range(self.rows):
            for c in range(self.cols):
                # n at (r,c) implies n not within n cells in orthogonal directions
                i1 = r*self.cols+c
                area1 = self.areas[i1]
                area1size = len(self.areasmap[area1])
                for n in range(1,area1size+1):
                    for d in range(1,n+1): # distance from r,c
                        for rr,cc in [(r+d,c),(r-d,c),(r,c+d),(r,c-d)]:
                            if rr < 0 or rr >= self.rows or cc < 0 or cc >= self.cols:
                                continue # off grid
                            i2 = rr*self.cols+cc
                            area2 = self.areas[i2]
                            area2size = len(self.areasmap[area2])
                            if n <= area2size: # n at (r,c) implies n not at (rr,cc)
                                result.append([-self.varmap[i1,n],-self.varmap[i2,n]])
        return result
    def toSol(self, satSol: list[int]) -> list[list[int]]:
        sol = super().toSol(satSol)
        return [sol[i:i+self.cols] for i in range(0,self.rows*self.cols,self.cols)]
