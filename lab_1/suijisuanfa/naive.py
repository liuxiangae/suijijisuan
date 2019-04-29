
data = [[1]]
file = open("linux_distinct.txt", "r")
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


for num_1 in data[1]:
    for num_2 in data[2]:
        if num_1 == num_2:
            count1 = count1 + 1

print("the a[1] is: {}".format(data[0]))
print("the a[2] is: {}".format(data[2]))
print("\nthe sim of a[{}] and a[{}] is {}".format(1,2,float(count1/(len(data[1])+len(data[2])-count1))))
