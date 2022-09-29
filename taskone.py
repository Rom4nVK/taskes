# Zadacha 14

# some_str = input()
# summ = 0
# for i in some_str:
#     if i != '.':
#         summ += int(i)
# print(summ)

# zadacha15
# fact = 1
# n = int(input())
# some_list = []
# for i in range(1, n + 1):
#     some_list.append(fact * i)
#     fact = fact * i
# print(some_list)

# n = int (input())
# summ = 0
# for i in range(1, n + 1):
#     summ += (1 + 1 / i) ** i
# print(summ)

# from random import *
# some_list = [randint(-10,10) for _ in range (randint(5,10))]
# print (some_list)
# shuffle(some_list)
# print(some_list)


# zadacha 16
import random
n = int(input())
a = []
for i in range(n):
    a.append(random.randint(-n, n))
print(a)
m = open ('f.txt', 'w')
len_m = random.randint(2, n)
for i in range (len_m):
    m.write(str(random.randint(0, n - 1)))
    m.write('\n')
m.close()
sum = 1
f = open ('f.txt', 'r')
for i in range(len_m):
    sum *= a[int(f.readline())]
print(sum)