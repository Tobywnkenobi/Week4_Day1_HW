# How to solve a problem:

#     -Figure out wher the input and its type are
#     -Set up a function
#     -Figure out what the output and its type are
#     -Gather your Knowledge
#     -Gathers your contraints (Not Always Necessary)
#     -Determine a Logical way to solve the problem
#      -Write each step out in English
#       -Write each step out in Python-esse (sudo-code)
#       -Invoke and Test your function
"""
Task:

Given two integers a and b, which can be positive or negative, find the sum of all the integers between and including them and return it. If the two numbers are equal return a or b.

Note: a and b are not ordered!

Examples (a, b) --> output (explanation)
(1, 0) --> 1 (1 + 0 = 1)
(1, 2) --> 3 (1 + 2 = 3)
(0, 1) --> 1 (0 + 1 = 1)
(1, 1) --> 1 (1 since both are same)
(-1, 0) --> -1 (-1 + 0 = -1)
(-1, 2) --> 2 (-1 + 0 + 1 + 2 = 2)
Your function should only return a number, not the explanation about how you get that number.
"""
def get_sum(a: int,b: int) -> int:
    lower = min(a, b)                       # - and below, contant.  only comparing two variables  O(d)
    upper = max(a, b)                          #same
    total = 0                                       #constant O(1)
    while lower <= upper:                       #    O(n)
        total += lower                          #O(n)
        lower += 1                              #0(1)
    return total


