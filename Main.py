import customtkinter
from Components import Containter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

app = customtkinter.CTk(fg_color="black")
app.wm_attributes("-fullscreen", True)

Containter.Ejecution(app)


app.mainloop()
