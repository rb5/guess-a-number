# guess a number
print('a number from 0 to 100 is envisioned')
import random
o = 'y'
while (o == 'y')or(o == 'yes'):
    number = random.randint(0,100)
    print('\nhow much you need to try to guess it? (enter the number of attempts)')
    k = int(input())
    a = -1
    i = 0
    while (number != a)and(i < k):
        i += 1
        print('attempt №%d:' % i)
        a = int(input())
        if (a == number):
            print('right, you won!')
            break
        elif (number < a):
            print(' number less than', a)
        elif (number > a):
            print(' number greater than', a)
    else:
        print('you lose. did not guess the number %d' % number)
    o = input('to start the game again? (y/n) ')