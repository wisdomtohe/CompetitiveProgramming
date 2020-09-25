# 10041 - Vito's Family

The world-known gangster Vito Deadstone is moving to New York. He has a very big family there, all
of them living in Lamafia Avenue. Since he will visit all his relatives very often, he is trying to find a
house close to them.

Vito wants to minimize the total distance to all of them and has blackmailed you to write a program
that solves his problem.


## Input

The input consists of several test cases. The first line contains the number of test cases.

For each test case you will be given the integer number of relatives *r* (0 < *r* < 500) and the street
numbers (also integers) *s<sub>1</sub>, s<sub>2</sub>, . . . , s<sub>i</sub>, . . . , s<sub>r</sub>* 
where they live (0 < s<sub>i</sub> < 30000 ). Note that several relatives could live in the same street number.


## Output

For each test case your program must write the minimal sum of distances from the optimal Vito’s house
to each one of his relatives. The distance between two street numbers *s<sub>i</sub>* and *s<sub>j</sub>* 
is *d<sub>ij</sub> = |s<sub>i</sub> − s<sub>j</sub> |*.


## Sample Input

```bash
2
2 2 4
3 2 4 6
```

## Sample Output

```bash
2
4
```

[\[pdf\]](https://uva.onlinejudge.org/external/100/10041.pdf)
