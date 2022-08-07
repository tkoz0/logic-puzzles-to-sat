from . import SatPuzzleSudokuJigsaw

class SatPuzzleSukakuJigsaw(SatPuzzleSudokuJigsaw):
    '''
    Sukaku, but with irregularly shaped areas instead of rectangular.
    '''
    def __init__(self, areas: list[list[int]], candidates: list[list[list[int]]]):
        '''
        areas = N x N grid of cell areas, each area is a unique symbol
        candidates = N x N grid of candidate list for each cell
        '''
        N = len(areas)
        super().__init__([[0]*N for _ in range(N)],areas)
        assert len(candidates) == N and all(len(row) == N for row in candidates)
        assert all(all(len(set(values)) == len(values) and all(1 <= value <= N for value in values) for values in row) for row in candidates)
        self.candidates = [[values[:] for values in row] for row in candidates]
    def toCnf(self) -> list[list[int]]:
        '''
        The constraints here are handled exactly the same way as they are in
        regular Sukaku.
        '''
        result = super().toCnf()
        N = self.nums
        x = lambda r,c,n : 1 + (r*N+c)*N + (n-1)
        for r in range(N):
            for c in range(N):
                result.append([x(r,c,n) for n in self.candidates[r][c]])
        return result
