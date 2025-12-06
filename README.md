# 🇺🇸 U.S. States Guessing Game

An interactive geography game built with Python to master data handling and GUI interaction.

## 🎮 How it Works
The program loads a map interface where users guess U.S. state names. It validates inputs against a dataset and dynamically places the text on the correct map coordinates.

## ⚙️ Key Features
* **Data Analysis:** Uses `pandas` to read and query CSV data.
* **Interactive GUI:** Built with the `turtle` graphics library for image rendering and text placement.
* **Smart Exit:** When the user types "Exit", the program uses **List Comprehension** to compare the full list vs. guessed list and exports a `states_to_learn.csv` file for study.

## 🛠️ Tech Stack
* Python 3.9+
* Pandas Library
* Turtle Module
