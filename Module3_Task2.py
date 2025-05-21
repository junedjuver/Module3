a=int(input('Enter first number: '))
c=a
b=int(input('Enter second number: '))
for i in range(a,b+1):
    a=a+i
d=a-c
print('The sum of numbers from 'f'{c} to 'f'{b} is {d}.')