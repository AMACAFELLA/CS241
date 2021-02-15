class Person:
  def __init__(self):
    self.name = "anonymous"
    self.birth = "unknown"
    
  def displayP(self):
    print("{} (b. {})".format(self.name, self.birth))
    
class Book:
  def __init__(self):
    self.title = "untitled"
    self.author = Person()
    self.publisher = "unpublished"
    
  def display(self):
    print(self.title)
    print("Publisher:")
    print(self.publisher)
    print("Author:")
    self.author.displayP()

def main():
  newBook = Book()
  newBook.display()
  print()
  print("Please enter the following:")
  newBook.author.name = input("Name: ")
  newBook.author.birth = input("Year: ")
  newBook.title = input("Title: ")
  newBook.publisher = input("Publisher: ")
  print()
  newBook.display()
  
  
if __name__ == "__main__":
  main()
