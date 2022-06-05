'''
Module's Description:
            module name: Stat
            modules description: A python module for statistics 
            module version: 1.0.0
            LICENSE: MIT
=================================================
Author's Description:
            Author: Promise Okoli
            Email: okoli4promise@gmail.com 
            github: https://www.github.com/Premerie/Stat
            Phone_No: +234 816 997 6046
            Date_created: 3 June 2022
=================================================
Features:
            - A simple API for statistics.
            - Very ligthweight and no external dependencies.
            - Excellent test coverage.
=================================================
Installation:
            pip install Stat
=================================================
USAGE:      
            lst = [72, 75, 80, 74, 78, 80, 70, 75, 68, 70, 75, 70]
            bsort(lst) # Return the lst sorted.
            smode(lst) # Returns the mode of lst.
            smean(lst) # Returns the mean of lst.
            smedian(lst) # Returns the median of lst.
            scount(lst, 72) # Returns the occurrence of 72 in lst.
            sdev(lst) # Returns the deviation of lst.
            smdev(lst) # Returns mean deviation of lst.
'''

from typing import Iterable, NewType

num = int, float
_Number = NewType("_Number", num)

__VERSION__ = "1.0.0"

__all__ = [
                "bsort", 
                "smean", 
                "smode", 
                "smedian", 
                "sdev",
                "smdev", 
                "scount"
                ]

def bsort(lst: Iterable[_Number]) -> Iterable[_Number]:
    '''
    It takes an iterable as a parameter and 
    return it sorted.
    >>> bsort([5, 2, 9, 3, 1, 0])
    [0, 1, 2, 3, 5, 9]
    >>> bsort([7, 3, 0, 6, 7])
    [0, 3, 6, 7, 7]
    >>> bsort([72, 75, 80, 74, 78, 80, 70, 75, 68, 70, 75, 70])
    [68, 70, 70, 70, 72, 74, 75, 75, 75, 78, 80, 80]
    '''
    ########Bubble sort algorithm#########
    length = len(lst)
    for i in range(0, length):
        swapped = False
        for j in range(0, length - 1 - i):
            if lst[j] > lst[j + 1]:
                (lst[j], lst[j + 1]) = (lst[j + 1], lst[j])
                swapped = True
        if not swapped:
            break
    return lst

def smean(lst: Iterable[_Number]) -> _Number:
    '''
    Takes an iterable as a parameter and returns
    the mean.
    >>> lst = [72, 75, 80, 74, 78, 80, 70, 75, 68, 70, 75, 70]
    >>> smean(lst)
    73.917
    >>> smean([5, 6, 9, 4])
    6.0
    '''
    sum_of_all = 0
    length = len(lst)
    for num in lst:
        sum_of_all += num
    mean = sum_of_all / length
    mean = round(mean, 3)
    return mean

def smedian(lst: Iterable[_Number]) -> _Number:
    '''
    Takes an iterable as a parameter and 
    returns the median.
    >>> lst = [72, 75, 80, 74, 78, 80, 70, 75, 68, 70, 75, 70]
    >>> smedian(lst)
    74.5
    >>> smedian([7, 9, 3, 5, 7, 3])
    6.0
    '''
    lst = bsort(lst)
    length = len(lst)
    if length % 2 != 0:
        mid = length // 2
        return lst[mid]
    mid = length // 2
    med = lst[mid - 1] + lst[mid]
    med /= 2
    return med

def scount(lst: Iterable[_Number], num: _Number) -> _Number:
    '''
    Takes an iterable and a number as a parameter. 
    The count function returns the occurrence of the 
    number in the iterable. 
    >>> lst = [72, 75, 80, 74, 78, 80, 70, 75, 68, 70, 75, 70]
    >>> scount(lst, 75)
    3
    >>> scount([7, 3, 8, 4], 3)
    1
    >>> scount([], 5)
    0
    >>> scount(lst, 80)
    2
    '''
    count = 0
    for n in lst:
        if n == num:
            count += 1
    return count

def smode(lst: Iterable[_Number]) -> _Number:
    '''
    Takes an iterable as a parameter and returns 
    the mode.
    >>> lst = [72, 75, 80, 74, 78, 80, 70, 75, 68, 70, 75, 70]
    >>> smode(lst)
    70
    >>> smode([7, 9, 3, 5, 7, 3])
    3
    '''
    counts = 0
    mode = None
    for nums in lst:
        amount = scount(lst, nums)
        if amount >= counts:
            counts = amount
            mode = nums
    return mode
    
def sdev(lst: Iterable[_Number]) -> _Number:
    '''
    Returns the deviation of the iterable
    given in the parameter.
    >>> lst = [72, 75, 80, 74, 78, 80, 70, 75, 68, 70, 75, 70]
    >>> sdev(lst)
    -1
    '''
    dev = 0
    mean = round(smean(lst))
    for num in lst:
        dev += num - mean
    return dev
    
def smdev(lst: Iterable[_Number]) -> _Number:
    '''
    Returns the mean deviation of the iterable
    given in the parameter.
    >>> lst = [72, 75, 80, 74, 78, 80, 70, 75, 68, 70, 75, 70]
    >>> smdev(lst)
    3.25
    '''
    mdev = 0     
    mean = round(smean(lst))      
    for num in lst:  
        mdev += abs(num - mean)
    mdev = round(mdev / len(lst), 3)
    return mdev
                
########### TEST CODE #############           
if __name__ == "__main__":
    import doctest
    doctest.testmod()
 
 #####################################################
 #####################################################
 ##                                                                                                                        ##     
 ##                ##               ##########         ##             ##########        ##
 ##         ##          ##                 ##                ## ##                    ##                  ##
 ##         ##                                ##              ##     ##                  ##                  ##
 ##                ##                         ##             ##       ##                 ##                  ##
 ##                      ##                   ##            ##         ##                ##                  ##
 ##        ##            ##                ##            ########               ##                  ##
 ##          ##         ##                 ##            ##          ##               ##                  ##
 ##                 ##                        ##            ##          ##               ##                  ##
 ##                                                                                                                         ##
 #####################################################      
 #####################################################     
  