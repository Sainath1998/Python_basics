def palindrome(a):
    
    mid = (len(a)-1)//2     #you can remove the -1 or you add <= sign in line 21 
    start = 0                #so that you can compare the middle elements also.
    last = len(a)-1
    flag = 0
    while(start<=mid):
        if a[start] == a[last]:
            start = start+1
            last = last-1
        else:
            flag = 1
            break
    if flag == 1:
        print('not a palindrom')
    else:
        print('its a palindrome')

a = input('enter a string')
palindrome(a)