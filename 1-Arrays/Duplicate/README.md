#Contains Duplicate
Platform: Leetcode
Difficulty: Easy
Topics: Arrays, sets...

#Understanding the problem:
We must determine if an array contains at least one value that appears more than once

#Approach 1: Brute force

A nested loop, taking an element and checking if it equals each other element after it in the array.
Time Complexity: O(n^2)
Space Complexity: O(1)

#Approach 2: Optimal Solution:
implementing a set  is the most time efficient solution to check if an element has a duplicate in the array
The technique is to go through the array, checking if each element already exists in the set, if it does then we have a duplicate, if it doesnt, add it and go to the next element.
Time complexity: O(n)
Space Complexity: O(n)

#References:
https://leetcode.com/problems/contains-duplicate/description/