def FormattedDivision(num1, num2):
    result = num1 / num2
    formatted_result = f"{result:.4f}"
    return formatted_result

# Test cases
print(FormattedDivision(123456789, 10000))  # Output: "12,345.6789"
print(FormattedDivision(2, 3))  # Output: "0.6667"
print(FormattedDivision(10, 10))  # Output: "1.0000"
