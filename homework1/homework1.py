# File: homework1.py

# --- Variables and Data Types ---

a = 10
print(a)
print(type(a)) # a is an integer, a whole number with no decimals

b = 1.5
print(b)
print(type(b)) # b is a float, a decimal number

c = 3j
print(c)
print(type(c)) # c is a complex number

d = "hello"
print(d)
print(type(d)) # d is a string

e = [1, 2, 3]
print(e)
print(type(e)) # e is a list

f = {"name": "Ellen", "favorite fruit": "strawberry"}
print(f)
print(type(f)) # f is a dictionary

g = (1, 2)
print(g)
print(type(g)) # g is a tuple

h = ["apple", "banana", "strawberry"]
print(h)
print(type(h)) # h is a list

i = True
print(i)
print(type(i)) # i is a boolean

j = None
print(j)
print(type(j)) # j is a NoneType

k = [True, "blue", 12]
print(k)
print(type(k)) # k is a list

l = str(14)
print(l)
print(type(l)) # l is a string

m = 1e4
print(m)
print(type(m)) # m is a float, defined by scientific notation e.g(1 x 10^4)

'''
1. How many different data types did you find?
a. 9 different data types

2. List all the data types you found.
a. int, float, complex, str, list, dict, tuple, bool, and NoneType

3. What variables have the same data types?
a. e, h, and k are all lists, d and l are strings, and b and m are both floats.

4. What was the data type of l? Why is it not an integer? What does str() do?
a. The data type of l is a string. str() converts what is passed to it into a string.

5. Look up one more data type not given above. Repeat the same procedure

'''
# 5
n = range(5)
print(n)
print(type(n)) # n is a range, which represents a sequence of numbers




print(10 > 9) # True, 10 is greater than 9
print(10 == 9) # False, 10 is not equal to 9
print(10 <= 9) # False, 10 is not less than or equal to 9
print(bool("abc")) # True, non-empty string is truthy
print(bool(123)) # True, non-zero integer is truthy
print(bool(["apple", "cherry", "banana"])) # True, non-empty list is truthy
            
print(bool(True)) # True (by definition)
print(bool(False)) # False (by definition)
print(bool(0)) # False, 0 is falsy
print(bool("")) # False, empty string is falsy
print(bool(" ")) # True, non-empty string with whitespace is truthy
print(bool(())) # False, empty tuple is falsy
print(bool([])) # False, empty list is falsy
print(bool({})) # False, empty dictionary is falsy

print(bool(True and False)) # False, and needs both sides to be true
print(bool(True and True)) # True, both sides are true
print(bool(False and False)) # False, neither side is true
print(bool(True or False)) # True, or only needs one side to be true
print(bool(True or True)) # True, at least one side is true
print(bool(False or False)) # False, neither side is true
print(bool(not(False))) # True, not flips False into True
print(bool(not(True))) # False, not flips True into False

'''
Questions:
1. What pattern do you notice about expressions returning True or False?
a. Comparisons and non-empty/non-zero values tend to return True, while empty values (0, "", (), [], {}) and false comparisons return False.

2. Which expression surprised you about its result?
a. bool(" ") surprised me, since it looks empty but it actually has a space in it, so it counts as a non-empty string and returns True.

3. Create an expression, not given above, that will return True. Why is it True?
a. print(7 > 3) returns True because 7 is greater than 3.

4. Create an expression, not given above, that will return False. Why is it False?
a. print(bool(0.0)) returns False because 0.0 is treated the same as 0, which is falsy.
'''
print(7 > 3) # True, 7 is greater than 3
print(bool(0.0)) # False, 0.0 is falsy just like 0





# --- Operators ---

# Arithmetic Operators
print(10 + 5) # 15, + performs addition
print(10 - 5) # 5, - performs subtraction
print(2 * 4) # 8, * performs multiplication
print(6 / 3) # 2.0, / performs division and always returns a float
print(5 % 2) # 1, % returns the remainder of the division
print(3 ** 2) # 9, ** raises a number to a power
print(15 // 2) # 7, // performs floor division and rounds down to a whole number

# Comparison Operators
print(5 == 2) # False, 5 is not equal to 2
print(10 != 10) # False, 10 is equal to 10, so "not equal" is false
print(2 < 5) # True, 2 is less than 5
print(12 > 5) # True, 12 is greater than 5
print(5 <= 6) # True, 5 is less than or equal to 6
print(1 >= 10) # False, 1 is not greater than or equal to 10

# Assignment Operators
x = 5
x += 5
print(x) # 10, += adds 5 to x and reassigns it
x -= 4
print(x) # 6, -= subtracts 4 from x and reassigns it
x *= 3
print(x) # 18, *= multiplies x by 3 and reassigns it

# Logical Operators
'''
1. What does the operator and do? Write an expression that results in True. Write an expression that results in False.
a. and returns True only when both sides are true.
print(True and True) # True
print(True and False) # False

2. What does the operator or do? Write an expression that results in True. Write an expression that results in False.
a. or returns True when at least one side is true.
print(True or False) # True
print(False or False) # False

3. What does the operator not do? Write an expression that results in True. Write an expression that results in False.
a. not flips a boolean to the opposite value.
print(not False) # True
print(not True) # False
'''
print(True and True) # True, both sides are true
print(True and False) # False, one side is false
print(True or False) # True, at least one side is true
print(False or False) # False, neither side is true
print(not False) # True, not flips False to True
print(not True) # False, not flips True to False

'''
More Questions:
1. What is the difference between / and //?
a. / always returns a float (decimal) result, while // rounds the result down to the nearest whole number.

2. What is the difference between % and //?
a. % gives the remainder left over from division, while // gives the whole number part of the division.

3. What operator would you use to calculate the remainder when dividing two numbers? Give an example.
a. The % operator. Example: print(10 % 3) gives 1.

4. How do assignment operators work?
a. They combine a math operation with assignment in one step, so x += 5 is the same as writing x = x + 5.
'''
print(10 % 3) # 1, the remainder of 10 divided by 3







# --- Strings ---
my_string = "hello"
print(my_string) # Prints: hello
print(my_string[0]) # h, indexing starts at 0
print(my_string[1]) # e
print(my_string[2]) # l
print(my_string[3]) # l
print(my_string[4]) # o
print(my_string[-1]) # o, negative indexing starts from the end of the string
print(my_string[1:3]) # el, slices starting at index 1 up to but not including index 3
print(my_string[0:5:2]) # hlo, slices from index 0 to 5, skipping every other character
print(len(my_string)) # 5, len() gives the length of the string
print(my_string + "goodbye") # hellogoodbye, + concatenates two strings together
print(7 * my_string) # hellohellohellohellohellohellohello, * repeats the string 7 times

'''
3.4.1 Questions:
1. Define the term slicing. For which of the manipulations did you slice your string?
a. Slicing means pulling out a portion of a string using a start, stop, and optional step index. I sliced my_string with my_string[1:3] and my_string[0:5:2].

2. Call the following, describe the result:
name = "Oski"
print("Hello, my name is", name)
a. This prints "Hello, my name is Oski". Using a comma in print() separates the arguments and automatically adds a space between them.

3. Call the following, describe the result.
name = "Oski"
print(f"Hello, my name is {name}")
a. This also prints "Hello, my name is Oski", but it uses an f-string to insert the variable directly into the string.

4. What is the difference between the two last print statements?
a. Both give the same output, but the comma version passes multiple separate arguments to print(), while the f-string version builds one single string with the variable embedded inside it. f-strings give more control over formatting.
'''
name = "Oski"
print("Hello, my name is", name)
print(f"Hello, my name is {name}")




# --- Terminal Commands ---
# cd
# Changes directories. Use it to move from one folder to another.
# e.g cd Desktop

# ls
# Lists the files and folders in the current directory.
# e.g: ls

# ls -a
# Lists all files and folders in the current directory, including hidden ones.
# e.g: ls -a

# mkdir
# Makes a new directory (folder).
# e.g: mkdir homework1

# cat
# Prints the contents of a file to the terminal.
# e.g: cat homework1.py

# pwd
# Prints the current working directory, showing your full file path.
# e.g: pwd

# cd ..
# Moves up one directory, into the parent folder.
# e.g: cd ..

# cd .
# Refers to the current directory. Doesn't actually move anywhere.
# e.g: cd .

# cd ~
# Moves to the home directory.
# e.g: cd ~

# cp
# Copies a file from one location to another.
# e.g: cp homework1.py homework1_copy.py

# mv
# Moves a file to a new location, or renames it.
# e.g: mv homework1.py homework1_folder/

# rm
# Removes (deletes) a file. Be careful, this is permanent!
# e.g: rm oldfile.py

# clear
# Clears the terminal screen.
# e.g: clear

# grep
# Searches for a pattern of text inside a file.
# e.g: grep "print" homework1.py

'''
Questions:
1. Look up 3 other commands not present. Define and explain how to use them on the command line.
a. touch - creates a new empty file. Example: touch newfile.py
   history - shows a list of commands you've previously run. Example: history
   man - opens the manual/help page for a command. Example: man ls

2. What is the difference between ls and ls -a?
a. ls only shows the regular visible files and folders, while ls -a also shows hidden files, which are files that start with a dot.

3. What is a hidden file?
a. A hidden file is a file whose name starts with a dot (.), so it doesn't show up in a normal ls listing.

4. Look up 3 other flags (e.g., -a was a flag for the ls command). Define and explain how to use them on the command line.
a. ls -l shows a detailed/long listing with permissions, size, and date modified. Example: ls -l
   rm -r removes a directory and everything inside it. Example: rm -r old_folder
   cp -r copies an entire directory and its contents. Example: cp -r folder1 folder2
'''