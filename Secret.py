substring = input("Enter a Secret Messsage :")
string = input("Enter a Coded Message :")
if substring in string:
	print("Secret message is found")
else:
	print("	Secret message is NOT found")