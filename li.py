#palindrome
a = input('Enter the string to know whether its palindrome or not \n')
size = len(a)-1
i = 0
while(i < size/2):
    if a[i] == a[size] :
        print('yes the given string is palindrom')
        break
    else:
        print('no its no a palindrom')
        break
