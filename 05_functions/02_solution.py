def sum_all(*args):
    print(args)
    for i in args:
        print(i ** 2, end=" ")
    return sum(args)

print(sum_all(1,2,3))