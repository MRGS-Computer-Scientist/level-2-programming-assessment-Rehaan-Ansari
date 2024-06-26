from tkinter import *
from PIL import Image, ImageTk
import os

class App:
    def __init__(self):
        self.window = Tk()
        self.window.title("TownTalk")

        # Maximize the window
        self.window.state('zoomed')

        # Load the background image
        image_path = os.path.join(os.path.dirname(__file__), "images", "I1.png")
        self.bg_image = Image.open(image_path)

        # Create a label for the background image
        self.bg_label = Label(self.window)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Function to resize the background image
        self.resize_bg_image()

        # Bind the resize event
        self.window.bind("<Configure>", self.resize_bg_image)

        ########## TOP FRAME #############
        self.top_frame = Frame(self.window, background='#004080', height=80)
        self.top_frame.pack(side=TOP, fill=X)

        title_label = Label(self.top_frame, text="TownTalk", font=("Verdana", 30, "bold"), bg='#004080', fg='white')
        title_label.pack(pady=(15, 0))

        ########## WELCOME TEXT SECTION #############
        welcome_text_frame = Frame(self.window, bg='white', highlightbackground='#ffffff', highlightthickness=1, bd=0)
        welcome_text_frame.place(relx=0.3, rely=0.5, anchor=CENTER, width=500, height=400)

        welcome_text_section = Frame(welcome_text_frame, bg='white', padx=20, pady=20)
        welcome_text_section.pack(fill=BOTH, expand=True)

        subtitle = ("Welcome to TownTalk, your hub for local connections and collaboration! Stay in the loop with "
                    "upcoming events, chat with neighbors, and join exciting group projects. Get involved, stay "
                    "informed, and make a difference in your community today!")
        subtitle_label = Label(welcome_text_section, text=subtitle, font=("Verdana", 16), wraplength=460, justify=LEFT, bg='white')
        subtitle_label.pack(expand=True, fill=BOTH)

        ########## LOGIN SECTION #############
        login_section_frame = Frame(self.window, bg='white', highlightbackground='#ffffff', highlightthickness=1, bd=0)
        login_section_frame.place(relx=0.7, rely=0.5, anchor=CENTER, width=400, height=500)

        login_section = Frame(login_section_frame, bg='white', padx=20, pady=20)
        login_section.pack(fill=BOTH, expand=True)

        discover_label = Label(login_section, text="Discover your town", font=("Verdana", 20, "bold"), bg='white')
        discover_label.pack(pady=10)

        guest_button = Button(login_section, text="Continue as Guest", font=("Verdana", 14), width=25, bg='#004080', fg='white', relief=FLAT)
        guest_button.pack(pady=5)

        or_label = Label(login_section, text="OR", font=("Verdana", 14), bg='white')
        or_label.pack(pady=10)

        self.email_entry = Entry(login_section, font=("Verdana", 14), width=30, fg='grey', bg='#f0f0f0')
        self.email_entry.pack(pady=5)
        self.email_entry.insert(0, "Email address")
        self.email_entry.bind("<FocusIn>", lambda event: self.clear_placeholder(event, "Email address"))
        self.email_entry.bind("<FocusOut>", lambda event: self.restore_placeholder(event, "Email address"))

        self.password_entry = Entry(login_section, font=("Verdana", 14), width=30, fg='grey', bg='#f0f0f0')
        self.password_entry.pack(pady=5)
        self.password_entry.insert(0, "Password")
        self.password_entry.bind("<FocusIn>", lambda event: self.clear_placeholder(event, "Password"))
        self.password_entry.bind("<FocusOut>", lambda event: self.restore_placeholder(event, "Password"))

        continue_button = Button(login_section, text="Continue", font=("Verdana", 14), width=25, bg='#004080', fg='white')
        continue_button.pack(pady=20)

        self.window.mainloop()

    def resize_bg_image(self, event=None):
        # Get the window size
        window_width = self.window.winfo_width()
        window_height = self.window.winfo_height()

        # Resize the background image
        resized_bg_image = self.bg_image.resize((window_width, window_height))
        self.bg_photo = ImageTk.PhotoImage(resized_bg_image)

        # Update the label with the resized image
        self.bg_label.config(image=self.bg_photo)

    def clear_placeholder(self, event, placeholder):
        if event.widget.get() == placeholder:
            event.widget.delete(0, END)
            event.widget.config(fg='black', show='')

    def restore_placeholder(self, event, placeholder):
        if not event.widget.get():
            event.widget.insert(0, placeholder)
            event.widget.config(fg='grey', show='*' if placeholder == "Password" else '')


if __name__ == "__main__":
    app = App()