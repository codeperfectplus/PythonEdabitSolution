""" Create a function that returns Burp with num "r"s in it.

Examples
long_burp(3) ➞ "Burrrp"

long_burp(5) ➞ "Burrrrrp"

long_burp(9) ➞ "Burrrrrrrrrp" """

def long_burp(n):
    print('Bu'+'r'*n +'p')

long_burp(9)