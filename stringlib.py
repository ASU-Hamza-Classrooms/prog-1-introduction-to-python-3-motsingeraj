#!/bin/python3

#Add the following functions:
#
#reverseStr - takes as input a string and returns the reverse of it
#
#containsWord - takes as input two strings, containingStr and containedStr,
#and returns "Yes" if containedStr is anywhere within containingStr 
#and returns "No" otherwise
#
#isPalindrome - takes as input a string and returns "Yes" if it is
#palindrome and "No" otherwise  
#
#upperCaseStr - takes as input a string and returns the identical string
#with the characters 'a' ... 'z' changed to uppercase
#


def reverseStr(string):
    rev = ''
    for i in range(len(string)-1, -1, -1):
        rev = rev + string[i]
    return rev


def containsWord(containingStr, containedStr):
    if len(containedStr) <= len(containingStr):
        i = 0
        j = len(containedStr)
        while j <= len(containingStr):
            if containingStr[i:j] == containedStr:
                return 'Yes'
            i = i + 1
            j = j + 1
    return 'No'


def isPalindrome(string):
    i = 0
    j = len(string)-1
    while i < j:
        if string[i] != string[j]:
            return 'No'
        i = i + 1
        j = j - 1
    return 'Yes'


def upperCaseStr(string):
    return string.upper()

