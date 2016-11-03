from math import factorial

#using recursion
# def recur_factorial(n):
#    if n == 1:
#        return n
#    else:
#        return n*recur_factorial(n-1)


# calculating sum of digits 
def sum(number):
	temp=0
	if number<10:
		return number
	else:
		for item in map(int, str(number)):
			temp =temp + item
		return temp	
			

# main function
def main():
	num = int(input("Enter a number to find its factorial : "))

	if num < 0:
	   print "Oops, Factorial does not exist for negative numbers"
	elif num == 0:
		print "Factorial of 0 is 1"
	else:
		# factorial_num=recur_factorial(num)
		factorial_of_num=factorial(num)
		# print("The factorial of",num,"is",recur_factorial(num))
		print " Factorial of %s is : %s " % (num, factorial_of_num)
		result=sum(factorial_of_num)

		print 'Sum is : %s' %  result


if __name__=="__main__":
	main()		



       
