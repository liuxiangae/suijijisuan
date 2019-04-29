import random

data = [[]]
file = open("data.txt", "r")
temp = 1
i = 0
count1 = 0
while True:
    context = file.readline()
    k = context.split(" ")
   # print(k)
    if k[0] == "":
        break
    else:
       if int(k[0]) == temp:
           data[i].append(int(k[1]))
       else:
          # print(data)
           i = i+1
           temp = int(k[0])
           data.extend([[int(k[1])]])

max1 = max(data[1])
max2 = max(data[2])
max = max(max1, max2)
m=[]
for i in range(0,max+1):
    m.append(i)
print(m)
print(data[1])
print(data[2])
count2 = 0
index1 = -1
index2 = -1
index = 0
for k in range(0, 10000):
    random.shuffle(m)
    for num_m in m:
        if num_m in data[1]:
            index1 = index
        if num_m in data[2]:
            index2 = index
        index = index + 1
        if index1 == index2 and index1 != -1 :
            count2 = count2 + 1
            break
        else:
            index1 = -1
            index2 = -1
            break

print(count2/10000)