print("Hey there, welcome to FizzBuzz!")

count = int(input("Please enter a number from 1 to 100: "))
count = int(count)

for x in range(1, count + 1):
    if x % 15 == 0:
        print("FizzBuzz")
    elif x % 3 == 0:
        print("Fizz")
    elif x % 5 == 0:
        print("Buzz")
    else:
        print(x)
