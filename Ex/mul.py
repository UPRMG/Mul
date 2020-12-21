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
rn = random.sample(range(1, 46), 6)
rn.sort()
print(rn)

# LOTTO
import random
a = []
o = random.randint(1,45)
for i in range(6):
    while o in a:
        o = random.randint(1,45)
    a.append(o)
a.sort()
print(a)


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

        
#Fibonacci Sequence
first = {1:1,2:1}

def f(x):
    if x in first:
        return first[x]
    
    output = f(x-1)+f(x-2)
    first[x] = output
    
    return output

f(7)

