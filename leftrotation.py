def rotateLeft(d, arr):
    while d > 0:
        c = arr[0]
        for j in range(len(arr)):
            if j == len(arr)-1:
                arr[j] = c
            else:
                arr[j] = arr[j + 1]
        d -= 1

    return arr


if __name__ == '__main__':
    d = 4
    arr = [1, 2, 3, 4, 5]
    res = rotateLeft(d, arr)
    print(res)
