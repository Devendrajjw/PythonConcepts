def is_prime(n):
    """Check if a number is a prime number."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def prime_batch_generator(start, end, batch_size=10):
    """Generate batches of prime numbers within the given range."""
    primes = []
    current = start
    while current <= end:
        if is_prime(current):
            primes.append(current)
        if len(primes) == batch_size:
            yield primes
            primes = []
        current += 1
    if primes:  # Yield remaining primes if any
        yield primes

# Get user input for range
start = int(input("Enter the lower bound of the range: "))
end = int(input("Enter the upper bound of the range: "))

# Create the generator
generator = prime_batch_generator(start, end)

# Use the generator to print batches of prime numbers
for batch in generator:
    print(batch)
