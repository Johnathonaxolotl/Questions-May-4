print("What question do you want?")  #go to the question choesn.  To go to a different question the program has to be ran again
question=int(input())
if question==1:
  #Question 1
  print("What is your first name?")  #asks the first name of the user
  first_name=input()  #gets the their name and sets it to the varible first_name
  print("What is your last name?")  #asks for the users last name
  last_name=input()  #sets the input to last_name
  print(last_name +", " + first_name)  #prints their name in last name, first name order
elif question==2:
  #Question 2
  print("Choose a number.")  #asks for a number
  number=input()  #sets the number given to the varible number
  if int(number)==0:  #if the number is zero say that the number is zero
    print("The number chosen is zero")
  elif int(number)%2==0:  #if the number is even state that the number chosen is even
    print(number, "is a even number")
  elif int(number)%2==1: #if the number is odd state that the number chosen is odd
    print(number, "is an odd number")
  else:  #if the value is not a number, then state that the value given is not a number 
    print("sorry that is not a number")
elif question==3:
  #Question 3
  print("Choose a day between 1 and 365.")  #asks what day of the year it is
  day=int(input())  #sets the day to the varible day
  if day<=31:  #checks what month it is based on the day and sets the month to that day.  Then when needed subtracts days off to match the number of days for that month
    month="January"
  elif day>=32 and day<=59:
    month="February"
    day-=31
  elif day>=60 and day<=90:
    month="March"
    day-=59
  elif day>=91 and day<=120:
    month="April"
    day-=90
  elif day>=121 and day<=151:
    month="May"
    day-=120
  elif day>=152 and day<=181:
    month="June"
    day-=151
  elif day>=182 and day<=212:
    month="July"
    day-=181
  elif day>=213 and day<=243:
    month="August"
    day-=212
  elif day>=244 and day<=273:
    month="September"
    day-=243
  elif day>=274 and day<=304:
    month="October"
    day-=273
  elif day>=305 and day<=334:
    month="November"
    day-=304
  elif day>=335 and day<=365:
    month="December"
    day-=334
  else:  #if a larger number or smaller number is given, it will say the message is invalid
    print("sorry that value is invalid")
  print("The day chosen is "+month, str(day)+".")  #States the month and day
elif question==4:
  #Question 4
  max_row=5  #how many numbers are in a row
  for i1 in range(5):  #the five is how many rows there will be
    number=5  #resets the number to what is was at the start
    for i2 in range(max_row,0,-1):
      print(number, sep='', end=" ")  #separates the numbers apart
      number-=1  #decreases the number by one so the next number in the row is one less
    print()  #goes to next row
    max_row-=1  #decreases the amount of numbers per row by one
elif question==5:
  #Question 5
  print("Choose a number")  #asks for a number
  number=int(input())  #sets the number given to varible number
  starting_value=number  #saves the starting number
  max_row=starting_value  #how many numbers are in a row
  for i1 in range(starting_value):  #this states how many rows there will be
    number=starting_value  #resets the number to what is was at the start
    for i2 in range(max_row,0,-1):
      print(number, sep='', end=" ")  #separates the numbers apart
      number-=1  #decreases the number by one so the next number in the row is one less
    print()  #goes to next row
    max_row-=1  #decreases the amount of numbers per row by one
elif question==6:
  #Question 6
  print("Choose a day between 1 and 365.")  #asks what day of the year it is
  day=int(input())  #sets the day to the varible day
  if day%7==0 or day==0:
    week="Monday"
  if day%7==1:
    week="Tuesday"
  if day%7==2:
    week="Wednesday"
  if day%7==3:
    week="Thursday"
  if day%7==4:
    week="Friday"
  if day%7==5:
    week="Saturday"
  if day%7==6:
    week="Sunday"
  if day<=31:  #checks what month it is based on the day and sets the month to that day.  Then when needed subtracts days off to match the number of days for that month
    month="January"
  elif day>=32 and day<=59:
    month="February"
    day-=31
  elif day>=60 and day<=90:
    month="March"
    day-=59
  elif day>=91 and day<=120:
    month="April"
    day-=90
  elif day>=121 and day<=151:
    month="May"
    day-=120
  elif day>=152 and day<=181:
    month="June"
    day-=151
  elif day>=182 and day<=212:
    month="July"
    day-=181
  elif day>=213 and day<=243:
    month="August"
    day-=212
  elif day>=244 and day<=273:
    month="September"
    day-=243
  elif day>=274 and day<=304:
    month="October"
    day-=273
  elif day>=305 and day<=334:
    month="November"
    day-=304
  elif day>=335 and day<=365:
    month="December"
    day-=334
  else:  #if a larger number or smaller number is given, it will say the message is invalid
    print("sorry that value is invalid")
  print("The day chosen is "+week, month, str(day)+".")  #States the month and day

else:
  print("Sorry", question, "is not a question.")