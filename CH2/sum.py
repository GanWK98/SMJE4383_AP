# initialize the input number and the sum

number_str = input ("Number: ")
the_sum = 0

#Stop if a period (.) is entered. 
# remember, number_str is a string until we convert it
while number_str != "." :
	number = int (number_str)

	if number % 2 == 1: #number is not even (it is odd)
		print ("Error, only even numbers please.")
		number_str = input ("Number: ")
		continue # if the number is not even, ignore it
	the_sum += number

	number_str = input ("Number: ")
	#print (number)

print ("The sum is:", the_sum)