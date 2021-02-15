class Complex:
  def __init__(self):
    self.real = 0
    self.imaginary = 0
    
  def prompt_value(self):
    self.real = input("Please enter the real part: ")
    self.imaginary = input("Please enter the imaginary part: ")
    return self

  def display_value(self):
    print('{} + {}i'.format(self.real,self.imaginary))

def main():
   value = Complex()
   value2 = Complex()
   print("The values are:")
   value.display_value()
   value2.display_value()
   print()
   value.prompt_value()
   print()
   value2.prompt_value()
   print()
   print("The values are:")
   value.display_value()
   value2.display_value()
        
if __name__ == "__main__":
  main()