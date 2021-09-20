def FizzBuzz(n):
    if (n % 3==0) and (n % 5 ==0):
        return('FizzBuzz')
    if (n % 3 == 0):
        return('Fizz')
    if ( n % 5 ==0):
        return('Buzz')

print(FizzBuzz(3))
print(FizzBuzz(5))
print(FizzBuzz(15))