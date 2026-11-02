# Write a program to solve a fractional Knapsack problem using a greedy method.

# n = int(input("Enter number of items: "))
# v = list(map(int, input("Enter values: ").split()))
# w = list(map(int, input("Enter weights: ").split()))
# c = int(input("Enter capacity: "))
# items = sorted(zip(v, w), key=lambda x: x[0]/x[1], reverse=True)
# total = 0
# for value, weight in items:
#     if c >= weight:
#         total += value
#         c -= weight
#     else:
#         total += value * c / weight
#         break
# print("Maximum value:", total)


n = int(input("Enter the number of items:"))
v = list(map(int, input("Enter the values:").split()))
w = list(map(int, input("Enter the weights:").split()))
c = int(input("Enter the capacity:"))
items = sorted(zip(v,w), key=lambda x: x[0]/x[1], reverse=True)
total = 0
for value, weight in items:
    if c >= weight:
        total += value 
        c -= weight
    else:
        total += value * c / weight
        break
print("Maximum value:", total)
