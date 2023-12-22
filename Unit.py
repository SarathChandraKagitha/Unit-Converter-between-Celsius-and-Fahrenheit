choice = int(input("Enter 1 to covert CELSIUS to FAHRENHEIT\n"      
               "      2 to convert FAHRENHEIT to CELSIUS\n"
               "Enter the value :"))
temp=0
try:
	if choice==2 :
		temp = float(input("Enter temperature in Fahrenheit :"))
	elif choice==1 :
		temp = float(input("Enter temperature in Celsius :"))   
	else :
		print("Please check the number you enterd. Since the number should only be 1/2")
except :
	print ('		Non numeric data found. Check that the data is entered is a Numeric Value.\n		Since the unsupported units are identified, the output temperature will be for 0 units of the input temperature')	
    

def to_fahrenheit() :
    fahrenheit = (temp*1.8)+32 
    print("Temperature in fahrenheit =",fahrenheit,"°F")

def to_celsius() :
    celsius = (temp - 32) * .5556
    print("Temperature in celsius =",celsius,"°c")

def convert():
    if choice==1:
        to_fahrenheit()
    elif choice==2 :   
        to_celsius()
   
convert()