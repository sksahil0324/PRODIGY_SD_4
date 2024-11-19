import tkinter as tk
from tkinter import messagebox

# Backtracking algorithm for solving Sudoku
def is_valid(board, row, col, num):
    # Check if the number is in the row
    for i in range(9):
        if board[row][i] == num:
            return False

    # Check if the number is in the column
    for i in range(9):
        if board[i][col] == num:
            return False

    # Check if the number is in the 3x3 sub-grid
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False

    return True

def solve(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:  # Find an empty cell
                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        if solve(board):
                            return True
                        board[row][col] = 0  # Backtrack
                return False
    return True

def solve_sudoku():
    # Get the current puzzle from the input grid
    board = []
    for i in range(9):
        row = []
        for j in range(9):
            try:
                num = int(entries[i][j].get())
                if num < 0 or num > 9:
                    raise ValueError
            except ValueError:
                num = 0  # Default to 0 if the input is invalid or empty
            row.append(num)
        board.append(row)

    # Solve the Sudoku puzzle
    if solve(board):
        for i in range(9):
            for j in range(9):
                entries[i][j].delete(0, tk.END)
                entries[i][j].insert(0, str(board[i][j]))
    else:
        messagebox.showerror("Error", "No solution exists!")

def reset_grid():
    for i in range(9):
        for j in range(9):
            entries[i][j].delete(0, tk.END)

# GUI Setup
root = tk.Tk()
root.title("Sudoku Solver")

frame = tk.Frame(root)
frame.grid(row=0, column=0, padx=10, pady=10)

entries = []

# Create a 9x9 grid of entry widgets for the Sudoku puzzle
for i in range(9):
    row_entries = []
    for j in range(9):
        entry = tk.Entry(frame, width=3, font=("Arial", 18), borderwidth=2, relief="solid", justify="center")
        entry.grid(row=i, column=j, padx=5, pady=5)
        row_entries.append(entry)
    entries.append(row_entries)

# Buttons for solving and resetting the grid
solve_button = tk.Button(root, text="Solve", font=("Arial", 14), command=solve_sudoku)
solve_button.grid(row=1, column=0, padx=10, pady=10)

reset_button = tk.Button(root, text="Reset", font=("Arial", 14), command=reset_grid)
reset_button.grid(row=2, column=0, padx=10, pady=10)

root.mainloop()
