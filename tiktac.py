import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, master):
        self.master = master
        master.title("Tic-Tac-Toe")
        master.geometry("300x350")

        self.current_player = "X"
        self.buttons = [[None]*3 for _ in range(3)]

        self.label = tk.Label(master, text=f"Player {self.current_player}'s turn", font=('Arial', 14))
        self.label.pack(pady=10)

        self.frame = tk.Frame(master)
        self.frame.pack()

        for row in range(3):
            for col in range(3):
                btn = tk.Button(self.frame, text="", font=('Arial', 24), width=5, height=2,
                                command=lambda r=row, c=col: self.on_click(r, c))
                btn.grid(row=row, column=col)
                self.buttons[row][col] = btn

        self.reset_btn = tk.Button(master, text="Reset Game", command=self.reset_game)
        self.reset_btn.pack(pady=10)

    def on_click(self, row, col):
        btn = self.buttons[row][col]
        if btn["text"] == "":
            btn["text"] = self.current_player
            if self.check_winner():
                messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
                self.disable_buttons()
            elif self.check_draw():
                messagebox.showinfo("Game Over", "It's a draw!")
                self.disable_buttons()
            else:
                self.switch_player()
        else:
            messagebox.showwarning("Invalid Move", "This cell is already taken!")

    def switch_player(self):
        self.current_player = "O" if self.current_player == "X" else "X"
        self.label.config(text=f"Player {self.current_player}'s turn")

    def check_winner(self):
        b = self.buttons
        # Check rows
        for row in range(3):
            if b[row][0]["text"] == b[row][1]["text"] == b[row][2]["text"] != "":
                return True
        # Check columns
        for col in range(3):
            if b[0][col]["text"] == b[1][col]["text"] == b[2][col]["text"] != "":
                return True
        # Check diagonals
        if b[0][0]["text"] == b[1][1]["text"] == b[2][2]["text"] != "":
            return True
        if b[0][2]["text"] == b[1][1]["text"] == b[2][0]["text"] != "":
            return True
        return False

    def check_draw(self):
        for row in self.buttons:
            for btn in row:
                if btn["text"] == "":
                    return False
        return True

    def disable_buttons(self):
        for row in self.buttons:
            for btn in row:
                btn.config(state="disabled")

    def reset_game(self):
        self.current_player = "X"
        self.label.config(text=f"Player {self.current_player}'s turn")
        for row in self.buttons:
            for btn in row:
                btn.config(text="", state="normal")

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
