
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
    if len(grid) != 81:
        print("Grid must be 81 length")
    else:
        zip_data = zip(boxes, grid)
        my_grid = dict(zip_data)
        return my_grid