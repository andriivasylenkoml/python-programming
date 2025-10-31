import random 


"""task1"""  
# n = int(input("Enter number element n: "))

# a_real = [random.random() for _ in range(n)]
# print(f"\na) Real numbers [0, 1]: {a_real}")

# a_int = [random.randint(-10, 10) for _ in range(n)]
# print(f"\nb) Whole numbers [-10, 10]: {a_int}")

# a_pos = [random.randint(0, 50) for _ in range(n)]
# print(f"\nc) Positive integers: [0, 50]: {a_pos}")


"""variant4"""
# # 4. Forming a new list

# a = [random.randint(1, 100) for _ in range(2 * n)]
# print(f"\nInitial list a (2n elements): {a}")

# b = []
# for i in range(n):
#     b.append(a[i])
#     b.append(a[i + n])

# print(f"\nNew list b = [a1, an+1, a2, an+2, …, an, a2n]: \n{b}")

"""variant19"""
n = int(input("Enter numbers n: "))
a = [random.randint(0, 50) for _ in range(2 * n)]
print(f"Initial list a: {a}")

x = a[::2] # Elements with odd index.
y = a[1::2] # Elements with even index.

print(f"List x (a1, a3, a5, ...): {x}")
print(f"List y (a2, a4, a6, ...): {y}")



"""task2"""
n = len(input("Enter name: "))
m = len(input("Enter lastname: "))

print(f"Size matrix: {m} x {n}")


"""variant4"""
# matrix = [[random.randint(-10, 10) for _ in range(n)] for _ in range(m)]

# print(f"\nMatrix (b) with elements from -10 to 10:")
# for row in matrix:
#     print(row)
    
# if n != m:
#     print("\nMatrix is not square, it is impossible to check symmetry.")
# else: 
#     symmetric = True 
#     for i in range(n):
#         for j in range(n):
#             if matrix[i][j] != matrix[j][i]:
#                 symmetric = False
#                 break
#             if not symmetric:
#                 break
        
#     if symmetric:
#         print("\nMatrix symmetric relative to the main diagonal.")
#     else: 
#         print("\nMatrix not symmetric relative to the main diagonal.")
        

"""variant19"""
matrix = [[round(random.uniform(-10, 10), 2) for _ in range(n)] for _ in range(m)]
print("\nInitial matrix (d) with elements form -10 to 10")
for row in matrix:
    print(row)
    

if n != m:
    print("\nMatrix is not square, the operation was performed only on existing diagonal positions.")
min_dim = min(n, m)

for i in range(1, m):
    for j in range(0, min(i, n)):
        matrix[i][j] = 0
        
print("\nMatrix after replacing the elements exiting below the main diagonal with zero: ")
for row in matrix:
    print(row)