# Max Min

You will be given a list of integers,  arr , and a single integer k. You must create an array of length k from elements of arr such that its unfairness is minimized. Call that array arr' . Unfairness of an array is calculated as

                max( arr' ) -  min( arr ' )

Where:
- max denotes the largest integer in arr' .
- min denotes the smallest integer in arr'.


Note: Integers in  may not be unique.

### Function Description

Complete the maxMin function in the editor below.
maxMin has the following parameter(s):

* int k: the number of elements to select
* int arr[n]:: an array of integers

### Returns

* int: the minimum possible unfairness

### Input Format

* The first line contains an integer n, the number of elements in array arr.
* The second line contains an integer k .
* Each of the next n lines contains an integer arr[ i ] where 0  <=  i  < n.

### Constraints

* 2  <=  n  <=  10^5
* 2  <=  k  <=  n
* 0   < =   arr[ i ]   <=  10^9


### Sample Input 0
```
7
3
10
100
300
200
1000
20
30
```

### Sample Output 0
```
20
```