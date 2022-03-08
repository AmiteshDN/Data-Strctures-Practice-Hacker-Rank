from audioop import reverse


def reverseArray(a):
    a.reverse()
    return a


if __name__ == '__main__':
    a = [1, 2, 3, 4, 5]
    res = reverseArray(a)
    print(res)
