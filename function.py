
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

def only_choice(values):
    """Finalize all values that are the only choice for a unit.

    Go through all the units, and whenever there is a unit with a value
    that only fits in one box, assign the value to this box.

    Input: Sudoku in dictionary form.
    Output: Resulting Sudoku in dictionary form after filling in only choices.
    """
    # TODO: Implement only choice strategy here
    for unit in unitlist:
        for digit in '123456789':
            matchedKeys = [box for box in unit if digit in values[box]]
            if len(matchedKeys) == 1:
                values[matchedKeys[0]] = digit

    return values

def reduce_puzzle(values):
    """
    Iterate eliminate() and only_choice(). If at some point, there is a box with no available values, return False.
    If the sudoku is solved, return the sudoku.
    If after an iteration of both functions, the sudoku remains the same, return the sudoku.
    Input: A sudoku in dictionary form.
    Output: The resulting sudoku in dictionary form.
    """
    notSolved = False
    while not notSolved:
        # Count boxes with correct/determined values
        solvedValuesBefore = len([boxKey for boxKey in values.keys() if len(values[boxKey]) == 1])
        # Using elimination
        values = eliminate(values)
        # Using Only Choice
        values = only_choice(values)
        # Count boxes with correct/determined values after elimination and only choice
        solvedValuesAfter = len([boxKey for boxKey in values.keys() if len(values[boxKey]) == 1])
        # Check if new correct/determined values are added
        notSolved = solvedValuesBefore == solvedValuesAfter
        # Sanity check, return False if there is a box with zero available values:
        if len([boxKey for boxKey in values.keys() if len(values[boxKey]) == 0]):
            return False
    return values

def depthFirstTreeSearch(values):
    "Using depth-first search and propagation, create a search tree and solve the sudoku."
    # First, reduce the puzzle using the previous function
    values = reduce_puzzle(values)
    if values is False:
        return False ## Failed earlier
    if all(len(values[s]) == 1 for s in boxes): 
        return values ## Solved!

    # Choose one of the unfilled squares with the fewest possibilities
    n,s = min((len(values[s]), s) for s in boxes if len(values[s]) > 1)

    # Now use recursion to solve each one of the resulting sudokus, and if one returns a value (not False), return that answer!
    for value in values[s]:
        newSudoko = values.copy()
        newSudoko[s] = value
        if attempt := depthFirstTreeSearch(newSudoko):
            return attempt
    

    


print("\n\nFirst Sudoko:-\n")
display(depthFirstTreeSearch(only_choice(eliminate(grid_values('..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3..')))))
print("\n\nSecond Sudoko:-\n")
display(depthFirstTreeSearch(only_choice(eliminate(grid_values('4.....8.5.3..........7......2.....6.....8.4......1.......6.3.7.5..2.....1.4......')))))
