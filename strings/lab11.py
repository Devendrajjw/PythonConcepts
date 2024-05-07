def convert_to_zigzag(s, num_rows):
    if num_rows == 1 or num_rows >= len(s):
        return s

    # Create a list of strings to hold characters in each row
    rows = [' '] * num_rows

    # Index to track the current row
    current_row = 0

    # Direction flag to indicate whether we are moving down or up
    direction = 1

    # Iterate through each character in the string
    for char in s:
        rows[current_row] += char  # Add the character to the current row

        # Update current_row based on the direction
        current_row += direction

        # Change direction if we reach the top or bottom row
        if current_row == 0 or current_row == num_rows - 1:
            direction *= -1

    # Concatenate rows to form the zigzag pattern
    zigzag_pattern = '\n'.join(rows)

    return zigzag_pattern

# Example usage:
s = "PAYPALISHIRING"
num_rows = 3
result = convert_to_zigzag(s, num_rows)
print(result)
