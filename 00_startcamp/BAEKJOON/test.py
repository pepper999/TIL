a, b, c, d, e, f = map(int, input().split())
if b != 0 and a != 0:
    x = ((e/b)*c-f)/((e/b)*a-d)
    y = ((d/a)*c-f)/((d/a)*b-e)
elif a == 0:
    y = c/b
    x = (f-(c/b)*e)/d
elif b == 0:
    x = c/a
    y = (f-(c/a)*d)/e
print(int(x), int(y))

sds