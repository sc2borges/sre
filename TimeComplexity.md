
```
************************Disclaimer*************************************
*
*
* I have had to understand how the Time Complexity works to write this script
* I think I barelly scratch the surface, but I think at least understand the idea of the script 
* runnning and returning the X number of elements from the file.
*
* I Appreaciate the opportunity
************************************************************************
```


## Q3 

Write a program, topX - given a number X and an arbitrarily large file that contains individual
numbers on each line (e.g. 500Gb file), will output the largest X numbers, highest first.

Tell us about the run time/space complexity of it, and whether you think there's room for
improvement in your approach.

#### Running the Program

Before execute we need to have a `txt` that contains random number to execute the main Program. 

This simple script creates 2.5 million lines.

```
python3 random_lines.py
 -> Generated 2500000 unique random numbers in random_numbers.txt
``` 

Running the main program to print the X numbers defined on the prompt cli.

The following will print the 30 highest number in the file.

E.Q
```
python3 topx.py random_number.txt 30 

```

#### Explaining the Time Complexity and Improvements


Since I am using the python module Heapq to execute this problem related to time complexity.

the explaination is the following.

* Using a simple for loop to ready each line we can sort the array. 

* the array initialize empty(`O(1)`), the heap or (heapsort) will structure the queue with the smaler object as the root tree, we order from botton to top 

* Everytime we sort the objets we swap the biggest with the smaler to order the tree, from the botton we have increase the complexity that depends the number of elements in the file and 
the Time Complexity for this process will use the `O(nlogn)` 

* After ready all elements in the file I compare the number of elements to extract from the array, like X set as 30 will append onto the array and once I have all elements in `min_heap` ordered is easy to reverse the list sorting the biggest numbers in order and return only the 30 results in the execution.

---

This implementation use 2 functions from heapq module (heappop and heappush)
heappop - Pop and return the smallest item from the heap, maintaining the heap invariant
heappush - Push the value item onto the heap.

To improve this program I can replace both functions to use `heappushpop()` instead and from the documentation explain that runs more efficiently


---
Reference resources

https://docs.python.org/3/library/heapq.html

https://stackoverflow.com/questions/52556930/time-complexity-of-the-heap-pop-operation

https://medium.com/@yankuan/time-complexity-of-creating-a-heap-or-priority-queue-fd23bcaefb83