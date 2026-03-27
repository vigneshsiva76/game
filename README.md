# 🎮 Text-Based Game — Level 1: Beginner
**Cognifyz Technologies Internship Task 1**

---

## 📋 Task Overview

| Field | Detail |
|-------|--------|
| Level | 1 – Beginner |
| Task | Develop a basic text-based game |
| Objective | Implement a simple game using conditional statements for game logic |

---

## 🗂 Project Structure

```
text_game/
├── index.html   ← Browser-playable version (open in any browser)
├── style.css    ← Retro-arcade styling (dark neon aesthetic)
├── game.py      ← Full Python terminal game
└── README.md    ← This file
```

---

## ✅ Steps Completed

### Step 1 — Choose a game type
Two modes were implemented:
- **Number Guessing Game** — guess a secret number with higher/lower hints
- **General Knowledge Quiz** — five multiple-choice questions (A/B/C/D)

### Step 2 — Define the game rules and logic
- **Guessing game** has three difficulty levels (Easy / Medium / Hard), each with its own number range and attempt limit.  
  Scoring formula: `base_score + (attempts_remaining × 10)`
- **Quiz** awards 1 point per correct answer out of 5.

### Step 3 — Use conditional statements to manage game flow
Every branch in both games is controlled exclusively by `if / elif / else`:
- Menu option routing
- Difficulty selection
- Guess comparison (`too low` / `too high` / `correct`)
- Attempt exhaustion check
- Quiz answer validation
- Replay / quit prompt

### Step 4 — Test and debug for correctness
- **Non-numeric input** is caught and the user is re-prompted.
- **Out-of-range guesses** are rejected with a clear message.
- **Empty input** is ignored safely.
- **Boundary values** (1 and upper_bound) are accepted and handled correctly.

---

## 🐍 Running the Python Game

**Requirements:** Python 3.7 or newer (no third-party packages needed)

```bash
python game.py
```

You will see:
```
==================================================
   🎮  NUMBER GUESSING GAME  🎮
   Cognifyz Technologies — Level 1
==================================================

Main Menu
  1. Number Guessing Game
  2. General Knowledge Quiz
  3. Quit
```

---

## 🌐 Running the Browser Game

Simply open `index.html` in any modern browser — no server required.

```bash
# macOS
open index.html

# Linux
xdg-open index.html

# Windows
start index.html
```

The browser version replicates the Python guessing game logic in JavaScript, styled with a retro-arcade terminal aesthetic.

---

## 🎯 Difficulty Levels (Guessing Game)

| Level | Range | Attempts | Base Score |
|-------|-------|----------|------------|
| Easy | 1 – 50 | 10 | 100 |
| Medium | 1 – 100 | 7 | 200 |
| Hard | 1 – 200 | 5 | 300 |

**Final score** = base score + (remaining attempts × 10)

---

## 🧠 Key Concepts Demonstrated

- `random.randint()` for secret number generation
- `if / elif / else` chains for all game-flow decisions
- Input validation with `while True` loops
- Functions for separation of concerns (`play_round`, `play_quiz`, `get_difficulty`, etc.)
- Return values to pass game results back to the main loop

---

## 👩‍💻 Author

Submitted as part of **Cognifyz Technologies Python Internship**  
Task: Level 1 · Beginner · Task 1 — Text-Based Game
