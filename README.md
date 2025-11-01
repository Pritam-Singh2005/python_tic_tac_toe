# ❌🅾️ Python Tic-Tac-Toe: Unbeatable AI Edition 🏆

---

## ✨ Overview

Welcome to a classic game of **Tic-Tac-Toe** built in Python! This is not just any game; it features a sleek, colorful command-line interface and an **Unbeatable AI** powered by the **Minimax algorithm**. You can choose to play against another human, a basic random-move AI, or challenge the ultimate Computer Player that will never lose!

This project utilizes the `colorama` library to bring vibrant colors and styles to the terminal experience.



---

## 🚀 Features

* **Three Game Modes:**
    * **Player vs Player:** Classic two-human game.
    * **Player vs Computer (Easy):** A relaxed game against an AI that makes random moves.
    * **Player vs Computer (Impossible):** Challenge the **Unbeatable AI** using the **Minimax algorithm**. The best you can do is tie!
* **Vibrant UI:** Utilizes **`colorama`** for a colorful and engaging terminal display, including a neatly aligned board and colored game messages.
* **Clear Board Representation:** The game board shows **current moves (X/O)** and an auxiliary board clearly displays the **numeric positions (0-8)** for easy input.
* **Win/Tie Detection:** Immediately announces the winner or a tie.

---

## 🛠️ Prerequisites

To run this game, you need **Python 3** installed.

The game also relies on the `colorama` library for the colorful output.

### 📦 Installation

1.  **Clone the repository** (if hosted, otherwise ensure the file is saved as a Python file, e.g., `tictactoe.py`):
    ```bash
    # Assuming you have it in a file called tictactoe.py
    ```

2.  **Install the required library:**
    ```bash
    pip install colorama
    ```

---

## 🎮 How to Play

1.  **Run the game from your terminal:**
    ```bash
    python tictactoe.py
    ```

2.  **Choose a game mode** (1, 2, or 3) from the main menu.
3.  The game will display the board and the available move numbers (0-8).
4.  When prompted, **enter the number (0-8)** of the square where you want to place your mark.
5.  If you choose the "Impossible" AI, prepare for a tough challenge!

---

## 🧠 The Unbeatable AI (Minimax)

The **`ComputerPlayer`** class implements the **Minimax algorithm** to determine the optimal move.

* **How it Works:** Minimax is a recursive algorithm used for decision-making in two-player games.
    * It **maximizes** the score for the AI player.
    * It **minimizes** the score for the opponent.
* The scoring in the code is strategically done by adding the number of empty squares remaining (`state.num_empty_squares() + 1`) to the base score. This incentivizes the AI to win **faster** and lose **slower** when possible, ensuring it finds the most optimal path to victory or a draw.

---

## 💡 Code Structure Highlights

| Class / Function | Description |
| :--- | :--- |
| `TicTacToe` | Manages the game state, board manipulation, and checking for winners. |
| `Player` / `HumanPlayer` | Base class for players and handles human input with validation. |
| **`ComputerPlayer`** | Extends `Player` and contains the core **Minimax logic** for the impossible AI. |
| `play(game, ...)` | The main game loop function that controls player turns and game flow. |
| `main()` | Handles the main menu, mode selection, and game setup/loop. |

---

## 🤝 Contributing

Feel free to fork this project, suggest improvements, or submit pull requests. All feedback is welcome!
