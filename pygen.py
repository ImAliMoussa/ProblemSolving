# use this to create long test cases by running this and redirecting output to a file
# example python3 pygen.py > outputfile
# then when you've compiled your program, redirect the output file to your compiled program
# example : 
# ./program < outputfile

# example -> created a very long linked list here by printing edges
n = int(2e4)
print(1)
print(n)
for i in range(2, n + 1):
    print(i - 1, i)
