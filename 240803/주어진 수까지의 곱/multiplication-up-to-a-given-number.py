a,b = map(int, input().split())
s = 1
for i in range(a, b+1):
    s *= i
print(s)