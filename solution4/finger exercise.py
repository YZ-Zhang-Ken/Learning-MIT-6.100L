N = int(input("Enter a positive integer: "))
is_perfect_cube = False
for i in range(1,N+1):
    if i**3 == N:
        is_perfect_cube = True
if is_perfect_cube:
    print(f"{N} is a perfect cube")
else:
    print("error")