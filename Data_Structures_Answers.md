Add your answers to the questions below.

1. What is the runtime complexity of your ring buffer's `append` method?
   O(1) runtime because we're just assigning a value and incrementing a count
2. What is the space complexity of your ring buffer's `append` function?
   O(1) because the list is already in memory, we're just changing the value and changing the value of our self.current
3. What is the runtime complexity of your ring buffer's `get` method?
   O(n) is the worstcase runtime since we have to iterate through the list and make sure that the values have been assigned to something other than None
4. What is the space complexity of your ring buffer's `get` method?
   Worst-case would be O(n) because we are iterating over our list and returning a new list comprehension with the None values removed

5. What is the runtime complexity of the provided code in `names.py`?
   O(n^2) because we have a nested for loop that's iterating over one of the lists for each eleemnt in the other list.
6. What is the space complexity of the provided code in `names.py`?
   The absolute worst-case would be 3n because we're creating the two lists of 10k names and if they were all duplicates then we would be creating one more list of length n. (But we drop the constant and simplify that down to n)
7. What is the runtime complexity of your optimized code in `names.py`?
   O(n) because we first create our set, we then create our list to compare to the set, and then we iterate over the list which has length n.
8. What is the space complexity of your optimized code in `names.py`?
   O(n) for the same reasons as the space-complexity of the original names.py algorithm
