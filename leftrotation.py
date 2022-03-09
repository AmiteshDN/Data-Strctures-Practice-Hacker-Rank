def rotateLeft(d, arr):
    # for the 'n' number of left shifts, slice the list from 'n'
    # add the list upto 'n'
    return (arr[d:] + arr[:d])


if __name__ == '__main__':
    d = 4
    arr = [1, 2, 3, 4, 5]
    res = rotateLeft(d, arr)
    print(res)
