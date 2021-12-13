W, H, x, y, r = map(int,input().split())
if H - y >= r and W - x >= r and x >= r and y >= r:
    print("Yes")
else:
    print("No")
