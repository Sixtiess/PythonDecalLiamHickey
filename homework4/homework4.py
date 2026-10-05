foods = ["pizza", "sushi", "tacos", "pasta", "burgers"]

print(foods[1])
print(foods[-1])


foods.append("ramen")
foods.insert(0, "apple")
del foods[2]
print(len(foods))

for food in foods:

    print(food.upper())

firstandlast = [foods[0], foods[-1]]
print(firstandlast)


if "potato" in foods:
    print("A potato!")
else:
    print("No potato!")





numbers = list(range(21))

def get_first_15(numbers):
    return numbers[:15]


def get_every_5th(l):
    return l[::5]

def reverse_and_stride(l):

    return l[::-1][::3]

step1 = get_first_15(numbers)

step2 = get_every_5th(step1)

step3 = reverse_and_stride(step2),


print(step1, step2, step3)



nested = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(nested[2])
print(nested[1][1])
nested.append([10, 11, 12])


def sum_nested(rows):
    total = 0
    for row in rows:
        for num in row:
            total += num

    return total

print(sum_nested(nested))



def make_grid():
    grid = []
    count = 1
    for _ in range(5):
        row = []
        for _ in range(5):
            row.append(count)
            count += 1

        grid.append(row)
    return grid


def replace_multiples_of_3(grid):
    for row in grid:
        for i in range(len(row)):
            if row[i] % 3 == 0:
                row[i] = "?"
    return grid

def sum_without_marks(grid):
    total = 0

    for row in grid:
        for item in row:
            if item != "?":
                total += item
    return total


grid = make_grid()
marked_grid  = replace_multiples_of_3(grid)
grid_sum = sum_without_marks(marked_grid)
print(marked_grid)
print(grid_sum)




ages = {
    "Katie": 30,
    "Mariam": 42,
    "Safia": 25,
    "Mira": 48
}

print(ages["Katie"])
ages["Mira"] = 100

ages["Milana"] = 52
del ages["Mariam"]

for name in ages:
    print(name, ages[name])




print(reverse_and_stride(get_every_5th(get_first_15(list(range(21))))))




"""
Errors:

1)
"NameError: name 'get_first15' is not defined"
I originally called get_first15(numbers) when the function is named get_first_15.
I fixed it by adding the missing underscore so the call matched the definition.

2)
"TypeError: unsupported operand type(s) for +=: 'int' and 'str'"
I originally added the 5x5 list without skipping the "?" entries, so the expression total += item
tried to add a string to a number which isnt allowed. I fixed it by checking item != "?" first.

3)
"IndexError: list index out of range"
I originally printed nested[3] for the third row, forgetting that indexing starts at 0.
I fixed it by using nested[2].
"""
