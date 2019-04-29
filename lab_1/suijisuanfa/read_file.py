def read():
    data = [[]]
    file = open("linux_distinct.txt", "r")
    temp = 1
    i = 0
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
                i = i + 1
                temp = int(k[0])
                data.extend([[int(k[1])]])
    return data

