import  datetime
arr = []
with open('test.txt','r') as f:
    for i in range(0,999999):
        arr.append(f.readline())
f.close()



def QuickSort(arr,firstIndex,lastIndex):
    if firstIndex < lastIndex:
        divIndex = Partition(arr,firstIndex,lastIndex)
        QuickSort(arr,firstIndex,divIndex)
        QuickSort(arr,divIndex+1,lastIndex)
    else:
        return

def Partition(arr,firstIndex,lastIndex):
    i=firstIndex-1
    for j in range(firstIndex,lastIndex):
        if arr[j]<=arr[lastIndex]:
            i=i+1
            arr[i],arr[j]=arr[j],arr[i]
    arr[i+1],arr[lastIndex]=arr[lastIndex],arr[i+1]
    return i

#print("the inital arrr:\n",arr)
time1=datetime.datetime.now()
QuickSort(arr,0,len(arr)-1)
#print("the sort arr",arr)
print(arr[int(len(arr)/2)])
time2 = datetime.datetime.now()
print("the time is :", (time2-time1).total_seconds(),'s')


