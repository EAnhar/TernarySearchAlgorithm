## Ternary Search ##

import random

def ternarySearch(l, r, key, ar):
	if (r >= l):
		#Find the two mids 
		mid1 = l + (r - l) //3
		mid2 = r - (r - l) //3

		#Check if the keys in the mids
		if (ar[mid1] == key):
			return mid1
		if (ar[mid2] == key):
			return mid2
		
		#if not,then search for which range the key is located in,
		#and call the function with new parameter
		if (key < ar[mid1]):
			return ternarySearch(l, mid1 - 1, key, ar)
		elif (key > ar[mid2]):
			return ternarySearch(mid2 + 1, r, key, ar)
		else:
			return ternarySearch(mid1 + 1,mid2 - 1, key, ar)	
		
	#If the key not found return -1
	return -1

#initialize the array size, and create random sorted array
arr_size = 100
my_array = [0] * arr_size
for i in range(arr_size):
    my_array[i] = random.randint(1, 1000)
my_array.sort()

l, r = 0, len(my_array)-1
key = 0 
print("The search array is:\n",my_array)

while key != -1 :
	print("\nEnter the key 1~1000  or -1 to exit: ")
	key = int(input())
	if key == -1:break
	result = ternarySearch(l, r, key, my_array)
	if result == -1 :
		print("the Key not found!")
	else:
		print("Index of", key, "is\t", result)
