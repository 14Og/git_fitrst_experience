from functools import reduce
print("Hello git!")


def sum(*nums):
    a  = [i for i in nums]
    f = reduce(lambda x, y: x + y, a)

    print(f)





sum(1, 2, 3, 4)


