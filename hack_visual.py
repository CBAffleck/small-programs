import random
import time

target = list("HELLO WORLD")
string = []
i = 0
for x in target:
	string.append("0")
while True:
	j = 0
	if string == target:
		break
	while j < len(target):
		if string[j] == target[j]:
			j += 1
		else:
			guess = chr(random.randint(32, 126))
			string[j] = guess
			j += 1
	print("".join(string), end="\r")
	time.sleep(.02)
print("".join(string))