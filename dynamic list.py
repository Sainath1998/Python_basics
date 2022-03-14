x = []
k = int(input('Enter the numver of elements in the given list \n'))
for i in range(0,k):
    x.append(input())
print("Given list with strings : \n",x)
# using int
res = [int(i) for i in x]
# Result
print("The converted list with integers : \n",res)