
'''#递归调用fbib函数计算斐波那契数列，计算前50个数所用时间较长
import time
def fib1(n):
    if n in (1, 2):
        return 1
    return fib1(n - 1) + fib1(n - 2)

start = time.time()

for i in range(1, 51):
    print(fib1(i))
end = time.time()
print("Time taken:", end - start)#Time taken: 5008.847773313522
'''
def fib2(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a
import time
start = time.time()
for i in range(1, 51):
    print(fib2(i))
end = time.time()
print("Time taken:", end - start)#Time taken: 0.003270864486694336


from functools import lru_cache

start = time.time()
@lru_cache()
def fib1(n):
    if n in (1, 2):
        return 1
    return fib1(n - 1) + fib1(n - 2)


for i in range(1, 51):
    print(i, fib1(i))
end = time.time()
print("Time taken with lru_cache:", end - start)#Time taken with lru_cache：0.003183603286743164