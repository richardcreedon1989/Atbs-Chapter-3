def collatz(number):
    if number % 2 == 0:
        print (number // 2)
        return number // 2
    elif number % 2==1:
        print (number *3 +1)
        return number *3 +1

print('Enter number here')

my_number=int(input())

while collatz(my_number) != 1:
    collatz(my_number)
    if my_number == 1:
        print(my_number)