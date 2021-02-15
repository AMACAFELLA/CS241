class robot:
  #creates a class called robot
  def __init__(self):
    self.xcoord = 10
    self.ycoord = 10
    self.fuel_a = 100
   #The varibles for the robot class
  def display(self):
    print("({}, {}) - Fuel: {}".format(self.xcoord, self.ycoord,self.fuel_a)) 
    #display function for the output format of the varibles

  def left(self):
    if self.fuel_a <= 0:
      print("Insufficient fuel to perform action")
    else:
      self.xcoord = self.xcoord -1
      self.fuel_a = self.fuel_a - 5
      #if fuel is less than 0 it will display not enough fuel if their is it will subtract from the xcoord and fuel
  
  def right(self):
    if self.fuel_a <= 0:
       print("Insufficient fuel to perform action")
    else:
      self.xcoord = self.xcoord + 1
      self.fuel_a = self.fuel_a - 5
      #if fuel is less than 0 it will display not enough fuel if their is it will add to the xcoord and fuel
  
  def up(self):
    if self.fuel_a <= 0:
      print("Insufficient fuel to perform action")
    else:
      self.ycoord = self.ycoord - 1
      self.fuel_a = self.fuel_a - 5
      #if fuel is less than 0 it will display not enough fuel if their is it will subtract from the xcoord and fuel

  def down(self):
    if self.fuel_a <= 0:
      print("Insufficient fuel to perform action")
    else:
      self.ycoord = self.ycoord + 1
      self.fuel_a = self.fuel_a - 5
      #if fuel is less than 0 it will display not enough fuel if their is it will add to the xcoord and fuel

  def fire(self):
    if self.fuel_a >= 15:
      print("Pew! Pew!")
      self.fuel_a = self.fuel_a - 15
    elif self.fuel_a <= 10:
      print("Insufficient fuel to perform action")
      #if fuel greater than or equals to 15 the function will print pew and subtract from fuel. Otherwise if it is less than 10
      #the elif statement will kick in printing not enough fuel

  def prompt_value(self):
    user = ""
    while user != "quit":
      user = input("Enter command: ")
      if user == "status":
        robot.display(self)
      elif user == "left":
        robot.left(self)  
      elif user == "right":
        robot.right(self)
      elif user == "down":
        robot.down(self)  
      elif user == "up":
        robot.up(self)  
      elif user == "fire":
        robot.fire(self)  
    else:
      print("Goodbye.")
    return user
    #The prompt function where the user enters the actions and each function is called 

def main():
   mr_robot = robot()
   #creates object in the main finction
   mr_robot.prompt_value()
   #main function calls prompt_value function which starts the program.
   
   
   
        
if __name__ == "__main__":
  main()