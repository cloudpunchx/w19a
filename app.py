# print Fizz if divisible by 3
# print Buzz if divisible by 5
# print FizzBuzz if divisible by both 3 and 5

def fizz_buzz(numbers):
    for i in range(len(numbers)):
        if (numbers[i] % 3 == 0 and numbers[i] % 5 == 0):
            print("FizzBuzz")
        elif (numbers[i] % 5 == 0):
            print("Buzz")
        elif (numbers[i] % 3 == 0 ):
            print("Fizz")
        else:
            print(numbers[i])

list_of_nums = [41, 52, 15, 99, 105, 66, 44, 88, 89, 100, 62, 55, 14, 1, 0, 2]

fizz_buzz(list_of_nums)