from . import SatPuzzleSudokuGeneral

class SatPuzzleSudokuOverlap(SatPuzzleSudokuGeneral):
    '''
    A generalization of Sudoku variants that overlap several standard sudoku
    grids overlapping on rectangular sub blocks.
    '''
    def __init__(self, blockR: int, blockC: int, givens: list[list[int]], corners: list[tuple[int,int]]):
        '''
        blockR = number of rows in each sub block
        blockC = number of columns in each sub block
        givens = grid of given values, 0 for no value, should have 0 in unused areas
        corners = list of (r,c) positions (with (0,0) being the top left)
            representing the top left corners of the standard sudoku puzzles
        '''
        N = blockR*blockC
        assert all(pr%blockR == 0 and pc%blockC == 0 for pr,pc in corners)
        brows = max(p[0] for p in corners)//blockR + blockC
        bcols = max(p[1] for p in corners)//blockC + blockR
        R = brows*blockR
        C = bcols*blockC
        self.rows = R
        self.cols = C
        self.blockR = blockR
        self.blockC = blockC
        self.corners = corners[:]
        assert len(givens) == R and all(len(row) == C for row in givens)
        areas = []
        self.blockmap = [[False]*bcols for _ in range(brows)]
        for pr,pc in corners: # for each (overlapping) standard sudoku
            for r in range(pr,pr+N): # rows
                areas.append(list(range(r*C+pc,r*C+pc+N)))
            for c in range(pc,pc+N): # cols
                areas.append(list(range(pr*C+c,(pr+N)*C+c,C)))
            for br in range(blockC): # areas for this standard puzzle
                for bc in range(blockR):
                    brow,bcol = pr//blockR+br, pc//blockC+bc
                    if not self.blockmap[brow][bcol]: # no area for this block yet
                        self.blockmap[brow][bcol] = True
                        areas.append([(brow*blockR+rr)*C+(bcol*blockC+cc) for rr in range(blockR) for cc in range(blockC)])
        # set dummy number in unused areas
        givens2 = [row[:] for row in givens]
        for brow,blockmaprow in enumerate(self.blockmap):
            for bcol,used in enumerate(blockmaprow):
                if not used:
                    for r in range(blockR):
                        for c in range(blockC):
                            assert givens[brow*blockR+r][bcol*blockC+c] == 0 # should provide 0 in unused space
                            givens2[brow*blockR+r][bcol*blockC+c] = 1
        super().__init__(R*C,N,areas,sum(givens2,[]))
    def toSol(self, satSol: list[int]) -> list[list[int]]:
        sol = super().toSol(satSol)
        gridSol = [sol[i:i+self.cols] for i in range(0,self.rows*self.cols,self.cols)]
        # set unused areas to zeroes
        for brow,blockmaprow in enumerate(self.blockmap):
            for bcol,used in enumerate(blockmaprow):
                if not used:
                    for r in range(self.blockR):
                        for c in range(self.blockC):
                            gridSol[brow*self.blockR+r][bcol*self.blockC+c] = 0
        return gridSol
