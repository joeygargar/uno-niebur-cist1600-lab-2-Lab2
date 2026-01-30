#Magic8Ball.py
#Name: Mia Garcia
#Date: 1/29/26
#Assignment: Lab 2

#We will need random for this program, import to use this package.
import random

def main():
  #Create a list of your responses.
  print("Magic 8 Ball")
  #Prompt the user for their question.
  input("ask any question?")
  answers = ("yes", "no", "try again later", "not likely", "definitely", "somewhat likely")
  #Answer question randomly with one of the options from your earlier list.
  
  r = random.random()* len(answers)
  r = int(r)
  #print(r)
  response = answers[r]
  print(response)
  


if __name__ == '__main__':
  main()
