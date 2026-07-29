#To calculate if x is divisible by both 3 and 5

x=int(input("Enter a number:"))
if (x % 3 == 0) and (x % 5 ==0):
	print(x,"Is divisible by both 3 and 5")
else:
	print(x,"Is not divisible by both 3 and 5")