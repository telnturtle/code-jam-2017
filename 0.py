# -*- coding: UTF-8 -*-

def drop_side_plus(str):

    left = 0
    right = len(str) - 1

    while str[left] == "+":
        left += 1

    while str[right] == "+":
        right -= 1

    # print("left = {}, right = {}".format(left, right))
    return str[left:right+1]



def flip(str, k):

    l = list(str)
    # print(str)
    for i in range(0, k):
        if l[i] == '+':
            l[i] = '-'
        else:
            l[i] = '+'

    return "".join(l)



# def is_str_all_that_ch(str, ch):

#     res = True

#     for c in str:
#         if c != ch:
#             res = False

#     return res

# def fn(str, ch):
#     return str == ch * len(str)


f = open("A-small-attempt0.in", "r")

t = int(f.readline())
lines_print = []
for i in range(1, t+1):

    _str, k = [s for s in f.readline().split(" ")]
    k = int(k)

    times_flip = 0

    while True:

        if _str == '+' * len(_str):
            break

        _str = drop_side_plus(_str)

        if len(_str) < k:
            times_flip = "IMPOSSIBLE"
            break

        _str = flip(_str, k)
        times_flip += 1


    lines_print.append("Case #{}: {}".format(i, times_flip))

f.close()

f2 = open("output", "w")

for _line in lines_print:
    f2.write(_line+"\n")





"""
끝부분의 +들을 잘라냄
끝의 -를 교정함
"""
