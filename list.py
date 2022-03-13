list = [12,32,432,6,3234,123,523,123]
size = len(list)
mid = size/2
i=0
print(list[::-1])
while(size>mid):
    temp = list[i]
    list[i]=list[size-1]
    list[size-1]=temp
    i=i+1
    size = size -1
print(list)