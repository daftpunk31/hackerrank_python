from itertools import product
if __name__=='__main__':
    map_a=map(int, input().split())
    map_b=map(int, input().split())
    a=set(map_a)
    b=set(map_b)
    A=list(a)
    B=list(b)
    print(*list(product(A, B)))
# This is the explanation
'''
You are given a two lists  and . Your task is to compute their cartesian product X.
Example
A = [1, 2]
B = [3, 4]

AxB = [(1, 3), (1, 4), (2, 3), (2, 4)]
Note:  and  are sorted lists, and the cartesian product's tuples should be output in sorted order.
Input Format
The first line contains the space separated elements of list . 
The second line contains the space separated elements of list .
Both lists have no duplicate integer elements.
Constraints
 

Output Format
Output the space separated tuples of the cartesian product.
Sample Input
 1 2
 3 4
 
Sample Output
 (1, 3) (1, 4) (2, 3) (2, 4)

'''
