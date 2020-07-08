#   The Impossible Chessboard

##  Tasks

The task is to solve and strategize the following situation of **2 Prisoners** and a **Warden**:

1. A **Warden** will set up a chessboard with size of *n x n* and place coins on all of the board with either Head or Tails (1 or 0)
2. **Warden** will let `Prisoner 1` in the room and will place a key under one of the board of the n x n chessboard.
3. `Prisoner 1` has to flip one of the coin on the chessboard (`Prisoner 1` knows where the key is)
4. `Prisoner 1` then go out to separate room and isolated.
5. `Prisoner 2` go in the room with the **warden** adn the chessboard and see the new board with one of the coin flipped by `Prisoner 1`
6. `Prisoner 2` ***DOES NOT*** know where the key is nor which coin that is flipped.
7. `Prisoner 2` has to deduct based on the board where the guard put the key.

For more details refer to 3Blue1Brown's video [here](https://www.youtube.com/watch?v=wTJI_WuZSwE&t=3s)

##  Usage

To just start an easy simulation, do the below. You can change the settings if needed.

```bash
git clone https://github.com/T-kON99/Impossible-Chessboard-Solver.git Solver
cd Solver
python Game.py
```
