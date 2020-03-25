def collatz(number):
    #Even numbers
    if number % 2 == 0:
        return number // 2
    #Odd numbers
    elif number % 2 == 1:
        return 3 * number + 1
    print("After collatz %s" % number)
number = int(input())

while number != 1:
    number = collatz(number)
    print(number)