a = int(input())
b = int(input())

if 1<= a <= b:
    squares_count = 0
    for i in range(a,b+1):
        if i**0.5 == int(i**0.5):
            squares_count = squares_count +1

    print(squares_count)

# a = 9
# b = 100
# so square count is 8 perfect squares