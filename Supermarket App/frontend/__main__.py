import customtkinter

class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        self.geometry("1080x800")
        self.title("Super Market App")
        self.minsize(500, 300)

        # create grid
        self.grid_rowconfigure(0, weight=5 )
        self.grid_columnconfigure((0, 1), weight=1)

if __name__ == "__main__" :
    app = App()

    app.mainloop()
