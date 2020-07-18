
def check_number(number):
	if(len(number)==10 and number.isdigit() and int(number[0])>6 and int(number[0])<10):
		return "VALID"
	else:
		return "NOT VALID"

number = input("Enter number: ")
print(check_number(number))