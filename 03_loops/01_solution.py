n = int(input("Enter length of the array: "))
sum_even = 0

for i in range(1,n+1):
    if i % 2 == 0:
        sum_even += i

print(sum_even)
