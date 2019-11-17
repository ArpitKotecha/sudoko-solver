
from utils import *


def grid_values(grid):
    """Convert grid string into {<box>: <value>} dict with '.' value for empties.

    Args:
        grid: Sudoku grid in string form, 81 characters long
    Returns:
        Sudoku grid in dictionary form:
        - keys: Box labels, e.g. 'A1'
        - values: Value in corresponding box, e.g. '8', or '.' if it is empty.
    """
    values = []
    all_digits = '123456789'
    for value in grid:
        if value == '.':
            values.append(all_digits)
        elif value in all_digits:
            values.append(value)
    assert len(values) == 81
    return dict(zip(boxes, values))

def eliminate(values):
    """Eliminate values from peers of each box with a single value.

    Go through all the boxes, and whenever there is a box with a single value,
    eliminate this value from the set of values of all its peers.

    Args:
        values: Sudoku in dictionary form.
    Returns:
        Resulting Sudoku in dictionary form after eliminating values.
    """
    for boxKey in values.keys():
        if len(values[boxKey]) == 1:
            for peerKey in peers[boxKey]:
                values[peerKey] = values[peerKey].replace(values[boxKey],'')
    return values  

display(eliminate(grid_values('..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3..')))
