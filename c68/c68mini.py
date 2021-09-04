"Single Cycle Check"

"""
Problem Statement
You are given an array of integers. Each integer represents a jump of its value in the array. 
For instance, the integer 2 represents a jump of 2 indices forward in the array;
the integer -3 represents a jump of 3 indices backward in the array. 
If a jump spills past the array's bounds, it wraps over to the other side. 
For instance, a jump of -1 at index 0 brings us to the last index in the array. 
Similarly, a jump of 1 at the last index in the array brings us to index 0. 
Write a function that returns a boolean representing whether the jumps in the array 
form a single cycle. 
A single cycle occurs if, starting at any index in the array and following the jumps, 
every element is visited exactly once before landing back on the starting index.
"""

"""
Sample input:

[2, 3, 1, -4, -4, 2] -> True
[2, 2, -1] -> True
[1, 2, 3, 4] -> False
[5] -> True
[] -> True
[1] -> True
[6, 7] -> False
[8, 2, -1] -> True

"""
a=[2, 3, 1, -4, -4, 2]
# b=set(range(len(a)))
# print(b)
# [b.remove((i+j)%len(a))for i,j in enumerate(a)];print(b);print([False,True][len(b)==0])

# print([False,True][set((i+j)%(c:=len(a))for i,j in enumerate(a))==set(range(c))])

for _ in [z:=input]*int(z()):
    a=eval(z())
    print([False,True][set((i+j)%(c:=len(a))for i,j in enumerate(a))==set(range(c))])


