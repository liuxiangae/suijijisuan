import random
#定义一个二维列表，用于存储数据
a = [[], [], [], []]
result = []
flag = 0

#打开文件
file = open("data.txt", "r")

#将数据从文件中读入到列表
while True:
    context = file.readline()
    k = context.split(" ")
    if len(context) == 0:
        break

    if int(k[0]) == 1:
        a[0].append(int(k[1]))

    elif int(k[0]) == 2:
        a[1].append(int(k[1]))

    elif int(k[0]) == 3:
        a[2].append(int(k[1]))

    elif int(k[0]) == 4:
        a[3].append(int(k[1]))
count1 = 0


#打印数据
print("a[0] is ")
print(a[0])
print("\na[1] is ")
print(a[1])
print("\na[2] is ")
print(a[2])
print("\na[3] is\n ")
print(a[3])

#利用多重循环来判断集合之间的相似度
for i in range(0, 3):
    for j in range(i+1, 4):
        for num_1 in a[i]:
            for num_2 in a[j]:
                if num_1 == num_2:
                    count1 = count1 + 1
        print("\nthe sim of a[{}] and a[{}] is {}".format(i,j,float(count1/(len(a[i])+len(a[j])-count1))))

        count1 = 0



#we will use the hash function to caculate the sim

m = [1, 2, 3, 4, 5, 6, 7, 8, 9]
count2 = 0
index1 = -1
index2 = -1
index = 0
print(a[1])
print(a[2])
for k in range(0, 1000):
    random.shuffle(m)
    print(m)
    for num_m in m:
        if num_m in a[1]:
            index1 = index
            print("tset1")
            print(index1)
        if num_m in a[2]:
            index2 = index
            print("test2")
            print(index2)
        index = index + 1
        if index1 == index2 and index1 != -1 :
            count2 = count2 + 1
            print(count2)
            break
        else:
            index1 = -1
            index2 = -1
            break


print(count2/1000)
