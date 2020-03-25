def collatz(number):
    try:
     result = my_number
     if number % 2 == 0:
        print(result)
        return number // 2
     else:
        print(result)
        return number *3 +1
    except ValueError:
        print('Value Error')


my_number=int(input('Enter a number:'))

while collatz(my_number) != 1:
    my_number = collatz(my_number)
    if my_number == 1:
     print(my_number)


