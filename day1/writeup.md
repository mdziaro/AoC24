# Input
initial format: multiple lines, each containing two numbers, separated by single tab
`number    number\n`
target format: an array containing two-element tuples

# Part 1
## Idea 1
Create two lists, one for left and one for right side. 
Sort them.
Iterate over one of them.
At each iteration, save a difference between these two in another array.
In the end, sum the element of array containing differences.

### Complexity
Space: Four n-elements arrays
Time: O(n)

# Part 2
## Idea 1
Similiarly to part 1, we separate the data into two lists, left and right.
Next, for each number in left list, we count occurences in right list.
Assuming naive approach, we iterate over right list each time, checking if the number from left list is matching the one we currently iterate over.
Problem: O(n^2) time complexity.
Possible solutions: Creating a dictionary {number: no_of_occurences}, which reduces the times we iterate over right list from *n* times to 1. To be researched later.

### Complexity
Space: Three n-elements arrays
Time: O(n^2)