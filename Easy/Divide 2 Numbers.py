""" Create a function that divides a and b the equation would look like a / b

Examples
[12,6]➞ 2

[3,3] ➞ 1

[5,0] ➞ "Error"
Notes
Return error if it is dividing by 0"""
def divide(a,b):
    try:
        return a/b
    except:
        return "Error"