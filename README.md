![Pathfind-RL](images/pathfind-rl.png)

Welcome to Pathfind-RL.

This project aims to explore reinforcement learning techniques for pathfinding in a grid-based environment.  It uses Pygame for visualization and a custom sprite handling system.

## Overview

The project currently consists of two main components:

1.  **Sprite Generation:**  The `spritemaker()` function (in `main.py`) processes sprite sheets located in the `assets/` directory. It extracts individual sprites, indexes them, and saves the index for later use. This allows the game to easily load and display sprites from the sheets.  The `SpriteMaker` class (in `utils/getsprites.py`) handles the sprite sheet processing.

2.  **Game Loop and Grid Visualization:** The `gameloop()` function (in `main.py`) initializes a Pygame window and creates a `GameGrid` object (from `utils/grid.py`).  The game loop handles basic events (like closing the window) and draws the grid on the screen.  The `GameGrid` class manages the grid's dimensions, tile size, and rendering.

## Getting Started

### Prerequisites

- Python 3.12
- Conda or Python-venv (to manage virtual environments)

### Installation

1.  Clone the repository:

```bash
git clone https://github.com/JustSurWHYving/pathfind-rl.git
```
2.  Install the required packages:
```bash
pip install -r requirements.txt
```
### Usage
1.  Run the main script:
```bash
python main.py
```
2.  The game window will open, displaying a grid.
