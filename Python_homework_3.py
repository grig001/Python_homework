x = [1, -2, 3, 9, 0, 1, 3, 2, -2, -4, 1, -3]

x_neg = []
x_pos = []
for i in x:
    if i < 0:
        x_neg.append(i)
    elif i > 0:
        x_pos.append(i)
    else:
        continue

sum = 0
for i in range(1, 102, 2):
    sum += i

print(sum)


sum1 = 0
for i in range(1, 101):
    if i % 2  == 1:
        sum1 += i
    else:
        sum1 += 1 / i

print(sum1)

k = 1
for i in range(2, 21, 2):
    k *= i

print(k)


t = 0
d = 1
for i in range(0, 21):
    t += (-1) ** i / d
    d *= i + 1

print(t)

summ = 0
i = 1
while 2 - summ > 0.001:
    summ += i / 2 ** i
    i += 1

print(summ)


x = list(map(int, input().split()))
max_x = x[0]
for i in x:
    if i > max_x:
        max_x = i

print(max_x)


x = list(map(int, input().split()))
n = len(x)
i = 0
while i < n:
   for j in range(n - i - 1):
       if x[j] > x[j + 1]:
           x[j], x[j + 1] = x[j + 1], x[j]
   i += 1

print(x)

