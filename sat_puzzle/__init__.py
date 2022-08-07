'''
Module containing classes to convert logic puzzles to CNF SAT.
'''

from .SatPuzzleBase import SatPuzzleBase
from .SatPuzzleSudokuGeneral import SatPuzzleSudokuGeneral
from .SatPuzzleSuguruGeneral import SatPuzzleSuguruGeneral
from .SatPuzzleLatinSquare import SatPuzzleLatinSquare
from .SatPuzzleLatinSquareX import SatPuzzleLatinSquareX
from .SatPuzzleSudokuStandard import SatPuzzleSudokuStandard
from .SatPuzzleSudokuX import SatPuzzleSudokuX
from .SatPuzzleSudokuJigsaw import SatPuzzleSudokuJigsaw
from .SatPuzzleSudokuJigsawX import SatPuzzleSudokuJigsawX
from .SatPuzzleSudokuOverlap import SatPuzzleSudokuOverlap
from .SatPuzzleSudokuButterfly import SatPuzzleSudokuButterfly
from .SatPuzzleSudokuCluelessBase import SatPuzzleSudokuCluelessBase
from .SatPuzzleSudokuClueless1 import SatPuzzleSudokuClueless1
from .SatPuzzleSudokuClueless2 import SatPuzzleSudokuClueless2
from .SatPuzzleSudokuFlower import SatPuzzleSudokuFlower
from .SatPuzzleSudokuGattai8 import SatPuzzleSudokuGattai8
from .SatPuzzleSudokuConsecutive import SatPuzzleSudokuConsecutive
from .SatPuzzleSudokuKropki import SatPuzzleSudokuKropki
from .SatPuzzleSudokuMagicNumberX import SatPuzzleSudokuMagicNumberX
from .SatPuzzleSudokuSamurai import SatPuzzleSudokuSamurai
from .SatPuzzleSudokuOddEven import SatPuzzleSudokuOddEven
from .SatPuzzleSudokuOddEvenSamurai import SatPuzzleSudokuOddEvenSamurai
from .SatPuzzleSudokuMarginalSum import SatPuzzleSudokuMarginalSum
from .SatPuzzleSudokuShogun import SatPuzzleSudokuShogun
from .SatPuzzleSudokuSohei import SatPuzzleSudokuSohei
from .SatPuzzleSudokuSumo import SatPuzzleSudokuSumo
from .SatPuzzleSudokuWindmill import SatPuzzleSudokuWindmill
from .SatPuzzleSudokuComparison import SatPuzzleSudokuComparison
from .SatPuzzleSuguruStandard import SatPuzzleSuguruStandard
from .SatPuzzleHakyuu import SatPuzzleHakyuu
from .SatPuzzleSukaku import SatPuzzleSukaku
from .SatPuzzleSukakuJigsaw import SatPuzzleSukakuJigsaw

# list of all classes in the module
__all__ = \
[
    'SatPuzzleBase',
    'SatPuzzleSudokuGeneral',
    'SatPuzzleSuguruGeneral',
    'SatPuzzleLatinSquare',
    'SatPuzzleLatinSquareX',
    'SatPuzzleSudokuStandard',
    'SatPuzzleSudokuX',
    'SatPuzzleSudokuJigsaw',
    'SatPuzzleSudokuJigsawX',
    'SatPuzzleSudokuOverlap',
    'SatPuzzleSudokuButterfly',
    'SatPuzzleSudokuCluelessBase',
    'SatPuzzleSudokuClueless1',
    'SatPuzzleSudokuClueless2',
    'SatPuzzleSudokuFlower',
    'SatPuzzleSudokuGattai8',
    'SatPuzzleSudokuConsecutive',
    'SatPuzzleSudokuKropki',
    'SatPuzzleSudokuMagicNumberX',
    'SatPuzzleSudokuSamurai',
    'SatPuzzleSudokuOddEven',
    'SatPuzzleSudokuOddEvenSamurai',
    'SatPuzzleSudokuMarginalSum',
    'SatPuzzleSudokuShogun',
    'SatPuzzleSudokuSohei',
    'SatPuzzleSudokuSumo',
    'SatPuzzleSudokuWindmill',
    'SatPuzzleSudokuComparison',
    'SatPuzzleSuguruStandard',
    'SatPuzzleHakyuu',
    'SatPuzzleSukaku',
    'SatPuzzleSukakuJigsaw'
]
