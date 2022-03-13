# secon largest no. in the five list
def second_largest(b):
    j = 0
    largest = 0
    for j in range(0,size):
        if b[j]> largest:
            largest = b[j]
    print('the largest number is : ', largest)
    temp = largest
    largest = 0
    secondlargest = 0
    for k in range(0,size):
        if b[k]>largest and b[k] != temp:
            secondlargest = b[k]
            #k = k+1
    print('The second largest number is',secondlargest) 

a = input()
b = a.split()
print(b)
i = 0
size = len(b) 
for i in range(0,size):
    b[i] = int(b[i])
print(b)
print(second_largest(b))