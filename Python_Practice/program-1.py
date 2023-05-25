
def sumOfTwoNumbers(num1,num2):
    sum=num1+num2
    print ("sum of two numbers is" ,sum)

sumOfTwoNumbers(2,3)

# maximum of two numbers

def maxOfTwoNumbers(num1,num2):
    if num1>num2:
        print(num1, "is greater")
    elif num1==num2:
        print("Both are equal")
    else:
        print(num2,"is greater")

maxOfTwoNumbers(2,2)

#factorial of a number

def factorialOfNUmber(number):
    factorial=1
    if(number<0):
        print("Error!Factorial for negative number doesnt exist")
        return
      
    else:
         while number>1:
             factorial=factorial*number
             number-=1
              
    print(factorial)     


factorialOfNUmber(4)
