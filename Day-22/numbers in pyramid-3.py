n = int(input())
for i in range(n):
    zero_digit = "0 "*(n-i-1)
    pattern = "1 "*(2*i+1)
    print(zero_digit + pattern+zero_digit)