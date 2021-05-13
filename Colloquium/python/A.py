def find_substr(s1, s2):
    sought = set(s2)
    minleft, minright = len(s1), len(s1)
    bestleft, bestright = len(s1), len(s1)
    while minleft > 0:
        while not sought.issubset(s1[minleft:minright]) and minleft > 0:
            minleft -= 1
        while sought.issubset(s1[minleft:minright]) and minleft < minright:
            if bestleft == len(s1) or minright-minleft <= bestright-bestleft:
                bestleft, bestright = minleft, minright
            minright -= 1
    return s1[bestleft:bestright]


if __name__ == '__main__':
    s1, s2 = input(), input()
    print(find_substr(s1, s2))
