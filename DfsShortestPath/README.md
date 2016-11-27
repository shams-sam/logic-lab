> #### given graph consisting of n nodes and m edges
#### there exist two different probes p1 and p2 which are used to traverse the edges which have different speeds v1 and v2
#### an edge can be marked 0 meaning it can be traversed by both the probes
#### or edge can be marked 1 meaning it can be traversed by only probe p1
#### find the shortest path by both probes from node x to node y and respective times
#### return max_int for no path found


##### input format
##### first line n and m
##### second line v1 and v2
##### third line x and y
##### following m lines have xi yi edge followed by distance and which probe can traverse it

Sample inputs and outpus
------------------------
````
5 6
12 25
0 4
0 1 5 0
0 2 2 1
0 3 5 0
1 4 5 0
2 4 2 1
3 4 5 0
p2 time 10
p1 time 4
````

````
7 8
10 25
6 1
0 1 3 1
1 2 10 1
2 4 10 1
4 6 7 1
4 5 3 1
1 3 20 0
3 5 20 0
5 6 30 0
p2 time 70
p1 time 27
````

````
7 8
10 25
1 6
0 1 3 1
1 2 10 1
2 4 10 1
4 6 7 1
4 5 3 1
1 3 20 0
3 5 20 0
5 6 30 0
p2 time 70
p1 time 27
````

````
7 8
10 25
5 6
0 1 3 1
1 2 10 1
2 4 10 1
4 6 7 1
4 5 3 1
1 3 20 0
3 5 20 0
5 6 30 0
p2 time 30
p1 time 10
````

````
7 8
10 25
5 4
0 1 3 1
1 2 10 1
2 4 10 1
4 6 7 1
4 5 3 1
1 3 20 0
3 5 20 0
5 6 30 0
p2 time none
p1 time 3
````
