# Multiple
i = int(input("insert 1number : "))
j = int(input("insert 2number : "))
print (i, "*", j, "=", i*j)

# UP & DOWN
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

# LOTTO
import random
n = []
while len(n) < 6:
	rn = random.randint(1, 45)
	if rn not in n :
		n.append(rn)
n.sort()
print(n)


# FizzBuzz
n = int(input("insert your choice number : "))

for i in range(1, n + 1):
	if i %3 == 0 :
		print("Fizz")
	elif i %5 == 0 :
		print("Buzz")
	elif i %15 == 0 :
		print("FizzBuzz")
	else :
		print(i)

