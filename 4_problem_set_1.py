
# # **Python Practice Problems (No Code Included)

# **Directions:** Solve each problem by writing your own Python code. Show outputs where required.

list1=list(range(1,11))
print(list)
for i in list1:
    print(1)
 #ii doesnt mean anything its just a place holder# ### **Problem 1: Print Numbers 1 to 10

# Write a program that prints the numbers from **1 to 10**, each on a new line.



# ### **Problem 2: Sum of Numbers

# Ask the user for a number **n**, then calculate and display the **sum of all numbers from 1 to n**.
n= int(input("Enter a num : "))
begnining=0
for i in range(1, n+1): #plus one to include the actual number
    begnining += i #total = total + i new value
print ("the sum of 1 to " , n, "is", begnining) 
# ### **Problem 3: Factorial Calculator

# Ask the user for a number **n**, then calculate the **factorial** of that number.

# *(Example: factorial of 5 is 120)
for i in range(5):
    print(i + 1)


def factorial(n):
    factorial= 1 #bcs mulitplying and 0 factorial eqal 1

    for i in range(n):
        factorial*= i+1


    return(factorial)

print(factorial (4)) # 4*3 *2*1

# ### **Problem 4: Count Vowels**

# Ask the user for a string. Count and print how many **vowels (a, e, i, o, u)** are in the string.


# ### **Problem 5: Print Even Numbers**
q= int(input("enter a num: "))
list2 = list(range(2, q))
for x in list2:
    if x % 2 == 0:
        print("This is even")
    else:
        print("This is not even")
# Ask the user for a number **n**, then print all **even numbers** from 2 up to n.



# ### **Problem 6: Reverse a String**

# Ask the user for a string, then print the string **backwards**.



# ### **Problem 7: Multiplication Table**

# Ask the user for a number **n**, then print the **multiplication table** for n from
# n × 1 up to n × 10.



# ### **Problem 8: Count Occurrences**

# Ask the user for **two strings**, a and b.
# Determine how many times **string b appears inside string a**.



# ### **Problem 9: Fibonacci Sequence**

# Ask the user for a number **n**, then print the first **n numbers** of the Fibonacci sequence.



# ### **Problem 10: Pattern Printing**

# Ask the user for a number **n**, then print a pattern of stars where the first row has 1 star, the second has 2, and so on until row n.

# *(Example for n = 4)*
# *
# **
# ***
# ****



# If you want, I can also turn this into a **Google Doc**, **worksheet**, **PDF**, or **Canvas/Schoology assignment format**.
