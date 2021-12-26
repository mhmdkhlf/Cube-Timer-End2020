import tkinter as tk

class PuzzleSelector:
    def __init__(self, puzzle):
        self.window = tk.Tk()
        self.selected_cube = tk.StringVar()
        self.selected_cube.set(puzzle)

        self.head = tk.Frame(self.window)
        self.message = tk.Label(self.head, text='close window after selecting puzzle')
        self.message.pack()
        self.head.pack()

        self.small_cube = tk.Frame(self.window)
        self.rb2 = tk.Radiobutton(self.small_cube, text='2x2 Cube', variable=self.selected_cube, value='2x2')
        self.rb3 = tk.Radiobutton(self.small_cube, text='3x3 Cube', variable=self.selected_cube, value='3x3')
        self.rb2.pack(side='left')
        self.rb3.pack(side='right')
        self.small_cube.pack()

        self.big_cube = tk.Frame(self.window)
        self.rb4 = tk.Radiobutton(self.big_cube, text='4x4 Cube', variable=self.selected_cube, value='4x4')
        self.rb5 = tk.Radiobutton(self.big_cube, text='5x5 Cube', variable=self.selected_cube, value='5x5')
        self.rb4.pack(side='left')
        self.rb5.pack(side='right')
        self.big_cube.pack()

        self.dodecahedron = tk.Frame(self.window)
        self.megaminx = tk.Radiobutton(self.dodecahedron, text='Megaminx', variable=self.selected_cube, value='megaminx')
        self.megaminx.pack()
        self.dodecahedron.pack()

        tk.mainloop()

    def get_choice(self):
        return self.selected_cube.get()