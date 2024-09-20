'''
    Lesson: Input and F strings Work
    Author: Aiden
    Date Created: Sept 19, 2024
    Date Last Modified: Spet 19, 2024
'''


def q1():
  #Write Assignment code here
  words = input("Type a word:")
  print(words)

def q2():
  #Write Assignment code here
  name = input("First name:")
  print("Hello " + name)

def q3():
  #Write Assignment code here
  first = input("Your first name:")
  last = input("Your last name :")
  print(last + first)

def q4():
  #Write Assignment code here
  studentOne = input("A students name:")
  studentTwo = input("Another students name:")
  students = f"Your students are {studentOne} and {studentTwo}"
  print(students)

#Do not edit code below this comment


q1()
q2()
q3()
q4()
