from tkinter import *
import Calculations

class SafeSipApp(Tk):
    def __init__(self):
        super().__init__()
        self.title("SafeSipApp")
        self.geometry("849x741")

        container = Frame(self)
        container.pack(fill="both", expand=True)
        
        self.frames = {}
        for F in (HomePage, Calculator):
            frame = F(container,self)
            self.frames[F] = frame
            frame.place(x=0, y=0, relwidth=1, relheight=1)

        self.show_frame(HomePage)

    def show_frame(self,page):
        if page in self.frames:
            frame = self.frames[page]
            frame.tkraise()
        else:
            print(f"Error: {page} not found in frames!")

class HomePage(Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
       
        # Label(self, text="Home Page").grid(pady=20)
        # Button(self, text="Go to Drink Calculator", command=lambda: controller.show_frame(Calculator)).grid()
        self.SafeSipLogo = PhotoImage(file="SafeSipLogo.png")
        # Label(self, image=self.SafeSipLogo).grid(column=2, row=2)

        background = Canvas(self, width=849, height=741)
        background.grid()
        background.create_image(0, 0, image = self.SafeSipLogo, anchor = "nw")

        homePageLabel = Label(self, text="Home Page")
        homePageLabel_Canvas = background.create_text(100, 10,  
                                       anchor = "nw", 
                                       text= homePageLabel)
        goToCalcButton = Button(self, text="Go to Drink Calculator", command=lambda: controller.show_frame(Calculator))
        goToCalcButton_Canvas = background.create_window(100, 10,  
                                       anchor = "nw", 
                                       window = goToCalcButton)
        


class Calculator(Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        Label(self, text="Calculator").grid(pady=50, column=8)
        Button(self, text="Back to Home", command=lambda: controller.show_frame(HomePage)).grid(column=3,row=8)
        
        self.configure(bg="#1e1e2f")  

        font_label = ("Helvetica", 12, "bold")
        font_entry = ("Helvetica", 12)
        font_button = ("Helvetica", 14, "bold")
        text_color = "#f5f5f5"
        accent_color = "#00bcd4"

        # Gender Label and Entry
        # genderLbl = Label(root, text="Enter Gender (M/F):", font=font_label, fg=text_color, bg="#1e1e2f", width=20, anchor="e")
        # genderLbl.grid(column=0, row=0, pady=10, padx=10)
        # genderForm = Entry(root, font=font_entry, bg="#33334d", fg=text_color, insertbackground=text_color, width=15)
        # genderForm.grid(column=1, row=0, pady=10, padx=10)

        Male = IntVar()
        Female = IntVar()

        MaleButton = Checkbutton(self, text="Male", 
                                variable=Male,
                                onvalue=1,
                                offvalue=0
                                )
        FemaleButton = Checkbutton(self, text="Female", 
                                variable=Female,
                                onvalue=1,
                                offvalue=0
                                )
        MaleButton.grid(column=0, row=0)
        FemaleButton.grid(column=1 ,row=0, padx=100,pady=20)


        # Weight Label and Entry
        weightLbl = Label(self, text="Enter Weight (lbs):", font=font_label, fg=text_color, bg="#1e1e2f", width=20, anchor="e")
        weightLbl.grid(column=0, row=1, pady=10, padx=10)
        weightForm = Entry(self, font=font_entry, bg="#33334d", fg=text_color, insertbackground=text_color, width=15)
        weightForm.grid(column=1, row=1, pady=10, padx=10)

        # Level Label and Entry
        levelLbl = Label(self, text="Enter What Level of Intoxication\nYou Would Like to Achieve (1-10):", font=font_label, fg=text_color, bg="#1e1e2f", width=26, anchor="e")
        levelLbl.grid(column=0, row=2, pady=10, padx=10)
        levelForm = Entry(self, font=font_entry, bg="#33334d", fg=text_color, insertbackground=text_color, width=15)
        levelForm.grid(column=1, row=2, pady=10, padx=10)

        # Hours Label and Entry
        hoursLbl = Label(self, text="Enter How Many Hours You\nWill Be Drinking Over: ", font=font_label, fg=text_color, bg="#1e1e2f", width=26, anchor="e")
        hoursLbl.grid(column=0, row=3, pady=10, padx=10)
        hoursForm = Entry(self, font=font_entry, bg="#33334d", fg=text_color, insertbackground=text_color, width=15)
        hoursForm.grid(column=1, row=3, pady=10, padx=10)

        # Drinks Result Label
        drinksLbl = Label(self, text="Drinks to be consumed:", font=font_label, fg=accent_color, bg="#1e1e2f", width=100, anchor="w")
        drinksLbl.grid(column=0, row=5, columnspan=2, pady=20)

        # Hours Until Legal Label
        driveHoursLBL = Label(self, text="You can drive again in approximately: ", font=font_label, fg=accent_color, bg="#1e1e2f", width=100, anchor="w")
        driveHoursLBL.grid(column=0, row=6,columnspan=2,pady=20)
        
    #     # Calculate button action
        def clicked():
            if Male.get() != Female.get():
                if Male.get() == 1:
                    gender = "m"
                else:
                    gender = "f"
            
            # gender = genderForm.get().strip()
            weight = float(weightForm.get().strip())
            level = int(levelForm.get().strip())
            hours = float(hoursForm.get().strip())

            if not gender or not weight or not level:
                drinksLbl.configure(text="Please fill in all fields!", fg="#ff5722")  
                return

            try:
                bac = Calculations.CalculateBAC(level, hours)
                drinks = Calculations.CalculateDrinks(weight, gender, bac)
                hoursTillLegal = Calculations.CalculateHoursTillLegal(bac)
                drinksLbl.configure(
                    text=f"Drinks to be consumed: {drinks:.2f}"
                )
                driveHoursLBL.configure(
                    text=f"You can drive again in approximately: {hoursTillLegal:.2f} hours after last drink"
                )
            except ValueError:
                drinksLbl.configure(text="Invalid input. Please enter valid numbers.", fg="#ff5722")
        btn = Button(
                self,
                text="Calculate Drinks",
                command=clicked,
                font=font_button,
                bg=accent_color,
                fg="#1e1e2f",
                activebackground="#00acc1",
                activeforeground=text_color,
                width=20,
                bd=0,
                relief="flat",
                )
        btn.grid(column=0, row=4, columnspan=2, pady=20)







# def main(): 
    # root = Tk()
    

#     # Calculate Button
    

#     root.mainloop()

if __name__ == "__main__":
    # main()
    SafeSipApp = SafeSipApp()
    SafeSipApp.mainloop()
