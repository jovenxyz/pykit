# tictactoe

A tiny, dependency-free **tic-tac-toe** engine with a perfect-play AI
based on the **negamax** algorithm (a symmetric variant of minimax).

## Usage

```python
from tictactoe import O, X, best_move, empty_board, play, winner

board = empty_board()
board = play(board, (1, 1), X)
board = play(board, best_move(board, O), O)

print(winner(board))    # None, X, or O
```

``best_move`` always plays optimally. Boards are immutable from the
caller's perspective -- ``play`` returns a new board.

## Tests

```bash
cd tictactoe
pytest
```
