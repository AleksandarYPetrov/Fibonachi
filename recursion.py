def fibonachi(n):
    if n <= 2:
        return 1
    else:
        return  fibonachi(n-1)+fibonachi(n-2)

print  (fibonachi(8)) #21

