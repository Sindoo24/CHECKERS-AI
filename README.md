# CHECKERS-AI




An AI-powered Checkers game implementing the Minimax algorithm for strategic decision-making, built with Python and Pygame.

## Overview

This project is a fully functional implementation of the classic board game **Checkers**, developed using **Python** and **Pygame**, where a human player competes against an intelligent AI on an 8x8 grid. At the core of the project lies the **Minimax Algorithm**, a recursive decision-making strategy widely used in Game Theory. By constructing a game tree to simulate potential future board states, the AI evaluates moves to maximize its own advantage while assuming the opponent plays optimally to minimize it. Beyond gameplay, the application demonstrates key technical concepts such as efficient game loop management, deep recursion for tree traversal, and heuristic evaluation of complex board configurations.





<img width="796" height="831" alt="Screenshot 2025-11-29 130330" src="https://github.com/user-attachments/assets/fec8dce7-6957-4a9a-818e-4121d59d470c" />






## Features

* **Strategic AI:** Challenge a computer opponent that utilizes the **Minimax algorithm** to predict future board states and make optimal moves.
* **Advanced Game Logic:** Fully implements complex Checkers mechanics, including **King promotion**, recursive **double jumps**, and multi-capture chains.
* **Interactive Interface:** A clean, responsive GUI built with **Pygame** that provides real-time visual feedback (blue dots) for valid moves.
* **Smart State Detection:** Automatically tracks the game flow to detect victories or declare **ties** based on the standard 50-move rule.



## Requirements

* **Python 3.x**
* **Pygame** library for rendering graphics and handling user input.

## How to Play

### 1. Install the Requirements

First, ensure you have Python installed. You can install the necessary dependencies using pip:

```bash
pip install pygame
