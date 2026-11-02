# Non-recursive Fibonacci program

n = int(input("Enter the number of terms: "))
a, b = 0, 1
steps = 0
print("Fibonacci Series:")
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b
    steps += 1
print("\nStep Count:", steps)


# Recursive Fibonacci program

steps = 0
def fibonacci(n):
    global steps
    steps += 1
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
n = int(input("Enter the number of terms: "))
print("Fibonacci Series:")
for i in range(n):
    print(fibonacci(i), end=" ")
print("\nStep Count:", steps)
