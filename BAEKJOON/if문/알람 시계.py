h, m = input().split()
h = int(h)
m = int(m)
if m >= 45:
    m = m-45
    print(h, m)
elif h == 0:
    h = 23
    m = 15 + m
    print(h, m)
elif m < 45:
    h = h - 1
    m = 15 + m
    print(h, m)
