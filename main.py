from pyfile.RealNumber import RealCramer

while True:
    try:
        print("Cramer's Rule Calculator")
        print("Enter The Following Number for Different Calculation:")
        print("1 - Real Number Simultaneous Equation")
        print("2 - Imaginary Number Simultaneous Equation")
        print("0 - Exit")
        
        Operation1 = int(input("Enter Your Operation > "))
        
        if Operation1==0:
            break
        elif Operation1==1:
            RealCramer.interface()
        elif Operation1==2:
            print("Under development!")
        else:
            print("Value INvalid, please try again!")
    
    except ValueError:
        print("The Operation Entered is Invalid, Please Try Again")    