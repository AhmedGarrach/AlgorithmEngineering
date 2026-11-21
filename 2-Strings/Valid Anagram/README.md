#Valid Anagram

Platform: LeetCode,
Difficulty: Easy,
Topics: Strings, Hash maps frequency

#Understanding the problem:

Make sure that two strings have the exact same letters and the exact same frequency of each letter, for example: "anagram" and "nagaram"

#First Approach: using a set

Initially i thought of using a set to make sure that both strings have the exact same letters, but the issue here is a set doesn't keep track of the number of occurences of each element inside of it which let me to

#Approach 2 : Using a Hash map (Dict)

The trick is to loop through the first string, each time adding each letter into an empty hashmap with the occurence number of 1, if the letter already exists, add 1 to the occurence number.
Then go through the other string.

How do we compare? well we could use another Hashmap and compare those two, but to save space, we balance out the frequencies instead of comparing, we go through the second string using the same Hashmap and simply decrementing the occurence each time an element exists in the dictionary and the string

so at the end, the values of the hashmap should all be 0 if the strings are anagrams

TIme Complexity: O(n),
Space Complexity: O(k), k being the number of characters stored in the hasmap

Key takeaways:
-Hash maps are useful when encountering frequency problems