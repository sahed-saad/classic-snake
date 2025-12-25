# Classic Snake Game 🐍🍎

A beginner-friendly implementation of the classic Snake game using Python's turtle graphics module. Control a growing snake as it hunts for apples while avoiding the boundaries of the game window.

## Features

- **Growing snake**: Your snake gets longer with each apple consumed
- **Progressive difficulty**: Speed increases as your score goes up
- **Score tracking**: Real-time score display in the corner
- **Custom shapes**: Apple and snake rendered with turtle graphics
- **Smooth controls**: Arrow key navigation with directional constraints

## How to Play

### Installation

1. Clone this repository:
```bash
git clone https://github.com/sahed-saad/classic-snake.git
cd classic-snake
```

2. Make sure you have Python 3.x installed (turtle module comes built-in)

### Running the Game
```bash
python snake.py
```

### Controls

| Key | Action |
|-----|--------|
| **SPACE** | Start the game |
| **↑** | Move up |
| **↓** | Move down |
| **←** | Move left |
| **→** | Move right |

### Gameplay Rules

1. Press **SPACE** to begin
2. Use arrow keys to guide your snake toward the red apples
3. Each apple eaten:
   - Increases your score by 10 points
   - Makes your snake longer
   - Speeds up the game slightly
4. Avoid hitting the yellow walls which is game over!
5. The snake can only turn 90 degrees (no reversing into yourself)

## Requirements

- Python 3.x
- turtle module (included with standard Python installation)
- No additional packages needed!

## Game Mechanics

- **Starting length**: 3 units
- **Starting speed**: 2 pixels per frame
- **Score per apple**: 10 points
- **Speed increase**: +1 per apple
- **Length increase**: +1 unit per apple

## Screenshots

The game features a bright yellow background with an orange snake and red apples. Score is displayed in the top-right corner.

## Learning Points

This project demonstrates:
- Basic Python game loops
- Event handling with keyboard input
- Random positioning
- Turtle graphics manipulation
- Game state management

## Future Improvements

Potential features to add:
- Self-collision detection (snake hitting its own body)
- Levels with obstacles
- High score persistence
- Pause functionality
- Sound effects
- Multiple difficulty modes

## License

Feel free to use and modify this code for learning purposes.

## Contributing

This is a beginner project, but suggestions and improvements are welcome! Feel free to open an issue or submit a pull request.