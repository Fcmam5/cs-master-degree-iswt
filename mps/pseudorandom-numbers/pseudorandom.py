a = 5
c = 9
RESULT = []
def pseudorandom(val, m):
    x = 2
    i = 1
    k = 0

    while 2**i < m:
        i += 1
        MM = 2**i
        k += 1
    x = (a * val + c)%MM

    if x < m:
        print("pseudorandom() => ",x)
        return x
    else:
        pseudorandom(x,m)


if __name__ == '__main__':
    for k in range(1,3):
        pseudorandom(2,k)
