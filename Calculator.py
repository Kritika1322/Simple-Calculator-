History=[]
inputs_history = [] 
while True:
        Num1=int(input("please enter a number"))
        Num2=int(input("please enter another number"))
        choice=int(input("please enter a choice:\n 1)Addition\n 2)Subtraction\n 3)Multiply\n 4)Divide\n 5)Exit\n 6)Show History\n 7)Clear History \n 8)Show Input History"))
        print(f"You chose option: {choice}")
        if choice==1:
                ans=Num1+Num2
        
        
        elif choice==2:
                    ans=Num1-Num2
    

        elif choice==3:
                    ans=Num1*Num2
    

        elif choice==4:
            if Num2==0:
                print("Error!Can't Divide By Zero")
                ans=None
            else:
                ans=Num1/Num2
        
        elif choice==5:
            print("Thanks for using the calculatior.\n Exiting Calculatior.\n GOODBYE!!")
            
 #to display history
            
        elif choice == 6:
            if not History:
                print("No History available.")
            else:
                print("\nCalculation History:")
                for item in History:
                    print(item)
            continue
#to clear history
        
        elif choice==7:
                History.clear()
                print("History cleared Succesfully")
                continue
        
        else:
            print("Invalid operation!")
   
        if ans is not None:
            print(f"The answer is :{ans}")
            History.append(Num1)
            last_result = ans 
            
#to continue using the calculator
            
        cont=input("Do you want to continue?(y/n)").lower()
        if cont !='y':
                print("Thanks for using the Calculator.\n Goodbye!")
        


