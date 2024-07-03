def two_sum(nums, target):
    # Dictionary to store number and its index
    num_map = {}

    # Traverse through each element in the array
    for i, num in enumerate(nums):
        # Calculate the complement needed to reach the target
        complement = target - num

        # Check if the complement is already in the dictionary
        if complement in num_map:
            # Return the indices of the two numbers
            return [num_map[complement], i]

        # Otherwise, store the current number and its index in the dictionary
        num_map[num] = i

    # If no such pair is found, return an empty list
    return []

# Example usage:
nums = [1,2,3,4]
target = 7
result = two_sum(nums, target)
print(f"The indices of the two numbers that add up to {target} are: {result}")
