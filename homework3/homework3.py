# Print Functions

def say_goodbye(name):
    print("Goodbye,", name)

def circle_area(radius):
    pi = 3.14
    print(pi * radius ** 2)



# Return Functions

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b


# Conditionals 

def temp_range(readings):
    return (min(readings), max(readings))


def is_weekend(day):
    # Monday = 1, ..., Sunday = 7
    return day == 6 or day == 7

def fuel_efficiency(distance, fuel):
    return distance / fuel



def secret_code(number):
    last_digit = number % 10
    remaining  = number // 10
    shift = 10 ** len(str(remaining))

    return last_digit * shift + remaining



# --- Loops ---

def power(x, y):
    result = 1
    for _ in range(y):
        result *= x
    return result


def find_min_for(numbers):
    smallest = numbers[0]
    for num in numbers:
        if num < smallest:
            smallest = num

    return smallest

def find_max_for(numbers):
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
    return largest



def find_min_while(numbers):
    smallest = numbers[0]
    i = 0
    while i < len(numbers):
        if numbers[i] < smallest:
            smallest = numbers[i]
        i += 1
    return smallest




def find_max_while(numbers):
    largest = numbers[0]
    i = 0

    while i < len(numbers):
        if numbers[i] > largest:
            largest = numbers[i]
        i += 1
    return largest



def digit_sum(number):
    total = 0
    while number > 0:
        total += number % 10
        number //= 10

    return total



# Run Script

x = 2
y = 3
result = power(x, y)
print(f"The result of Oski Stole Your Power (6.1) with x = {x} and y = {y} is {result}.")
