"""
All data is made up of 0's and 1's known as bits.  Witwise operators allow us to perform bit-related operations on values

&      Bitwise AND  In-fix
|      Bitwise OR   In-fix
^      Bitwise XOR  In-fix
tilde   Bitwise NOT Prefix
<<      Shift Bits Left In-fix
>>      Shift Bits Right    In-fix
"""

num1 = 10 # Binary value = 01010
num2 = 20 # Binary value = 10100

print(num1 & num2) # 0000
print(num1 | num2) # 1110
print(num1 ^ num2) # 1110
print(num1 << 3) # 0010


# This gave me a basic understanding of what bitwise operators are, but I still don't understand when I'd use them