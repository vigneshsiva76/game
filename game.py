"""
Text-Based Number Guessing Game
Level 1: Beginner — Cognifyz Technologies
Objective: Implement a simple game using conditional statements for game logic.
"""

import random


def display_banner():
    print("=" * 50)
    print("   🎮  NUMBER GUESSING GAME  🎮")
    print("   Cognifyz Technologies — Level 1")
    print("=" * 50)


def get_difficulty():
    """Let the player choose a difficulty level."""
    print("\nChoose difficulty:")
    print("  1. Easy   (1–50,  10 attempts)")
    print("  2. Medium (1–100,  7 attempts)")
    print("  3. Hard   (1–200,  5 attempts)")

    while True:
        choice = input("\nEnter 1, 2 or 3: ").strip()
        if choice == "1":
            return 1, 50, 10
        elif choice == "2":
            return 2, 100, 7
        elif choice == "3":
            return 3, 200, 5
        else:
            print("❌  Invalid choice. Please enter 1, 2 or 3.")


def get_valid_guess(upper_bound):
    """Read and validate a numeric guess from the player."""
    while True:
        raw = input("Your guess: ").strip()
        if not raw.isdigit():
            print("❌  Please enter a whole number.")
            continue
        guess = int(raw)
        if guess < 1 or guess > upper_bound:
            print(f"❌  Guess must be between 1 and {upper_bound}.")
            continue
        return guess


def play_round(upper_bound, max_attempts):
    """Core game loop — returns True if the player wins."""
    secret = random.randint(1, upper_bound)
    attempts_used = 0

    print(f"\n🔢  I've picked a number between 1 and {upper_bound}.")
    print(f"    You have {max_attempts} attempts. Good luck!\n")

    while attempts_used < max_attempts:
        remaining = max_attempts - attempts_used
        print(f"  Attempts remaining: {remaining}")

        guess = get_valid_guess(upper_bound)
        attempts_used += 1

        # ── Conditional statements that manage game flow ──
        if guess < secret:
            print("  📈  Too low! Try higher.\n")
        elif guess > secret:
            print("  📉  Too high! Try lower.\n")
        else:
            print(f"\n🎉  Correct! The number was {secret}.")
            print(f"    You got it in {attempts_used} attempt(s)!")
            return True, attempts_used

    # Player ran out of attempts
    print(f"\n😞  Out of attempts! The number was {secret}.")
    return False, attempts_used


def calculate_score(difficulty_level, attempts_used, max_attempts, won):
    """Simple scoring formula."""
    if not won:
        return 0
    base_scores = {1: 100, 2: 200, 3: 300}
    base = base_scores[difficulty_level]
    bonus = (max_attempts - attempts_used) * 10
    return base + bonus


def play_quiz():
    """Bonus: a small general-knowledge quiz game."""
    questions = [
        {
            "question": "What is the capital of France?",
            "options": ["A) London", "B) Paris", "C) Berlin", "D) Madrid"],
            "answer": "B",
        },
        {
            "question": "Which planet is known as the Red Planet?",
            "options": ["A) Venus", "B) Jupiter", "C) Mars", "D) Saturn"],
            "answer": "C",
        },
        {
            "question": "What is 12 × 12?",
            "options": ["A) 124", "B) 144", "C) 132", "D) 148"],
            "answer": "B",
        },
        {
            "question": "Who wrote 'Romeo and Juliet'?",
            "options": [
                "A) Charles Dickens",
                "B) Mark Twain",
                "C) William Shakespeare",
                "D) Jane Austen",
            ],
            "answer": "C",
        },
        {
            "question": "What is the chemical symbol for water?",
            "options": ["A) O2", "B) CO2", "C) H2O", "D) NaCl"],
            "answer": "C",
        },
    ]

    print("\n" + "=" * 50)
    print("   📚  BONUS QUIZ GAME  📚")
    print("=" * 50)
    print("Answer each question by typing A, B, C or D.\n")

    score = 0
    for i, q in enumerate(questions, 1):
        print(f"Q{i}: {q['question']}")
        for opt in q["options"]:
            print(f"     {opt}")

        while True:
            ans = input("  Your answer: ").strip().upper()
            if ans in ("A", "B", "C", "D"):
                break
            print("  ❌  Please enter A, B, C or D.")

        # Conditional to check answer
        if ans == q["answer"]:
            print("  ✅  Correct!\n")
            score += 1
        else:
            print(f"  ❌  Wrong! The answer was {q['answer']}.\n")

    print(f"Quiz finished! You scored {score}/{len(questions)}.")
    if score == len(questions):
        print("🏆  Perfect score!")
    elif score >= 3:
        print("👍  Great job!")
    else:
        print("📖  Keep practising!")
    return score


def main():
    display_banner()
    total_score = 0

    while True:
        print("\nMain Menu")
        print("  1. Number Guessing Game")
        print("  2. General Knowledge Quiz")
        print("  3. Quit")

        menu_choice = input("\nChoose an option (1/2/3): ").strip()

        if menu_choice == "1":
            difficulty_level, upper_bound, max_attempts = get_difficulty()
            won, attempts_used = play_round(upper_bound, max_attempts)
            round_score = calculate_score(
                difficulty_level, attempts_used, max_attempts, won
            )
            total_score += round_score
            if won:
                print(f"    Round score: {round_score}  |  Total score: {total_score}")

        elif menu_choice == "2":
            quiz_score = play_quiz()
            total_score += quiz_score * 20
            print(f"    Total score so far: {total_score}")

        elif menu_choice == "3":
            print(f"\n👋  Thanks for playing! Final score: {total_score}")
            print("    See you next time!\n")
            break

        else:
            print("❌  Invalid choice. Enter 1, 2 or 3.")

        again = input("\nReturn to main menu? (y/n): ").strip().lower()
        if again != "y":
            print(f"\n👋  Thanks for playing! Final score: {total_score}\n")
            break


if __name__ == "__main__":
    main()
