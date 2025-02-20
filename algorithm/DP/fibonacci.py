def fibonacci_bottom_up(n):
    if n <= 1:  # Base case
        return n
    fib = [0] * (n + 1)  # Create an array to store Fibonacci numbers
    fib[1] = 1  # Initialize first two Fibonacci numbers
    for i in range(2, n + 1):  # Fill the array iteratively
        fib[i] = fib[i - 1] + fib[i - 2]
    return fib[n]

# Example usage
n = 10
# print(f"Bottom-Up: The {n}th Fibonacci number is {fibonacci_bottom_up(n)}")


def fibonacci_top_down(n, memo={}):
    if n in memo:  # Check if already computed
        return memo[n]
    if n <= 1:  # Base case
        return n
    # Store result in memo dictionary
    memo[n] = fibonacci_top_down(n - 2, memo) + fibonacci_top_down(n - 1, memo)
    return memo[n]

# Example usage
n = 4
print(f"Top-Down: The {n}th Fibonacci number is {fibonacci_top_down(n)}")
