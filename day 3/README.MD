# Merge the Tools

Consider the following:


* A string, s , of length n where s = c0c1...cn-1.
* An integer, k , where k is a factor of n.
* We can split s into n/k subsegments where each subsegment, ti , consists of a contiguous block of  characters in . Then, use each  to create string  such that:

  * The characters in  are a subsequence of the characters in .
  * Any repeat occurrence of a character is removed from the string such that each character in  occurs exactly once. In other words, if the character at some index  in  occurs at a previous index  in , then do not include the character in string .
Given  and , print  lines where each line  denotes string .

### Function Description

Complete the merge_the_tools function in the editor below.

merge_the_tools has the following parameters:

* string s: the string to analyze
* int k: the size of substrings to analyze

### Prints

Print each subsequence on a new line. There will be n/k of them. No return value is expected.

### Input Format

The first line contains a single string denoting s.
The second line contains an integer, k, denoting the length of each subsegment.

### Constraints

* 1 <= n <= 10^4, where n is the length of s
* 1 <= k <= n
* It is guaranteed that  is a multiple of .

### Sample Input
 ```
STDIN       Function
-----       --------
AABCAAADA   s = 'AABCAAADA'
3           k = 3

```
### Sample Output

```
AB
CA
AD
```