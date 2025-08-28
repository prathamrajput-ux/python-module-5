'''ask 1: Read a File and Handle Errors
Problem Statement:  Write a Python program that:
1.   Opens and reads a text file named sample.txt.
2.   Prints its content line by line.
3.   Handles errors gracefully if the file does not exist.
'''
# Solution 1 :
try :
    a = open('sample.txt','r')
    b = a.read()


# Solution 2 :
    print(b)

# Solution #
except FileExistsError :
    print("Error : The file 'sample.txt' was not found")