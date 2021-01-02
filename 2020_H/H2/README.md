# Boring Numbers
(7pts, 12pts)

## Problem

Ron read a book about boring numbers. According to the book, a positive number is called boring if all of the digits at even positions in the number are even and all of the digits at odd positions are odd. The digits are enumerated from left to right starting from 1. For example, the number 1478 is boring as the odd positions include the digits {1, 7} which are odd and even positions include the digits {4, 8} which are even.

Given two numbers L and R, Ron wants to count how many numbers in the range [L, R] (L and R inclusive) are boring. Ron is unable to solve the problem, hence he needs your help.
Input
The first line of the input gives the number of test cases, T. T test cases follow. Each test case consists of a single line with two numbers L and R.

## Output

For each test case, output one line containing Case #x: y, where x is the test case number (starting from 1) and y is the count of boring numbers.

## Limits

Time limit: 20 seconds.
Memory limit: 1 GB.
1 ≤ T ≤ 100.
Test Set 1
1 ≤ L ≤ R ≤ 10^3.
Test Set 2
1 ≤ L ≤ R ≤ 10^18.

## Sample

Input

3  
5 15  
120 125  
779 783  

Output

Case #1: 6  
Case #2: 3  
Case #3: 2  

  
In Sample Case #1, the numbers in the range are {5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15} out of which {5, 7, 9, 10, 12, 14} are boring, hence the answer is 6.

In Sample Case #2, the numbers in the range are {120, 121, 122, 123, 124, 125} out of which {121, 123, 125} are boring, hence the answer is 3.

In Sample Case #3, the numbers in the range are {779, 780, 781, 782, 783} out of which {781, 783} are boring, hence the answer is 2.

## Solution

Following the analysis from the author of this problem.

> For example, let R = 3422. Number of boring numbers in [1, R] equals the number of boring numbers in [1,9] + [10, 99] + [100, 999] + [1000, 1999] + [2000, 2999] + [3000, 3099] + [3100, 3199] + [3200, 3299] + [3300, 3399] + [3400, 3409] + [3410, 3419] + [3420, 3422].

There are three types of the intervals:
1. intervals that start with 1(0) and end with (9)
2. intervals that start with x(0) and end with x(9)
3. last interval [x, y] where y - x < 10
It's easier to do this with two while loops, first we increment the length of the numbers until we exhaust all intervals type 1. Then we look for intervals type 2 and decrease the length until we reach the last interval type 3.

> Final answer = (number of boring numbers less than or equal to R) - (number of boring numbers less than or equal to L - 1).  
Complexity = O(log10(R)).

With as high input as 10^18 we had to find logarithmic solution. The best scenario is O(log10(R)). For example, if R = 1000, we can have only 3 intervals [1,9],[10,99],[100,999], log10(1000) = 3.

## Testing  

### Python 3.6
```
python3.6 h2.py < input.txt
```

### PyPy2
```
pypy h2pp2.py < input.txt
```

### Javascript
```
node h2.js < input.txt
```

### TypeScript

```
tsc
node h2.js < input.txt
```

### TypeScript Node
```
ts-node h2.ts < input.txt
```