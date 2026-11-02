# Design 8-Queens matrix having first Queen placed. Use backtracking to 
# place remaining Queens to generate the final 8-queen’s matrix.

N = int(input("Enter N: "))
board = [[0]*N for _ in range(N)]
board[0][0] = 1
def safe(r, c):
    for i in range(r):
        if board[i][c] or (c-r+i >= 0 and board[i][c-r+i]) or (c+r-i < N and board[i][c+r-i]):
            return False
    return True
def solve(r):
    if r == N:
        return True
    for c in range(N):
        if safe(r, c):
            board[r][c] = 1
            if solve(r+1):
                return True
            board[r][c] = 0
    return False
solve(1)
for row in board:
    print(*row)





# n = int(input("Enter N: "))
# board = [[0] * n for _ in range(n)]
# def safe(row, col):
#     for i in range(row):
#         if board[i][col] == 1:
#             return False
#         if col - (row - i) >= 0 and board[i][col - (row - i)] == 1:
#             return False
#         if col + (row - i) < n and board[i][col + (row - i)] == 1:
#             return False
#     return True
# def solve(row):
#     if row == n:
#         return True
#     for col in range(n):
#         if safe(row, col):
#             board[row][col] = 1
#             if solve(row + 1):
#                 return True
#             board[row][col] = 0
#     return False
# if n < 1:
#     print("Enter a positive number")
# elif solve(0):
#     print("N-Queens Matrix:")
#     for row in board:
#         print(row)
# else:
#     print("No solution exists")