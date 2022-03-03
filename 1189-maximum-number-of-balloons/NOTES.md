We need **1B 1A 2L 2O and 1N** characters from our string to make the word balloon. Creating a hashmap to store the occurences of these characters would be great. Consider the following table that represents the data that we get after inserting data into the dictionary or hash
| Character | Minimum requirement | What we have |
|-----------|---------------------------|:-------------|
| b         | 1                         | 2            |
| a         | 1                         | 2            |
| l         | 2                         | 4            |
| o         | 2                         | 5            |
| n         | 1                         | 2            |
​
What we can do is we can divide the values that we have by its corresponding value that is required. Then we take the minimum of those values to give the result.