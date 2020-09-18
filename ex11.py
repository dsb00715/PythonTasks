"""
Question: Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check whether they are divisible by 5 or not. 
The numbers that are divisible by 5 are to be printed in a comma separated sequence. 
Example: 0100,0011,1010,1001 Then the output should be: 1010 Notes: Assume the data is input by console.

Hints: In case of input data being supplied to the question, it should be assumed to be a console input.

"""

# Solution 1:

ip_list = [int(v, 2) for v in input("Enter numbers in binary sequence:").split(",")]

final_list = [bin(v) for v in ip_list if (v % 5 == 0)]

print(",".join(v[2:] for v in final_list))

# Solution 2:
'''
final_list = []
values = [x for x in input().split(",")]
for v in values:
    intv = int(v, 2)
    if not intv%5:
        final_list.append(v)

print(",".join(final_list))'''