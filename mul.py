# 원하는 수들의 곱셈
i = int(input("insert 1number : "))
j = int(input("insert 2number : "))
print (i, "*", j, "=", i*j)

# UP & DOWN 게임
import random
rn = random.randint(1, 100)
count = 0

while True:
	n = int(input("Insert your choice number : "))
	count += 1
	if rn > n :
		print("UP!")
	elif rn < n :
		print("DOWN!")
	else :
		print(count)
		break

# 로또 번호 뽑기
import random
n = []
while len(n) < 6:
	rn = random.randint(1, 45)
	if rn not in n :
		n.append(rn)
n.sort()
print(n)


# 별표찍기
n = int(input"insert number : "))
s = n // 2
for star in range(1, n, 2):
	print(" " * s + "*" * star)
	s += 1






