"""
Level 2

Question: Write a program that computes the net amount of a bank account based a transaction log from console input. 
The transaction log format is shown as following: D 100 W 200

D means deposit while W means withdrawal. Suppose the following input is supplied to the program: D 300 D 300 W 200 D 100 Then, the output should be: 500

Hints: In case of input data being supplied to the question, it should be assumed to be a console input.

Solution:
"""
result = 0
ip_ls = [c for c in input("Enter the transaction log: ").split(" ")]

for i in range(0, len(ip_ls)):
    if ip_ls[i] == "D":
        result +=int(ip_ls[i+1])
    elif ip_ls[i] == "W":
        result -=int(ip_ls[i+1])
    else:
        pass
print(result)