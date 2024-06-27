def count_favourite_singers(singers):
    # Dictionary to count occurrences of each singer
    singer_count = {}

    for singer in singers:
        if singer in singer_count:
            singer_count[singer] += 1
        else:
            singer_count[singer] = 1

    # Find the maximum count of songs for any singer
    max_count = max(singer_count.values())
    print(max_count, "============")

    # Count how many singers have this maximum count
    favourite_singer_count = sum(1 for count in singer_count.values() if count == max_count)

    return favourite_singer_count

# Read input values
# n = int(input())  # Number of songs
singers = list(map(int, input().split()))  # Singer IDs for each song

# Get the result
result = count_favourite_singers(singers)

# Print the result
print(result)
