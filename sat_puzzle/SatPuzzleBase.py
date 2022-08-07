from typing import Any, Iterator
import pycosat

class SatPuzzleBase:
    '''
    Base class for a puzzle to SAT reducer. Must override the following:
    - toCnf: convert a puzzle instance to a CNF SAT instance
    - toSol: convert the solution to the SAT problem back to the puzzle solution
    The other functions extend the functionality of these and should not need to
    be overridden by subclasses.
    '''
    def toCnf(self) -> list[list[int]]:
        '''
        Convert puzzle to a CNF logic expression. The return value is a list of
        clauses similar to the DIMACS CNF format. Each clause is a list of
        nonzero integers (+n for variable n and -n for the negation of variable
        n). The value 0 should not be included, it is simply the clause
        terminator for the DIMACS CNF format and is not necessary for this list
        of lists representation.
        '''
        assert 0, 'not implemented'
        return []
    def toSol(self, satSol: list[int]) -> Any:
        '''
        Convert a solution to the CNF SAT instance into a puzzle solution. The
        type returned should be determined by the subclass.
        '''
        assert 0, 'not implemented'
    def cnfSolve(self) -> list[int]:
        '''
        Solves the CNF problem returned by self.toCnf(). Currently, pycosat
        (Python3 package for PicoSAT) is used. The return value is a list of
        nonzero integers (+n for n true and -n for n false), or the empty list
        if no solution is found.
        '''
        result = pycosat.solve(self.toCnf())
        assert result != 'UNKNOWN'
        return [] if result == 'UNSAT' else result
    def cnfSolveAll(self) -> Iterator[list[int]]:
        '''
        Finds all solutions to the CNF problem, returning an iterator of them.
        '''
        return pycosat.itersolve(self.toCnf())
    def solve(self) -> Any:
        '''
        Finds a solution to the logic puzzle. Currently, an exception should
        occur if no solution is found.
        '''
        return self.toSol(self.cnfSolve())
    def solveAll(self) -> Iterator[Any]:
        '''
        Returns an iterator of all solutions to the logic puzzle.
        '''
        return map(self.toSol,self.cnfSolveAll())
