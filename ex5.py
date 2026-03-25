# Exercise 5 - Fizz Buzz

def fizz_buzz(up_to):
    res = ''

    for n in range(1, int(up_to) + 1):
        if n % (3 * 5) == 0:
            res += 'FizzBuzz '
        elif n % 3 == 0:
            res += 'Fizz '
        elif n % 5 == 0:
            res += 'Buzz '
        else:
            res += f'{n} '

    return res.rstrip()


assert fizz_buzz(
    35) == '1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 FizzBuzz 16 17 Fizz 19 Buzz Fizz 22 23 Fizz Buzz 26 Fizz 28 29 FizzBuzz 31 32 Fizz 34 Buzz'
