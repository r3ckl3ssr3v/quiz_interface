# KBC Quiz Game

This project is a text-based quiz game inspired by the popular TV show "Kaun Banega Crorepati" (KBC). The game asks multiple-choice questions, and the player earns increasing amounts of money as they answer correctly. If the player gives a wrong answer, the game ends, and they take home the last milestone amount they achieved.

## How to Play

1. Run the program.
2. Press enter to start the game.
3. You will be presented with a series of questions, each having four options (a, b, c, d).
4. Input the number (1-4) corresponding to the correct answer.
5. For each correct answer, you win a certain amount of virtual money based on the level you are on.
6. The game ends if you give an incorrect answer, and you take home the last achieved milestone prize.

## Questions

The game consists of the following questions:

1. **What is the capital of India?**
2. **Who's the first president of India?**
3. **Who's the CEO of Google?**
4. **In which language was Facebook created?**
5. **Who let the ____ out?**

The prize levels are:

- ₹1000
- ₹2000
- ₹4000
- ₹8000
- ₹16000
- ₹32000

## Code Breakdown

The program consists of a `KBC()` function, which:

- Defines the list of questions and their correct answers.
- Tracks the user's progress through a loop.
- Prompts the user for input and checks the answer.
- Ends the game when the user gives an incorrect answer.

## Running the Project

To run the project:

1. Clone this repository.
2. Run the code in any Python environment (Python 3+).
   ```bash
   python kbc_game.py
