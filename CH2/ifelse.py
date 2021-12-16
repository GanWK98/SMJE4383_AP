percent_float = float (input ("What is your percentage? "))

if 90 <= percent_float < 100: 
	print ("you received an A")

if 80 <= percent_float < 90:
	print ("you received a B")

elif 70 <= percent_float < 80:
	print("you received a C")

if 60 <= percent_float < 70:
	print("you received a D")

elif 50 <= percent_float < 60:
	print("you received a E")

else:
	print("oops, not good")