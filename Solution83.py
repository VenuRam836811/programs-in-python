### PROBLEM ###

Count the number of x character in input, but don't count x if it is next to y in either direction.

Case sensitive.
Input
Line 1: x
Line 2: y
Line 3: text A string of random characters
Output
Total count of x not next to a y
If not such x is found, then return 0
Constraints
x length = 1
y length = 1
1 ≤ text ≤ 30
Example
Input
a
b
abca
Output
1

### CODE FOR THE PROBLEM ###

def count_x_not_next_to_y(x, y, text):
    count = 0
    for i in range(len(text)):
        if text[i] == x:
            # Check if 'x' is not next to 'y' in either direction
            if (i == 0 or text[i - 1] != y) and (i == len(text) - 1 or text[i + 1] != y):
                count += 1
    return count

# Example usage:
x = input()
y = input()
text = input()

result = count_x_not_next_to_y(x, y, text)
print(result)
