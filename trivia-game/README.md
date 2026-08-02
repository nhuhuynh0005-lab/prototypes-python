overview
- a simple CLI trivia game. the program will randomly pick 10 questions from a question bank (provided by this guide) and prints out the prompt and a list of choice. the user will input the choice they think are correct. After all questions are answered, the number of correct questions answered is printed out.
- the first choice is the correct choice in the question bank.

how to use this guide
- commands should be run from root project directory.
- run sample programs using `python3 trivia-game/soln/main.py` to understand the expected output.
- feel free to use any search engine.
- ai usage should be refrained.
- feel free to use any python built-in libraries.
- make changes to `trivia-game/main.py`.

stages
1. Understand the shape of `raw_questions`'s element. Print the first question to stdout as follow.
    ```sh
    $ python3 trivia-game/main.py
    What do plants take in that people breathe out?
    1. Carbon dioxide
    2. Oxygen
    3. Hydrogen
    4. Neon
    ```
2. Store the previous code somewhere. Modify the program so that it displays a prompt symbol (`>`) and waits for user input. When user presses `Enter`, the next prompt symbol should be displayed. Ctrl+C should exit the program.
    ```sh
    $ python3 trivia-game/main.py
    >
    >
    >
    >
    ```

3. Modify the program to continuously accepts shell inputs and print the user inputs to stdout.
    ```sh
    $ python3 trivia-game/main.py
    > hello
    You typed: hello
    > world
    You typed: world
    ```
4. Modify the program to print the first 10 questions in the same format as step (1) and exit. After each question, wait for user input. Only displays the next question once the user presses "enter".
    ```sh
    $ python3 trivia-game/main.py
    What do plants take in that people breathe out?
    1. Carbon dioxide
    2. Oxygen
    3. Hydrogen
    4. Neon
    >
    The Vietnamese dessert 'che' is best described as what?
    1. A sweet soup or pudding with beans, jelly, and coconut milk
    2. A savory grilled skewer
    3. A fried spring roll
    4. A rice noodle salad
    >
    ```
5. processes user input and print out whether the user picks the correct / incorrect option.
    ```sh
    $ python3 trivia-game/main.py
    What do plants take in that people breathe out?
    1. Carbon dioxide
    2. Oxygen
    3. Hydrogen
    4. Neon
    > 1
    ✅ Correct
    The Vietnamese dessert 'che' is best described as what?
    1. A sweet soup or pudding with beans, jelly, and coconut milk
    2. A savory grilled skewer
    3. A fried spring roll
    4. A rice noodle salad
    > 2
    ❌ Incorrect
    ```
7. Randomizes the order of the choice, so that the first choice is no longer always the correct choice.
8. Randomly sample 10 questions from the question banks instead of always printing out the first 10.
9. Keep track of the score and print it out at the end.
    ```sh
    $ python3 trivia-game/main.py
    ...
    The Vietnamese dessert 'che' is best described as what?
    1. A sweet soup or pudding with beans, jelly, and coconut milk
    2. A savory grilled skewer
    3. A fried spring roll
    4. A rice noodle salad
    > 2
    ❌ Incorrect
    Your score is 5/10.
    ```

Extra features:
- support yes / no, "fill in the blank" questions.
- customize number of questions, difficulty, genres, ...
- add a main menu to start / restart the game.
- keep a leaderboard.
- print different final message depending on the score.