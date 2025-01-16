from tkinter import Tk, Label, Entry, Button, StringVar
import Calculations

def main(): 
    root = Tk()
    root.title("SafeSip - Drink Calculator")
    root.geometry('800x400')
    root.configure(bg="#1e1e2f")  

    font_label = ("Helvetica", 12, "bold")
    font_entry = ("Helvetica", 12)
    font_button = ("Helvetica", 14, "bold")
    text_color = "#f5f5f5"
    accent_color = "#00bcd4"

    # Gender Label and Entry
    genderLbl = Label(root, text="Enter Gender (M/F):", font=font_label, fg=text_color, bg="#1e1e2f", width=20, anchor="e")
    genderLbl.grid(column=0, row=0, pady=10, padx=10)
    genderForm = Entry(root, font=font_entry, bg="#33334d", fg=text_color, insertbackground=text_color, width=15)
    genderForm.grid(column=1, row=0, pady=10, padx=10)

    # Weight Label and Entry
    weightLbl = Label(root, text="Enter Weight (lbs):", font=font_label, fg=text_color, bg="#1e1e2f", width=20, anchor="e")
    weightLbl.grid(column=0, row=1, pady=10, padx=10)
    weightForm = Entry(root, font=font_entry, bg="#33334d", fg=text_color, insertbackground=text_color, width=15)
    weightForm.grid(column=1, row=1, pady=10, padx=10)

    # Level Label and Entry
    levelLbl = Label(root, text="Enter What Level of Intoxication\nYou Would Like to Achieve (1-10):", font=font_label, fg=text_color, bg="#1e1e2f", width=26, anchor="e")
    levelLbl.grid(column=0, row=2, pady=10, padx=10)
    levelForm = Entry(root, font=font_entry, bg="#33334d", fg=text_color, insertbackground=text_color, width=15)
    levelForm.grid(column=1, row=2, pady=10, padx=10)

    # Drinks Result Label
    drinksLbl = Label(root, text="Drinks to be consumed in one hour:", font=font_label, fg=accent_color, bg="#1e1e2f", width=100, anchor="w")
    drinksLbl.grid(column=0, row=4, columnspan=2, pady=20)

    # Hours Until Legal Label
    hoursLBL = Label(root, text="You can drive again in approximately: ", font=font_label, fg=accent_color, bg="#1e1e2f", width=100, anchor="w")
    hoursLBL.grid(column=0, row=5,columnspan=2,pady=20)
    # Calculate button action
    def clicked():
        gender = genderForm.get().strip()
        weight = float(weightForm.get().strip())
        level = int(levelForm.get().strip())

        if not gender or not weight or not level:
            drinksLbl.configure(text="Please fill in all fields!", fg="#ff5722")  
            return

        try:
            bac = Calculations.CalculateBAC(level)
            drinks = Calculations.CalculateDrinks(weight, gender, bac)
            hoursTillLegal = Calculations.CalculateHoursTillLegal(bac)
            drinksLbl.configure(
                text=f"Drinks to be consumed in one hour: {drinks:.2f} drinks to reach level {level}",
                fg=accent_color
            )
            hoursLBL.configure(
                text=f"You can drive again in approximately: {hoursTillLegal:.2f} hours"
            )
        except ValueError:
            drinksLbl.configure(text="Invalid input. Please enter valid numbers.", fg="#ff5722")

    # Calculate Button
    btn = Button(
        root,
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
    btn.grid(column=0, row=3, columnspan=2, pady=20)

    root.mainloop()

if __name__ == "__main__":
    main()
