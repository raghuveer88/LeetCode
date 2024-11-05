# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        # just do the binary search to find the picked element remeber her they have already
        # defined a function named guess you have to use that
        low = 1
        high = n
        while low <= high:
            mid = (low + high)//2
            result = guess(mid)
            if result == 0:
                return mid
            if result == -1:
                high = mid -1
            if result == 1:
                low = mid + 1
        