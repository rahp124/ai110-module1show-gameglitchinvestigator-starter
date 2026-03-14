# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable.

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: _"How do I keep a variable from resetting in Streamlit when I click a button?"_
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

This app is a Streamlit number guessing game where the player chooses a difficulty level, gets a hidden number within that level’s range, and tries to guess it in limited attempts while receiving hints.
The hint logic was reversed in behavior expectations. The New Game button regenerated the secret ignoring the selected difficulty range.
Verified and enforced correct hint behavior in tests:
Guess > secret -> Too high, message includes LOWER.
Guess < secret -> Too low, message includes HIGHER.
Updated New Game state reset logic to generate secrets using difficulty bounds.
Added focused pytest coverage.

## 📸 Demo

![Screenshot of the game](images/screenshot1.png)

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, insert a screenshot of your Enhanced Game UI here]
