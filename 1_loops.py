# Example Practice:
# Given this list of fruits:
fruits = ["apple", "banana", "cherry", "date"]

# Challenge:
# Use a for loop to print each fruit on a new line.
print(fruits[0])
print(fruits[1])
print(fruits[2])
for fruit in fruits:
    print(fruit)
# i just worked with loops
print(len(fruits))

# Given a list of school subjects:
subjects = ["Math", "Science", "History", "Art"]
for subject in subjects:
    if subject == "History":
        break
    else:
        print((subject))


print(len(subjects))
# Challenge:
# Use a for loop and range to print each subject along with its index:
# Example output: "Subject 0: Math"
for index in range(len(subjects)) :
    print("Subject" + str(index) + ":" + subjects[index])

# Given:
numbers = [5, 10, 15, 20]

# Challenge:
# Use a for loop to add all the numbers and print the total.
#leave the 0 out of the loop so it just starts w it and adds to it

total = 0
for num in numbers:
    total += numbers
print("total: ", total)

new_num =list(range(1,61))

base = 0
for num in new_num:
    base += num
print("base", num)
 