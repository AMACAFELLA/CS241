class Student:
  def __init__(self):
    self.fname = ""
    self.lname = ""
    self.id = 0

def prompt_student():
  stu = Student()
  stu.fname = input("Please enter your first name: ")
  stu.lname = input("Please enter your last name: ")
  stu.id = input("Please enter your id number: ")
  return stu

def display_student(user):
  print("Your information:")
  print('{} - {} {}'.format(user.id,user.fname, user.lname))

def main():
   user = prompt_student()
   print()
   display_student(user)
        
if __name__ == "__main__":
  main()
