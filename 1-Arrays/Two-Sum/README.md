#Two Sum
Platform: Leetcode
Difficulty: Easy
Topics: Arrays, Hash table...

#Understanding the problem:

Given an array of integers nums, i need to return the indices of two numbers so that they add up to the target provided

#Approach 1, Brute force:
A nested loop seems like the most straightforward solution here, go through each element and add it with every other element infront of it in the array checking if the sum is target each time
Time complexity: O(n^2)
Space Complexity: O(1)

#Approach 2, Optimal solution:
instead of checking every possible pair, we can use a hasmap: going through the loop, see if current value + another value = target, if no such other value exists yet in the hashmap, add the current value to said hashmap and continue
Time Complexity: O(n)
Space Complexity: O(n)
Key takeaways:
. Trading space complexity for time complexity is favorable when sufficient memory is available

References:
https://leetcode.com/problems/two-sum/description/