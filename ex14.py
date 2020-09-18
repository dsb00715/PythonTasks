'''
Level 2

Question: Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters. 
Suppose the following input is supplied to the program: Hello world! Then, the output should be: UPPER CASE 1 LOWER CASE 9

Hints: In case of input data being supplied to the question, it should be assumed to be a console input.

Solution:
'''

ip_sen = input("ENter Sentence:")

upper = sum(c.isupper() for c in ip_sen)
lower = sum(c.islower() for c in ip_sen)

print(f"UPPER CASE: {upper}, LOWER CASE: {lower}")
