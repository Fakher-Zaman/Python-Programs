# ---> By Using Generators
# def mygen():
#     yield 1
#     yield 2
#     yield 3
# x = mygen()
# print(x.__next__())
# print(x.__next__())
# print(x.__next__())

# ---> Normal Way
# print("Even values:")
# def mygen(n):
#     a = 0
#     while a < n:
#         if a % 2 == 0:
#             yield a
#         a += 1
# x = mygen(15)
# for i in x:
#     print(i)

# ---> By using Generators
print("Fibonacci Sequence:")
def fibo(n):
    a, b = 0, 1

    while a < n:
        yield a
        a, b = b, b+a
x = fibo(10)
for i in x:
    print(i)