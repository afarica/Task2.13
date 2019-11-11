# For a given integer N, print all the squares of integer numbers where the
# square is less than or equal to N, in ascending order.
a=int(input("Enter your number:"))
i=1
while i**2<=a**2:
	print(i**2) 
	i += 1
