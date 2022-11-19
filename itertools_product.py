from itertools import product
if __name__=='__main__':
    map_a=map(int, input().split())
    map_b=map(int, input().split())
    a=set(map_a)
    b=set(map_b)
    A=list(a)
    B=list(b)
    print(*list(product(A, B)))
