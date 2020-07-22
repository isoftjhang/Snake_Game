# Snake Game

This is a classic Snake game developed in Python. The game allows players to control a snake that grows in length as it consumes food, while avoiding collisions with the walls and itself.

## Project Structure

```
snake-game
├── src
│   ├── main.py          # Entry point of the game
│   ├── game
│   │   ├── __init__.py  # Game package initialization
│   │   ├── snake.py     # Snake class for managing the snake's behavior
│   │   ├── food.py      # Food class for managing food spawning
│   │   ├── obstacle.py  # Obstacle manager for spawning hazards
│   │   └── board.py     # Board class for managing the game board
│   └── utils
│       └── __init__.py  # Utils package initialization
├── requirements.txt      # Project dependencies
├── README.md             # Project documentation
└── .gitignore            # Files to ignore in version control
```

## Requirements

To run this game, you need to have Python installed along with the required libraries. You can install the dependencies listed in `requirements.txt` using pip:

```
pip install -r requirements.txt
```

## How to Run the Game

1. Clone the repository or download the project files.
2. Navigate to the project directory.
3. Run the game using the following command:

```
python src/main.py
```

## Additional Information

This version includes several improvements:
- Start screen with instructions
- Difficulty selection on the menu (Easy / Medium / Hard)
- Obstacle hazards that appear as your level increases
- Pause support with the `P` key
- Level progression as your score increases
- High score persistence across runs
- Cleaner board UI with score, level, difficulty, and high score display

Feel free to modify the code to add new features or improve the game mechanics. Enjoy playing!