'''
Level 2

Question: Write a program, which will find all such numbers between 1000 and 3000 (both included) such that 
each digit of the number is an even number. The numbers obtained should be printed in a comma-separated sequence on a single line.

Hints: In case of input data being supplied to the question, it should be assumed to be a console input.

Solution:'''

values=[]

x,y = [int(r) for r in input().split(",")]

for n in range(x,y):
    s = str(n)
    if all(int(d) % 2 == 0 for d in s):
        values.append(s)

print(",".join(values))
