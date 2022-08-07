from . import SatPuzzleSuguruGeneral

class SatPuzzleSuguruStandard(SatPuzzleSuguruGeneral):
    '''
    An M x N grid divided into areas. Each area of size A must contain the
    numbers 1,2,..,N. The same number cannot be adjacent or diagonally adjacent.
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
        For each cell c1, add up to 8 constraints for neighboring cells c2:
        - not x(c1,n) or not x(c2,n)
        This needs to be done for all n limited by the size of the area(s) c1
        and c2 are in.
        '''
        result = super().toCnf()
        for r in range(self.rows):
            for c in range(self.cols):
                # for the 8 cells around it
                for dr in range(-1,2):
                    for dc in range(-1,2):
                        if dr == 0 and dc == 0:
                            continue
                        rr,cc = r+dr,c+dc
                        if rr < 0 or rr >= self.rows or cc < 0 or cc >= self.cols:
                            continue # off grid
                        i1 = r*self.cols+c
                        i2 = rr*self.cols+cc
                        area1 = self.areas[i1]
                        area2 = self.areas[i2]
                        area1size = len(self.areasmap[area1])
                        area2size = len(self.areasmap[area2])
                        # n at (r,c) implies n not at at (rr,cc)
                        for n in range(1,min(area1size+1,area2size+1)):
                            result.append([-self.varmap[(i1,n)],-self.varmap[(i2,n)]])
        return result
    def toSol(self, satSol: list[int]) -> list[list[int]]:
        sol = super().toSol(satSol)
        return [sol[i:i+self.cols] for i in range(0,self.rows*self.cols,self.cols)]
