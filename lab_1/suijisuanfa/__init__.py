import random
list1 = [1, 2, 3, 4]

file = open("data.txt", 'w+')
a = 1
while a <= 10:
    ptr = str(random.choice(list1)) + " " + str(random.randint(1, 10))
    file.write(ptr+"\n")
    a = a+1
file.close()