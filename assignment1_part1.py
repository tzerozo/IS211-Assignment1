#!/usr/bin/env python
# _*_ coding: utf-8 _*_

#week1 assignment1

def listDivide (numbers, divide = 2):
    """Functions and Exceptions: divide items in a list"""
    """
    Args:
        numbers(list): list of int
        divide=2 (int): number to divide by

    Returns:
        int : the number of elements in the list divisible by divisor.

    Examples:
         listDivide ([1,2,3,4,5])
         2
    """
    divby2 = 0
    for item in numbers:
        if item % divide == 0:
            divby2 += 1
    return divby2

class ListDivideException(Exception):
    """Tow lines of class code"""
    pass

def testListDivide():
    """To test and find out about exceptions"""

    if listDivide ([1,2,3,4,5]) != 2:
        raise ListDivideException
    elif listDivide ([2,4,6,8,10]) !=5:
        raise ListDivideException
    elif listDivide ([30,54,63,98,100], 10) != 2:
        raise ListDivideException
    elif listDivide ([]) != 0:
        raise ListDivideException
    elif listDivide ([1,2,3,4,5], 1) != 5:
        raise ListDivideException

if __name__ == "__main__":
    testListDivide()