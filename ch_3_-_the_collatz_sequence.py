def collatz(num):
    if num % 2 == 0:
        num = num//2
    else:
        num = (num * 3) + 1
    print(num)
    return(num)

print("Enter number:")
num = int(input())
while num != 1:
    num = collatz(num)
