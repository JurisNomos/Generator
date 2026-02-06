# Generator

[繁體中文](./README.zh-tw.md)

This project is a command-line utility that creates secure passwords based on user input. It allows users to specify the desired length, and the program randomly mixes letters, numbers, and symbols to ensure high entropy (randomness).

Use this project to practice Python fundamentals, specifically string manipulation and utilizing built-in libraries.

## Features
- **Customizable Length:**: User can input the exact number of characters.
- **Secure Randomization:**: Uses Python's `random` module for unpredictable results.
- **Instant Output:**: Generates and displays the password immediately.
- **Error Handling:**: Ensures the user enters a valid number for length.

## Run
1. Ensure you have Python installed.

   ```bash
   python3 -V
   ```

2. Download or clone this repository.

   ```bash
   git clone ssh://git@codeberg.org/JurisByte/Generator.git
   ```

3. Navigate to the directory.
   
   ```bash
   cd Generator/
   ```

4. Run the application.
   
   ```bash
   python3 main.py
   ```
