from tkinter import *
import CalculateDrinks

def main():
    root = Tk()
    root.title("GetFuckedUp")
    root.geometry('800x300')
    
    genderLbl = Label(root,width=15,text="Enter Gender (M/F): ")
    genderLbl.grid(column=1,row=1)
    genderForm = Entry(root, width=10)
    genderForm.grid(column=2,row=1)
    
    weightLbl = Label(root,width=15,text="Enter Weight (lbs): ")
    weightLbl.grid(column=1,row=2)
    weightForm = Entry(root, width=10)
    weightForm.grid(column=2,row=2)
    
    levelLbl = Label(root,width=20,text="Enter How FuckedUp (1-10): ")
    levelLbl.grid(column=1,row=3)
    levelForm = Entry(root, width=10)
    levelForm.grid(column=2,row=3)
    
    drinksLbl = Label(root, text="Drinks to be consumed in one hour: ")
    drinksLbl.grid(column=3,row=5)


    def clicked():
            gender = genderForm.get()
            weight = weightForm.get()
            level = levelForm.get()
            
            drinks = CalculateDrinks.CalculateDrinks(weight,gender,level)
            drinksString = str(drinks)
            levelString = str(level)
            updatedLbl = "Drinks to be consumed in one hour: " + drinksString + " drinks to reach a level of " + levelString
            drinksLbl.configure(text=updatedLbl)
    btn = Button(root, text="Calculate Drinks", command=clicked)
    btn.grid(column=1,row=4)

    

    root.mainloop()
    
    # try:
    #     print("\n\n\nWelcome to the General Effecient Trey's Fast Ultimate Cool Knowledgeable Educative Drinking Unflappable Program")
    #     # gender = str(input("\n\nEnter your gender (Type M or F): "))
    #     # weight = float(input("\n\nEnter your weight: "))
    #     # level = int(input("\n\nEnter how FuckedUp would you like to get tonight: "))
    #     if level > 10 or level < 1:
    #         print("\nStop Being Dumb\n")
    #     else:
    #         drinks = CalculateDrinks.CalculateDrinks(weight, gender, level)
    #         print(f"\n\nTo reach a FuckedUp level of {level}, you must consume {drinks} drinks in one hour!\nYou are now legally bound to have {drinks} drinks!\n\n")
    # except ValueError:
    #     print("\n\nInsert the correct values, you twat!")

if __name__ == "__main__":
    main()

