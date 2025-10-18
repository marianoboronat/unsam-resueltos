

def recursion(n):
    if n < 1:
        return
    else:

        print(recursion(n-1))
        return n

recursion(8)