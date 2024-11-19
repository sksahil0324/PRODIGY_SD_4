# PRODIGY_SD_4
```markdown
# Sudoku Solver

A simple Python program with a GUI that automatically solves Sudoku puzzles using the **backtracking algorithm**. The program allows users to input an unsolved Sudoku puzzle and solve it with a single click.

---

## Features

- **Sudoku Solver:** Automatically solves Sudoku puzzles using the backtracking algorithm.
- **User Input:** Allows users to input their own Sudoku puzzles in a 9x9 grid.
- **Graphical Interface:** Uses a Tkinter GUI for easy interaction.
- **Reset Functionality:** Clear the grid to enter a new puzzle.
- **Error Handling:** If the puzzle has no solution, an error message will be shown.

---

## Requirements

- Python 3.6 or higher
- `tkinter` (comes pre-installed with Python)

---

## Installation

1. Clone or download this repository.
2. Ensure Python is installed on your system:
   ```bash
   python --version
   ```

---

## Usage

1. **Run the Program:**
   ```bash
   python sudoku_solver_gui.py
   ```

2. **Input your Sudoku puzzle**:  
   Fill in the 9x9 grid with your Sudoku puzzle. Use `0` for empty cells.

3. **Solve the Puzzle**:  
   Click the **Solve** button. The program will automatically fill in the solution for you.

4. **Reset the Grid**:  
   Click the **Reset** button to clear all input cells and start with a new puzzle.

---

## How It Works

- The Sudoku puzzle is solved using the **backtracking algorithm**, a depth-first search approach that tries to place numbers in empty cells, checking for validity at each step.
- The algorithm backtracks when it hits a dead end and tries another number until the puzzle is solved.

---

## Screenshots

1. **Sudoku Solver Interface**:  
   ![Sudoku Solver](https://via.placeholder.com/500x300?text=Sudoku+Solver+Interface)

---

## File Details

- `sudoku_solver_gui.py`: Main program file that includes the Tkinter GUI and backtracking algorithm.

---

## Example

1. **Initial Interface:**  
   You will see a blank 9x9 grid where you can input your Sudoku puzzle.
   
2. **Input Puzzle:**  
   Fill the grid with the puzzle, leaving `0` for empty cells.

3. **Solve Puzzle:**  
   Click the **Solve** button to fill in the solution.

4. **Reset Puzzle:**  
   Click the **Reset** button to clear the grid and start a new puzzle.

---

## Contributing

Contributions are welcome! Feel free to fork this repository, make improvements, and submit a pull request.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

## Author

**Your Name**  
[GitHub Profile](https://github.com/sksahil0324)  
