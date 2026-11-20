#Best time to buy and sell stock

Platform: Leetcode,
Difficulty: Easy,
Topics: Arrays, sets...

#Understanding the problem:

We're given an array of prices of stocks, each index represents a day, We need to return the maximum profit possible,
the profit here represents the value of the day we solt - the value of the day we bought

#Approach 1: Brute force

A nested loop, loop 1 will contain the day of buying, the second loop, starts at (i+1) will be the selling day
each time we put the profit inside an array , then we find the maximum in that array

Time Complexity: O(n^2),
Space Complexity: O(n)

#Approach 2: Optimal solution

My initial thought was simply finding the smallest and biggest number in the array and subtracting them, but that's not applicable when the day we buy on (smallest) is after the day we sell on (biggest), and what if the smallest number is in the last day?
My simple fix is going through the array and keeping note of the lowest buying price each time(min_price), if the day after is bigger, subtract, and compare that result to a variable i called max_profit, if it is bigger, then that is the max_profit so far, until the end of the array

Time Complexity: O(n),
Space Complexity: O(1)