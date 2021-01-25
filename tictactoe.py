import tkinter as tk

class Game:
    def reset(self):
        self.players = ("X", "O")
        self.currentTurn = 0
        self.grid = [
                ["", "", ""],
                ["", "", ""],
                ["", "", ""]
        ]
        self.moves = 0
        self.won = False

    def __init__(self):
        self.reset()
    def checkBoard(self):
        for row in self.grid:
            # check every row
            if row[0] and row[0] == row[1] and row[0] == row[2]:
                    return row[0]

        for i in range(3):
            # check every column
            if self.grid[0][i] and self.grid[0][i] == self.grid[1][i] and self.grid[0][i] == self.grid[2][i]:
                    return self.grid[0][i]
        # check both diagonals
        if self.grid[0][0] and self.grid[0][0] == self.grid[1][1] and self.grid[0][0] == self.grid[2][2]:
                return self.grid[0][0]
        if self.grid[0][2] and self.grid[0][2] == self.grid[1][1] and self.grid[0][2] == self.grid[2][0]:
            return self.grid[0][0]
        # if we are here there's no winner
        # if all 9 moves have been made then it's a draw
        if self.moves == 9:
            return "No one" # will be prepended to wins to = No one wins

    def makeMove(self, coords):
        if self.won:
            return
        x = coords[0]
        y = coords[1]
        if not self.grid[x][y]:
            self.grid[x][y] = self.getCurrentPlayer()
            self.moves += 1
            self.currentTurn = 0 if self.currentTurn == 1 else 1
            winner = self.checkBoard()
            if winner:
                self.won = True
                return winner + " wins!"
        else:
            return "Invalid move!"

    def getCurrentPlayer(self):
        return self.players[self.currentTurn]

class Window:
    def __init__(self):
        self.root = tk.Tk()
        self.game = Game()
        self.textVariable = tk.StringVar()
        self.textVariable.set(self.game.getCurrentPlayer() + "'s turn")
        self.header = tk.Label(self.root, textvariable=self.textVariable)
        self.ButtonGrid = tk.Frame(self.root)
        self.buttons = []
        self.buttonText = []
        for i in range(3):
            for j in range(3):
                self.buttonText.append(tk.StringVar())
                self.buttons.append(tk.Button(self.ButtonGrid, textvariable=self.buttonText[-1], command=lambda r=i, c=j:self.handleClick(r, c)).grid(row=i, column=j, ipadx=20, ipady=20))
        self.header.pack()
        self.ButtonGrid.pack()
        tk.Button(self.root, text="Reset", command=self.reset).pack()
    def reset(self):
        self.game.reset()
        self.updateGrid()
        self.textVariable.set(self.game.getCurrentPlayer() + "'s turn")
    def updateGrid(self):
        index = 0
        for row in range(3):
            for col in range(3):
                self.buttonText[index].set(self.game.grid[row][col])
                index += 1

    def handleClick(self, row, col):
        result = self.game.makeMove((row, col))
        if result:
            self.textVariable.set(result)
        self.updateGrid()
    def loop(self):
        self.root.mainloop()

window = Window()
window.loop()
