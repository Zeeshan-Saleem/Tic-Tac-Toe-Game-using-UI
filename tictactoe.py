import tkinter as tk

class TicTacToeUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Tic Tac Toe")
        self.current_player = "X"
        self.board = [""] * 9
        self.create_widgets()

    def create_widgets(self):
        # create the 3x3 grid of buttons for the game board
        self.buttons = []
        for i in range(3):
            row = []
            for j in range(3):
                button = tk.Button(self.master, width=4, height=2, font=("Helvetica", 32), command=lambda i=i, j=j: self.on_button_click(i, j))
                button.grid(row=i, column=j)
                row.append(button)
            self.buttons.append(row)

        # create the "New Game" button
        self.new_game_button = tk.Button(self.master, text="New Game", command=self.new_game)
        self.new_game_button.grid(row=3, column=1)

        # create the label to display the current player
        self.current_player_label = tk.Label(self.master, text=f"Current Player: {self.current_player}", font=("Helvetica", 16))
        self.current_player_label.grid(row=4, column=1)

    def on_button_click(self, i, j):
        if self.board[3*i + j] == "":
            self.board[3*i + j] = self.current_player
            self.buttons[i][j].config(text=self.current_player)
            winner = self.check_for_winner()
            if winner:
                self.current_player_label.config(text=f"Winner: {winner}")
                self.disable_buttons()
            elif self.board.count("") == 0:
                self.current_player_label.config(text="It's a tie!")
                self.disable_buttons()
            else:
                self.switch_players()

    def check_for_winner(self):
        winning_positions = [
            [0, 1, 2],
            [3, 4, 5],
            [6, 7, 8],
            [0, 3, 6],
            [1, 4, 7],
            [2, 5, 8],
            [0, 4, 8],
            [2, 4, 6]
        ]
        for pos in winning_positions:
            if self.board[pos[0]] == self.board[pos[1]] == self.board[pos[2]] != "":
                return self.board[pos[0]]
        return None

    def switch_players(self):
        if self.current_player == "X":
            self.current_player = "O"
        else:
            self.current_player = "X"
        self.current_player_label.config(text=f"Current Player: {self.current_player}")

    def disable_buttons(self):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(state=tk.DISABLED)

    def new_game(self):
        self.current_player = "X"
        self.board = [""] * 9
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text="", state=tk.NORMAL)
        self.current_player_label.config(text=f"Current Player: {self.current_player}")

if __name__ == "__main__":
    root = tk.Tk()
    TicTacToeUI(root)
    root.mainloop()