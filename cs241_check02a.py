
def prompt_number():
    while True:
        num = int(input("Enter a positive number: "))
        if num >= 0:
            return num
        elif num <= 0:
          print("Invalid entry. The number must be positive.")

def compute_sum(numb,numb2,numb3):
    sum = numb + numb2 + numb3
    return sum 
  
def main():
  while True:
    
    num1 = prompt_number()
    print()
    num2 = prompt_number()
    print()
    num3 = prompt_number()
    print()
    print("The sum is:",compute_sum(num1,num2,num3))
    break
if __name__ == "__main__":
    main()