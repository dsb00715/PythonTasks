'''
Level 2

Question: Write a program that accepts a sentence and calculate the number of letters and digits. 
Suppose the following input is supplied to the program: hello world! 123 Then, the output should be: LETTERS 10 DIGITS 3

Hints: In case of input data being supplied to the question, it should be assumed to be a console input.
'''

ip_sen = input("Enter a sentence with word & digits:")

letters = sum(c.isalpha() for c in ip_sen)
digits = sum(c.isdigit() for c in ip_sen)

print(f"LETTERS:{letters}, DIGITS:{digits}")
