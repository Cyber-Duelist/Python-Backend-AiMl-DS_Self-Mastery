"""Write a function isPalindrome that gets a string and returns true if the string is a palindrome, otherwise false.

A palindrome is a word or phrase that reads the same backward as forward."""

from stack import Stack


def isPalindrome(s):
    # Write code here
    st = Stack()
    for char in s:
        st.push(char)

    reversed_s = ""
    for _ in range(len(s)) :
        reversed_s += st.pop()   

    

    return s == reversed_s
print(isPalindrome("oppo"))
print(isPalindrome("vivo"))