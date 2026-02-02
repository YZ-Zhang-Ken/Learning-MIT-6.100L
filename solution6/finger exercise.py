N = int(input("Enter a integer within 0 and 1000: "))

high = 1000
low = 0
count = 0
epsilon = 0.01
answer = (high + low)/2

while(abs(answer-N) > epsilon):
    count += 1
    if answer > N:
        high = answer
    else:
        low = answer
    answer = int((high + low)/2)
print(f"count:{count}")
print(f"answer:{int(answer)}")