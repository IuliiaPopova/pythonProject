"""












"""
import fileinput


def fun(l):
    l.sort(key=len)
    s = [len(x) for x in l]
    for x in range(len(s) + 1):
        if s[x] + 1 != s[x + 1]:
            return s[x] + 1


print(fun([[1, 2], [4, 5, 1, 1], [1], [5, 6, 7, 8, 9]]))
