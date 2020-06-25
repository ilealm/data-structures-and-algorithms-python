# Left Join
Write a function that LEFT JOINs two hashmaps into a single data structure.
The first parameter is a hashmap that has word strings as keys, and a synonym of the key as values.
The second parameter is a hashmap that has word strings as keys, and antonyms of the key as values.
Combine the key and corresponding values (if they exist) into a new data structure according to LEFT JOIN logic.
LEFT JOIN means all the values in the first hashmap are returned, and if values exist in the “right” hashmap, they are appended to the result row. If no values exist in the right hashmap, then some flavor of NULL should be appended to the result row.
The returned data structure that holds the results is up to you. It doesn’t need to exactly match the output below, so long as it achieves the LEFT JOIN logic.
Avoid utilizing any of the library methods available to your language.

## Challenge
### Challenge 33: Left Join

challenges/left_join/left_join.py
GitHub Pull# 25

[Pull on GitHub](https://github.com/ilealm/data-structures-and-algorithms-python/pull/25)


## Approach & Efficiency
TIME: O(n); Because we need to traverse both hashtables
SPACE O(1): Because we need to create new structures for the database.

## Solution
Solution for lab 33

![My solution](/assets/left_join.jpg)

