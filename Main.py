import tkinter
import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")  

app = customtkinter.CTk()
app.geometry("700x500")
def button_function():
    print("button pressed")

button = customtkinter.CTkButton(master=app, text="Hello World",command=button_function, fg_color="white", text_color="black")
button.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

app.mainloop()