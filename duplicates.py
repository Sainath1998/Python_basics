def remove_duplicates(userlist):
    res = []
    testres = userlist
    for i in testres :
        if i not in res:
            res.append(i)
    return res

userlist = input('enter a string \n')
userlist = userlist.split()
print(userlist)
for i in range(0,len(userlist)):
    userlist[i] = int(userlist[i])
print(userlist)
print('after removing duplicate items in the given list')
print(remove_duplicates(userlist))