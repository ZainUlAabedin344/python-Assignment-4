 # Question No 01
#  Calculate your age based on the current year and your birth year.
print("|<----------------------------------=<Age Calculator=>---------------------------------->|")
def ageCalculator():
    birthYear = int(input("Enter your birth year : "))
    currentYear =int(input("Enter the current year : "))
    age = currentYear -  birthYear
    return age

result:int = ageCalculator()
print(f"Your age is {result} year")




# Question No 02
#  Write a program that calculates the area of a rectangle using length and width variables
print("|<-------------------------------=<Area Calculator  of Rectangle=>------------------------------->|")

def areaCalaculatorOfRectangle():
  length :int = int(input("Enter the length of side of rectangle : "))
  width:int = int(input("Enter the width of rectangle : "))
  area:int = length * width
  return area

result1:int =areaCalaculatorOfRectangle()
print(f"The area of calculator is  {result1}")   


# Question No 03
#  Write a program that calculates the area of a circle
print ("|<-------------------------------<=Area Calculator of circle=>------------------------------->|")
def areaCalculatorOfCircle():
  circleRadius:int =int(input("Enter the diameter of circle : "))/2
  piValue:int =3.141
  area1:int = piValue*circleRadius**2
  return area1

results:int = areaCalculatorOfCircle()
print(f" The Area of circle is {results}" )

# Question No 04
#  Write a program that calculates the area of the cube.
print("|<-------------------------------<=Area calculator of cube=>------------------------------->|")
def areaCalculatorOfCube():
  length:int = int(input("Enter the length of one side of cube : "))**2
  area:int = length * 6
  return area

area:int = areaCalculatorOfCube()
print(f"The area of cube is  {area}" )

# Question No 05
#  Create a program that converts a temperature from Fahrenheit to Celsius and vice versa using a variable.
print("|<--------------------------------<=Temperature Convertor=>-------------------------------->|")
print("|<--------------------------------<=Fahrenheit to Celsius=>-------------------------------->|")
def fahrenheitToCelcius():
  fahrenheit:float = int(input("Enter the temperature in Fahrenheit : ")) 
  celsius:float =((fahrenheit -32) *5/9)
  return  celsius

output:int = fahrenheitToCelcius()
print(f"After converting fahrenheit to celcius, Temperatue is {output}")

print("|<--------------------------------<=Celcius to Fahrenheit=>-------------------------------->|")
def celsiusToFahrenheit():
  celsius1:int = int(input("Enter temperature in Cellcius : "))*9/5
  fahrenheit1:int = celsius1 + 32
  return fahrenheit1

output:int = celsiusToFahrenheit()
print(f"After converting celcius to fahrenheit, Temperatur is {output} ", )


# Question No 06
# Convert a given number of seconds into minutes and seconds using variables.
print("|<--------------------------------<=Time Calculation=>------------------------------->|")
print("|<----------------------------<=Minutes into Seconds=>------------------------------->|")
def minutesIntoSeconds ():
  timeCalculation:int =int(input("Enter time in Minutes to calculate it into second : "))
  result:int = timeCalculation * 60
  return result

userInput:int = minutesIntoSeconds()
print(f"Your given Minutes in seconds {userInput}" )

print("|<-------------------------------<=Second into Minutes=>------------------------------->|")
def secondsIntoMinutes():
  timeCalculate:int = int(input("Enter time in seconds  to calculate it  into minutes : "))
  timeInMinutes:int = timeCalculate / 60
  return timeInMinutes 

output:int = secondsIntoMinutes()
print(f"Your given Seconds in Minutes {output}")

# Question No 07
#  - Write a program that calculates the percentage.
print("|<--------------------------------<=Percentage Calculation=>-------------------------------->|")
def percentageCalculation():
  obtainedMarks:int = int(input("Enter Your Obtained Marks : "))
  totalMarks:int =int(input("Enter total marks : "))
  percentage:int = obtainedMarks / totalMarks * 100
  return percentage

output:int =percentageCalculation()
print(f"Your Obtained marks in percentage is  {output:.4f}" )

# Question No 08
# - Write a program that calculates the BMI using height (in meters) and weight (in kilograms) variables
print("|<---------------------------<=BMI or Body Mass index Calculation=>--------------------------->|")
def bmiCalculation():
  height:int =float(input("Enter Your height in meter : "))
  weight:int =int(input("Enter your body weight in kg : "))
  bmi:int = weight /( height**2)
  return bmi

output:int =bmiCalculation()
print(f"Your BMI is {output:.3f}")

# Question No 09
# - Write a program that calculates the volume of a cylinder using the formula .
print("|<-------------------------------<=Calculate Volume of cylinder=>------------------------------->|")
def volumeOfCylinder():
  radius:int = int(input("Enter the radius  : "))
  height1:int =int(input("Enter the height : "))
  volume:int =3.14*(radius**2)*height1
  return volume

output:int= volumeOfCylinder()
print(f"The volume of cylinder is {output:.2f}")