def find_combinations(arr, target):
    def backtrack(start, target, path):
        if target == 0:
            result.append(path)
            return
        for i in range(start, len(arr)):
            if arr[i] <= target:
                backtrack(i, target - arr[i], path + [arr[i]])

    result = []
    backtrack(0, target, [])
    return result

# Example usage
input1 = 12
input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

combinations = find_combinations(input_list, input1)
print(f"Combinations that add up to {input1}: {combinations}")
