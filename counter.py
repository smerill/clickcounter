import tkinter as tk
import json
from pathlib import Path

HIGHSCORE_FILE = Path("highscore.json")

if HIGHSCORE_FILE.exists():
    try:
        data = json.loads(HIGHSCORE_FILE.read_text())
        highscore = data.get("highscore", 0)
    except json.JSONDecodeError:
        highscore = 0
else:
    highscore = 0

class Counter(tk.Tk):
    def __init__(self):
        super().__init__()
        self.session_counter = 0
        self.highscore = highscore
        self.title("Click Counter")
        
        self.label_click = tk.Label(self, text="Clicks: 0", font=("Arial", 24))
        self.label_click.pack(pady=20)

        self.button = tk.Button(self, text="CLICK ME", font=("Arial", 12), command=self.increment)
        self.button.pack()
        
        self.label_highscore = tk.Label(self, text=f"Highscore: {self.highscore}", font=("Arial", 8))
        self.label_highscore.pack()
        
        self.protocol("WM_DELETE_WINDOW", self.on_close)

    def increment(self):
        self.session_counter += 1
        self.label_click.config(text=f'Clicks: {self.session_counter}')
        self.check_highscore()

    def check_highscore(self):
        if self.session_counter > self.highscore:
            self.highscore = self.session_counter
            self.label_highscore.config(text=f'Highscore: {self.highscore}')
            

    def on_close(self):
        HIGHSCORE_FILE.write_text(json.dumps({"highscore": self.highscore}))
        self.destroy()
            

if __name__ == "__main__":
    counter = Counter()
    counter.mainloop()
