# Author: Alexander Barr ajb7463@psu

def getGradePoint(letter):
  if letter == "A":
    letter = 4.0
  elif letter == "A-":
    letter = 3.67
  elif letter == "B+":
    letter = 3.33
  elif letter == "B":
    letter = 3.0
  elif letter == "B-":
    letter = 2.67
  elif letter == "C+":
    letter = 2.33
  elif letter == "C":
    letter = 2.0
  elif letter == "D":
    letter = 1.0
  else:
    letter = 0.0
  return letter

def run():
  gp1 = getGradePoint(input("Enter your course 1 letter grade: "))
  c1 = int(input("Enter your course 1 credit: "))
  print(f"Grade point for course 1 is: {gp1}")

  gp2 = getGradePoint(input("Enter your course 2 letter grade: "))
  c2 = int(input("Enter your course 2 credit: "))
  print(f"Grade point for course 2 is: {gp2}")

  gp3 = getGradePoint(input("Enter your course 3 letter grade: "))
  c3 = int(input("Enter your course 3 credit: "))
  print(f"Grade point for course 3 is: {gp3}")

  gpa = ((gp1 * c1 + gp2 * c2 + gp3 * c3)/(c1 + c2 + c3))

  print(f"Your GPA is: {gpa}")

  if __name__ == "__main__":
    run()

  
  