'''
Classes representing propositional logic expressions. These are all immutable.
'''

from typing import Iterable, Union

_label_t = Union[str,int]

class EXPR:
    ''' Base class, do not instantiate directly '''
    def __init__(self, exprs: Iterable['EXPR'], min_length = 0, max_length = 255):
        '''
        Initialize a propositional logic expression.
        '''
        self.exprs = tuple(exprs)
        assert min_length <= len(self.exprs) <= max_length
    def eval(self, values: dict[_label_t,bool]) -> bool:
        '''
        Evaluate a logic expression given a variable assignment.
        '''
        assert 0, 'not implemented'
        return False
    def __eq__(self, other: 'EXPR') -> bool:
        return isinstance(other,type(self)) and self.exprs == other.exprs
    def __hash__(self) -> int:
        h = 0
        for expr in self.exprs:
            h += hash(expr)
        h += hash(type(self))
        return h % (2**61-1)
    def __repr__(self) -> str:
        return f'{type(self).__name__}({",".join(repr(expr) for expr in self.exprs)})'

class VAR(EXPR):
    ''' A single variable '''
    def __init__(self, label: _label_t):
        super().__init__([],0,0)
        self.label = label
    def eval(self, values: dict[_label_t,bool]) -> bool:
        return values[self.label]
    def __eq__(self, other: 'EXPR') -> bool:
        return isinstance(other,type(self)) and self.label == other.label
    def __hash__(self) -> int:
        return hash(self.label) % (2**61-1)
    def __repr__(self) -> str:
        return f'VAR({repr(self.label)})'

class NOT(EXPR):
    def __init__(self, expr: EXPR):
        super().__init__([expr],1,1)
    def eval(self, values: dict[_label_t,bool]) -> bool:
        return not self.exprs[0].eval(values)

class AND(EXPR):
    def __init__(self, *exprs: EXPR):
        super().__init__(exprs,2)
    def eval(self, values: dict[_label_t,bool]) -> bool:
        return all(expr.eval(values) for expr in self.exprs)

class OR(EXPR):
    def __init__(self, *exprs: EXPR):
        super().__init__(exprs,2)
    def eval(self, values: dict[_label_t,bool]) -> bool:
        return any(expr.eval(values) for expr in self.exprs)

class IF(EXPR):
    def __init__(self, expr1: EXPR, expr2: EXPR):
        super().__init__([expr1,expr2],2,2)
    def eval(self, values: dict[_label_t,bool]) -> bool:
        return (not self.exprs[0].eval(values)) or self.exprs[1].eval(values)

class IFF(EXPR):
    def __init__(self, expr1: EXPR, expr2: EXPR):
        super().__init__([expr1,expr2],2,2)
    def eval(self, values: dict[_label_t,bool]) -> bool:
        return self.exprs[0].eval(values) == self.exprs[1].eval(values)

class XOR(EXPR):
    def __init__(self, expr1: EXPR, expr2: EXPR):
        super().__init__([expr1,expr2],2,2)
    def eval(self, values: dict[_label_t,bool]) -> bool:
        return self.exprs[0].eval(values) != self.exprs[1].eval(values)

class XNOR(XOR): # same as IFF
    def __init__(self, expr1: EXPR, expr2: EXPR):
        super().__init__(expr1,expr2)
    def eval(self, values: dict[_label_t,bool]) -> bool:
        return not super().eval(values)

class NAND(AND):
    def __init__(self, *exprs: EXPR):
        super().__init__(*exprs)
    def eval(self, values: dict[_label_t,bool]) -> bool:
        return not super().eval(values)

class NOR(OR):
    def __init__(self, *exprs: EXPR):
        super().__init__(*exprs)
    def eval(self, values: dict[_label_t,bool]) -> bool:
        return not super().eval(values)

def _tseitin_mapper(expr: EXPR, var2expr: dict[int,EXPR], expr2var: dict[EXPR,int], next_var = 1) -> int:
    ''' produce mapping of each (sub) expression to a variable number '''
    if expr not in expr2var: # give expr a variable number
        expr2var[expr] = next_var
        var2expr[next_var] = expr
        next_var += 1
        for sub_expr in expr.exprs: # recursively apply to sub expressions
            next_var = _tseitin_mapper(sub_expr,var2expr,expr2var,next_var)
    return next_var

def _tseitin_helper(expr: EXPR, expr2var: dict[EXPR,int], cnf: list[list[int]], done_exprs: set[int] = set()):
    x = expr2var[expr]
    if x in done_exprs:
        return
    ys = [expr2var[e] for e in expr.exprs]
    if isinstance(expr,VAR):
        return
    elif isinstance(expr,NOT): # x <-> not y
        y, = ys
        cnf.append([-x,-y])
        cnf.append([x,y])
    elif isinstance(expr,AND): # x <-> y1 and y2 and ...
        cnf.append([x]+[-y for y in ys])
        for y in ys:
            cnf.append([-x,y])
    elif isinstance(expr,OR): # x <-> y1 or y2 or ...
        cnf.append([-x]+ys)
        for y in ys:
            cnf.append([x,-y])
    elif isinstance(expr,IF): # x <-> (y -> z)
        y,z = ys
        cnf.append([-x,-y,z])
        cnf.append([x,y])
        cnf.append([x,-z])
    elif isinstance(expr,IFF): # x <-> (y <-> z)
        y,z = ys
        cnf.append([-x,-y,z])
        cnf.append([-x,y,-z])
        cnf.append([x,y,z])
        cnf.append([x,-y,-z])
    elif isinstance(expr,XOR): # x <-> (y ^ z)
        y,z = ys
        cnf.append([-x,y,z])
        cnf.append([-x,-y,-z])
        cnf.append([x,-y,z])
        cnf.append([x,y,-z])
    elif isinstance(expr,XNOR): # x <-> (y <-> z)
        y,z = ys
        cnf.append([-x,-y,z])
        cnf.append([-x,y,-z])
        cnf.append([x,y,z])
        cnf.append([x,-y,-z])
    elif isinstance(expr,NAND): # x <-> not y1 or not y2 or ...
        cnf.append([-x]+[-y for y in ys])
        for y in ys:
            cnf.append([x,y])
    elif isinstance(expr,NOR): # x <-> not y1 and not y2 and ...
        cnf.append([x]+ys)
        for y in ys:
            cnf.append([-x,-y])
    else:
        assert 0, f'invalid expression type {type(expr)}'
    done_exprs.add(x)
    for sub_expr in expr.exprs:
        _tseitin_helper(sub_expr,expr2var,cnf,done_exprs)

def tseitin_transform(expr: EXPR) -> tuple[list[list[int]],dict[int,EXPR]]:
    '''
    Creates an equivalent CNF representation for a given propositional logic
    expression and a mapping of the variables in this CNF instance to
    expressions or variables in the original expression.
    '''
    # make map of (sub) expressions to CNF variables
    var2expr: dict[int,EXPR] = dict()
    expr2var: dict[EXPR,int] = dict()
    _tseitin_mapper(expr,var2expr,expr2var)
    # start with the variable for the expression
    cnf = [[expr2var[expr]]]
    # conjunct substitutions for all sub exprs (exclude single vars)
    _tseitin_helper(expr,expr2var,cnf)
    return cnf,var2expr
