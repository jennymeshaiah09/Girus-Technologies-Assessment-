def is_valid_group(values):
    """Check if a list contains digits 1–9 without repetition."""
    return set(values) == set('123456789')
def validate_sudoku(board, custom_zones):
    # Validate rows
    for row in board:
        if not is_valid_group(row):
            return False
    # Validate columns
    for col in range(9):
        column = [board[row][col] for row in range(9)]
        if not is_valid_group(column):
            return False
    # Validate custom zones
    for zone in custom_zones:
        zone_values = [board[row][col] for (row, col) in zone]
        if not is_valid_group(zone_values):
            return False
    return True
# A valid filled Sudoku board
board = [
    ['5', '3', '4', '6', '7', '8', '9', '1', '2'],
    ['6', '7', '2', '1', '9', '5', '3', '4', '8'],
    ['1', '9', '8', '3', '4', '2', '5', '6', '7'],
    ['8', '5', '9', '7', '6', '1', '4', '2', '3'],
    ['4', '2', '6', '8', '5', '3', '7', '9', '1'],
    ['7', '1', '3', '9', '2', '4', '8', '5', '6'],
    ['9', '6', '1', '5', '3', '7', '2', '8', '4'],
    ['2', '8', '7', '4', '1', '9', '6', '3', '5'],
    ['3', '4', '5', '2', '8', '6', '1', '7', '9'],
]
# Example of custom zones (simulating 3x3 blocks)
custom_zones = [
    [(0,0), (0,1), (0,2), (1,0), (1,1), (1,2), (2,0), (2,1), (2,2)],  # Top-left block
    [(0,3), (0,4), (0,5), (1,3), (1,4), (1,5), (2,3), (2,4), (2,5)],  # Top-middle block
    [(0,6), (0,7), (0,8), (1,6), (1,7), (1,8), (2,6), (2,7), (2,8)],  # Top-right block
    [(3,0), (3,1), (3,2), (4,0), (4,1), (4,2), (5,0), (5,1), (5,2)],  # Middle-left block
    [(3,3), (3,4), (3,5), (4,3), (4,4), (4,5), (5,3), (5,4), (5,5)],  # Middle-middle block
    [(3,6), (3,7), (3,8), (4,6), (4,7), (4,8), (5,6), (5,7), (5,8)],  # Middle-right block
    [(6,0), (6,1), (6,2), (7,0), (7,1), (7,2), (8,0), (8,1), (8,2)],  # Bottom-left block
    [(6,3), (6,4), (6,5), (7,3), (7,4), (7,5), (8,3), (8,4), (8,5)],  # Bottom-middle block
    [(6,6), (6,7), (6,8), (7,6), (7,7), (7,8), (8,6), (8,7), (8,8)],  # Bottom-right block
]
# Run validation
print(validate_sudoku(board, custom_zones))
