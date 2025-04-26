import tkinter as tk

class Counter(tk.Tk):
    def __init__(self):
        super().__init__()
        self.counter = 0
        self.title("Click Counter")
        
        self.label = tk.Label(self, text="Clicks: 0", font=("Arial", 24))
        self.label.pack(pady=20)

        self.button = tk.Button(self, text="CLICK ME", font=("Arial", 12), command=self.increment)
        self.button.pack()

    def increment(self):
        self.counter += 1
        self.label.config(text=f'Clicks: {self.counter}')

if __name__ == "__main__":
    counter = Counter()
    counter.mainloop()
