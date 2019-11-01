#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 00:09:57 2019

@author: randou
"""

# =============================================================================
# EASY
# =============================================================================
 
# 1. Two Sum
class Solution1:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for index, num in enumerate(nums):
            if ((target - num) in nums) and (nums.index(target-num)!=index):
                return [index, nums.index(target-num)]

# 7. Reverse Integer
class Solution7:
    def reverse(self, x: int) -> int:
        if x<-2**31 or x>(2**31-1):
            return 0
        elif x<0:
            if -int(str(abs(x))[::-1]) in range(-2**31, 2**31-1):
                return -int(str(abs(x))[::-1])
            else:
                return 0
        elif x>=0:
            if int(str(abs(x))[::-1]) in range(-2**31, 2**31-1):
                return int(str(abs(x))[::-1])
            else:
                return 0

# 9. Palindrome Number
class Solution9:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        else:
            if sum([str(x)[i]!=str(x)[-(i+1)] for i in range(len(str(x))//2)]) == 0:
                return True
            else: return False

# 13. Roman to Integer
class Solution13:
    def romanToInt(self, s: str) -> int:
        symbol_order ={'I':1, 'V':2, 'X':3, 'L':4, 'C':5, 'D':6, 'M':7}
        symbol_value ={'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        sum_list = []
        for index,letter in enumerate(s):
            if index != len(s)-1:
                if symbol_order[letter]>=symbol_order[s[index+1]]:
                    sum_list += [symbol_value[letter]]
                else: sum_list += [-symbol_value[letter]]
            else: sum_list += [symbol_value[letter]]
        return sum(sum_list)

# 14. Longest Common Prefix
class Solution14:
    def longestCommonPrefix(self, strs) -> str:
        if not strs:
            return ""
        min_length = min([len(word) for word in strs])
        common_prefix = []
        for i in range(min_length):
            letters = set([word[i] for word in strs])
            if len(letters)==1:
                common_prefix += list(letters)
            else: break
        return ''.join(common_prefix)

# 20. Valid Parentheses
class Solution20:
    def isValid(self, s: str) -> bool:
        stack = []
        dict = {"]":"[", "}":"{", ")":"("}
        for char in s: 
            if char in dict.values():
                stack.append(char)
            elif char in dict.keys():
                if stack == [] or dict[char] != stack.pop():
                    return False
            else:
                return False
        return stack == []

# 26. Remove Duplicates from Sorted Array
class Solution26:
    def removeDuplicates(self, nums: list[int]) -> int:
        nums[:len(set(nums))] = list(sorted(set(nums)))
        return len(set(nums))

# 27. Remove Element
class Solution27:
    def removeElement(self, nums: list, val: int) -> int:
        length = 0
        for num in nums:
            if num==val:
                length += 1
        for i in range(length):
            nums.remove(val)

# 28. Implement strStr()
class Solution28:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle not in haystack:
            return -1
        else: 
            return haystack.find(needle)

# 35. Search Insert Position
class Solution35:
    def searchInsert(self, nums: list[int], target: int) -> int:
        position = 0
        for index,num in enumerate(nums):
            if num < target:
                position = index + 1
        return position         

# 38. Count and Say
class Solution38:
    def countAndSay(self, n: int) -> str:
        count_say = {1:'1', 2:'11'}
        for i in range(3,31):
            previous = count_say[i-1]
            count = [previous[0]]
            new = []
            for index in range(1,len(previous)):
                if previous[index]==previous[index-1]:
                    count += [previous[index]]
                    if index==len(previous)-1:
                        new.extend([str(len(count)), previous[index]])
                else:
                    new.extend([str(len(count)), previous[index-1]])
                    count = [previous[index]]
                    if index==len(previous)-1:
                        new.extend([str(len(count)), previous[index]])
            count_say[i] = ''.join(new)
        return count_say[n]

# 58. Length of Last Word
class Solution58:
    def lengthOfLastWord(self, s: str) -> int:
        if not s or not s.split():
            return 0
        else:
            return len(s.split()[-1])

# 66. Plus One
class Solutio66:
    def plusOne(self, digits: list[int]) -> list[int]:
        if digits[-1] != 9:
            digits[-1] = digits[-1] + 1
        else:
            count_nine = 0
            for i in digits[::-1]:
                if i == 9:
                    count_nine += 1
                else:
                    break
            if count_nine == len(digits):
                digits = [1] + [0]*count_nine
            else:
                digits[-(count_nine+1):] = [digits[-(count_nine+1)]+1] + [0]*count_nine
        return digits

# 67. Add Binary
class Solution67:
    def addBinary(self, a: str, b: str) -> str:
        a_base10 = int(a, 2)
        b_base10 = int(b, 2)
        sum_base10 = a_base10 + b_base10
        sum_base2 = str(bin(sum_base10))
        return sum_base2[2:]

# 69. Sqrt(x)
class Solution69:
    def mySqrt(self, x: int) -> int:
        return int(x**0.5)

# 70. Climbing Stairs
class Solution70:
    def climbStairs(self, n: int) -> int:
        a = 1
        b = 1
        for i in range(n):
            a, b = b, a
            a += b
        return b



# =============================================================================
# MEDIUM
# =============================================================================






# =============================================================================
# HARD
# =============================================================================




