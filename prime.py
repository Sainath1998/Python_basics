num = int(input('Enter a number \n'))
for i in range(2,num) :
    if(num % i == 0):
        print('not a prime')
        break

    else:
        print(' a prime')
        exit(0)
        
