def add(num1,num2):
    return num1+num2
def subtract(num1,num2):
    return num1-num2
def multiplication(num1,num2):
    return num1*num2
def division(num1,num2):
    return num1/num2
while True:
    print("Enter the operation\n1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n")
    x=input("Enter the choice (1/2/3/4): ")
    if x in ('1','2','3','4'):
        num1=float(input("Enter the first number : "))
        num2=float(input("Enter the second number : "))
        if(x== "1"):
            print("The addition of",num1,"+",num2,"is",add(num1,num2))
        elif(x == "2"):
            print("The subtract of",num1,"-",num2, "is",subtract(num1,num2))
        elif(x == "3"):
            print("tThe multiplication of",num1,"*",num2 ,"is",multiplication(num1,num2))
        elif(x == "4"):
            print("The division value of",num1,"/",num2 ,"is",division(num1,num2))
        u=input("Do you want to repeat this?(yes/No)")
        if(u=="no"):
            break
        elif(u=="yes"):
            continue
        else:
            print("wrong command")
            break
    else:
        print("Enter wrong input")
        break

    
        
        
               
        
    
