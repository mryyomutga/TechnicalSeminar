from __future__ import print_function
import time

for n in range(0,10):
	print(n)
	time.sleep(0.5)
print()

for n in range(0, 10, 2):
	print(n)
	time.sleep(0.5)
print()

for n in [0, 2, 4, 6, 10, 8]:
	print(n)
	time.sleep(0.5)
print()

for n in [1, 0.2, 1, 0.5, 1, 0.2]:
	print(n)
	time.sleep(n)

