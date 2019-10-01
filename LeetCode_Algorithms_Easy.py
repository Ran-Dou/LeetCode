#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 00:09:57 2019

@author: randou
"""

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        else:
            if sum([str(x)[i]!=str(x)[-(i+1)] for i in range(len(str(x))//2)]) == 0:
                return True
            else: return False
       
        
class Solution:
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


class Solution35:
    def removeElement(self, nums: list, val: int) -> int:
        length = 0
        for num in nums[::-1]:
            if num==val:
                length += 1
                nums.pop(num)
        return nums


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
    

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        max_list = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)+1):
                if sum(nums[i:j]) > max_sum:
                    max_sum = sum(nums[i:j])
                    max_list = nums[i:j]
        return max_sum


class Solution58:
    def lengthOfLastWord(self, s: str) -> int:
        if not s:
            return 0
        else:
            return len(s.split()[-1])


class Solution66:
    def plusOne(self, digits: list) -> list:
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


# 2019.09.25
# Medium
# Longest Substring Without Repeating Characters
class Solution3:
    def lengthOfLongestSubstring(self, s: str) -> int:
        strtolist = list(s)
        [y-x for x, y in zip(A[:-1], A[1:])]

# 2019.09.30
# Easy
# Add Binary
class Solution67:
    def addBinary(self, a: str, b: str) -> str:
        a_base10 = int(a, 2)
        b_base10 = int(b, 2)
        sum_base10 = a_base10 + b_base10
        sum_base2 = str(bin(sum_base10))
        return sum_base2[2:]

# Easy
# Sqrt(x)
class Solution69:
    def mySqrt(self, x: int) -> int:
        return int(x**0.5)

# Easy
# 







