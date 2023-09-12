# How to solve a problem:

#     -Figure out wher the input and its type are / string.  list
#     -Set up a function
#     -Figure out what the output and its type are /integer.  It is a count of the vowels  set counter to 0
#     -Gather your Knowledge
#     -Gathers your contraints (Not Always Necessary)
#     -Determine a Logical way to solve the problem /  search the list, return the vowels
#      -Write each step out in English / 
#       -Write each step out in Python-esse (sudo-code)
#       -Invoke and Test your function

"""
Return the number (count) of vowels in the given string.

We will consider a, e, i, o, u as vowels for this Kata (but not y).

The input string will only consist of lower case letters and/or spaces.

"""
def get_count(sentence: str) -> int:
    vowels = "aeiou"                    #constant time O(1)
    count = 0                           # constant time                      
    for v in sentence:                  # Runs once for every character O(n)
        if v in vowels:                 #O(n) -bc it's in the loop?otherwise, 5 vowels for a length is constant.
            count +=1                   # O(n) -bc of the surrounding loop

    return count

test = "This is a test with a few vowels...to check this out."
print(get_count(test))