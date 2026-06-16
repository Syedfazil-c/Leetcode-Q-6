Plus One

Problem

You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer.

The digits are ordered from most significant to least significant digit from left to right.

Increment the large integer by one and return the resulting array of digits.

Approach

Start traversing the array from the last digit.

If the current digit is less than 9:
- Add 1 to it.
- Return the updated array immediately.

If the current digit is 9:
- Change it to 0.
- Continue moving left to handle the carry.

If all digits are 9:
- Convert all digits to 0.
- Add 1 at the beginning of the array.

Complexity

Time Complexity: O(n)

Space Complexity: O(1)

Key Insight

When adding 1 to a number, we start from the rightmost digit.

If a digit becomes 10, we write 0 and carry 1 to the next digit on the left.

The only special case occurs when all digits are 9, requiring an extra digit at the beginning.

Example

Input:
digits = [1,2,3]

Output:
[1,2,4]

Explanation:
123 + 1 = 124

Input:
digits = [4,3,2,1]

Output:
[4,3,2,2]

Explanation:
4321 + 1 = 4322

Input:
digits = [9,9,9]

Output:
[1,0,0,0]

Explanation:
999 + 1 = 1000

Code

def plusOne(digits):
    for i in range(len(digits)):
        if digits[i] <9:
            digits[i]+=1
            return digits
        digits[i]=0
    return [1]+digits

