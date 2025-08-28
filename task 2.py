'''Problem Statement: Write a Python program that:
1.   Takes user input and writes it to a file named output.txt.
2.   Appends additional data to the same file.
3.   Reads and displays the final content of the file
'''

# Solution 1 :

a = input("Enter text to write to the file  : ")
b = open('output.txt','w')
c= b.write(a +  "\n")
b.close()


#  Solution 2 :
d = open('output.txt','a')
e= d.write('Learning file handling in python')
d.close()


# Solution 3 :
f = open('output.txt','r')
g = f.read()
print(g)
f.close()