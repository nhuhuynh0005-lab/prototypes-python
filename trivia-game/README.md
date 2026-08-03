## Overview

A simple CLI trivia game. The program will randomly pick 10 questions from a question bank (provided by this guide) and print out the prompt and a list of choices. The user will input the choice they think is correct. After all questions are answered, the number of correct questions answered is printed out.

## Goals

- Understand how to use classes in Python.
- Understand object-oriented design and how it helps.

## How to use this guide

- Run sample program: `python3 trivia-game/soln/main.py`.
- Run your program: `python3 trivia-game/main.py`.
- Make changes to `trivia-game/main.py`. Inside the file, there's a `DO NOT TOUCH` block, which loads the question bank from a JSON file.
- The first choice is the correct choice in the question bank.
- The final program doesn't need to be strictly the same as the sample one. Feel free to customize areas like messages as you see fit.
- Feel free to use:
    - Search engines
    - Python's built-in libraries
- Refrain from using:
    - AI tools

## Stages

1. Understand the shape of `raw_questions`'s elements. Print the first question to stdout as follows.
    ```sh
    $ python3 trivia-game/main.py
    What is 5 plus 7?
    1. 12
    2. 11
    3. 13
    4. 10
    ```
2. Store the previous code somewhere. Modify the program so that it displays a prompt symbol (`>`) and waits for user input. When the user presses `Enter`, the next prompt symbol should be displayed. Ctrl+C should exit the program.
    ```sh
    $ python3 trivia-game/main.py
    >
    >
    >
    >
    ```

3. Modify the program to continuously accept shell inputs and print the user inputs to stdout.
    ```sh
    $ python3 trivia-game/main.py
    > hello
    You typed: hello
    > world
    You typed: world
    ```
4. Modify the program to print the first 10 questions in the same format as step (1) and exit. After each question, wait for user input. Only display the next question once the user presses `Enter`.
    ```sh
    $ python3 trivia-game/main.py
    What is 5 plus 7?
    1. 12
    2. 11
    3. 13
    4. 10
    >
    How many sides does a triangle have?
    1. 3
    2. 4
    3. 5
    4. 2
    >
    ```
5. Process user input and print out whether the user picks the correct / incorrect option.
    ```sh
    $ python3 trivia-game/main.py
    What is 5 plus 7?
    1. 12
    2. 11
    3. 13
    4. 10
    > 1
    ✅ Correct
    How many sides does a triangle have?
    1. 3
    2. 4
    3. 5
    4. 2
    > 2
    ❌ Incorrect
    ```
6. Keep track of the score and print it out at the end.
    ```sh
    $ python3 trivia-game/main.py
    ...
    How many sides does a triangle have?
    1. 3
    2. 4
    3. 5
    4. 2
    > 2
    ❌ Incorrect
    Your score is 5/10.
    ```
7. Randomize the order of the choices so that the first choice is no longer always the correct choice.
8. Randomly sample 10 questions from the question bank instead of always printing out the first 10.

## Extra features

- Print out different final message depending on user score (Easy).
- Allow customization of the number of questions (Easy).
- Add a main menu to start / exit the game (Medium).
- Support more types of questions: yes / no, "fill in the blank", multiple select, ... (Medium).
- Keep a leaderboard (Hard).
- Allow customization of difficulty and genres of the questions (Hard).