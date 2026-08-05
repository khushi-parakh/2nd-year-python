# using for loop display multiplication table of any number using for loop

n = int(input("Enter a number whose table you want: "))

print("Table of", n)

for i in range(1, 11):
    print(n, "multiplied by", i, "is equal to", n * i)