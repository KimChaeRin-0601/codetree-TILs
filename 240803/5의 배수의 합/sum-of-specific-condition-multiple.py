a, b  =map(int, input().split())
cnt = 0
if a < b:
    for i in range(a, b+1):
        if i % 5 == 0:
            cnt += i 
elif a == b:
    for i in range(a, b+1):
        if i % 5 == 0:
            cnt += i 
else:
    for i in range(b, a+1):
        if i % 5 == 0:
            cnt += i
print(cnt)