import datetime
def randomized_select(A, p, r, i):
    if p == r:
        return A[p]
    q = randomized_partition(A, p, r)
    k = q - p + 1
    if i == k:
        return A[q]
    elif i < k:
        return randomized_select(A, p, q - 1, i)
    else:
        return randomized_select(A, q + 1, r, i - k)


import random


def randomized_partition(A, p, r):
    i = random.randint(p, r)
    t = A[r]
    A[r] = A[i]
    A[i] = t
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] < x:
            i += 1
            t = A[i]
            A[i] = A[j]
            A[j] = t
    A[r] = A[i + 1]
    A[i + 1] = x
    return i + 1

A = []
with open('test.txt', 'r') as f:
    for i in range(0, 999999):
        A.append(f.readline())
f.close()
if __name__=='__main__':
   time1 = datetime.datetime.now()
   print(randomized_select(A,0,999998,555555))
   time2 = datetime.datetime.now()
   print("the time is :", (time2-time1).total_seconds(),'s')






