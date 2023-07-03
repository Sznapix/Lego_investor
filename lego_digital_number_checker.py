import tkinter
import main





root = tkinter.Tk()
root.geometry("970x700")
root.title("Lego investor")

def adding_to_db():
    window_with_text = tkinter.Label(root, text = main.the_best_offer())
    window_with_text.grid(row=1,column=0)

button_adding_to_db = tkinter.Button(root,text="Download offers to the database", font=("Arial",13), command=adding_to_db).grid(row=0,column=0, padx=6)
show_offers_from_db = tkinter.Button(root,text="Show all offers from the database", font=("Arial",13)).grid(row=0,column=1, padx=6)
show_the_best_offers_from_db = tkinter.Button(root, text="Show the best lego offers ", font=("Arial",13)).grid(row=0,column=2, padx=6)
clear_the_db = tkinter.Button(root,text="clear your database", font=("Arial",13)).grid(row=0,column=3, padx=6)
exit = tkinter.Button(root,text="Exit", font=("Arial",13)).grid(row=0,column=4, padx=6)



root.mainloop()