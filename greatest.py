a = int(input('Enter a number \n'))
b = int(input('Enter a number \n'))
c = int(input('Enter a number \n'))
if(a > b and a > c):
    print('a is the greatest')
elif(b > a and b > c):
    print('b is greatest')
elif(c>a and c > b):
    print('c is the greatest')
else:
    print('none')