# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

Hint messages are reversed. Difficulty range does not match the instructions. New Game resets attempts incorrectly

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
  Copilot
  Inline Chat forexplanations
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
  When refactoring the check_guess function into logic_utils.py, Copilot correctly moved the function and updated the import in app.py. It also suggested fixing the reversed hint bug.
  I asked it to write a pytest test targeting this behavior and ran it. The test passed, confirming that the hints were now correct. I also ran the app in Streamlit and verified the live game.
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
  I asked Copilot to refactor get_range_for_difficulty. It initially suggested changing all difficulty ranges to 1-100. I noticed the discrepancy when comparing the AI suggestion to the original code and by checking the sidebar difficulty captions.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
  checking both the code logic and the live behavior in the Streamlit app.
- Describe at least one test you ran (manual or using pytest)  
   and what it showed you about your code.
  I ran the copilot pytest test in tests/test_game_logic.py specifically targeting the hint bug. Running this test showed that the hints were now correct for guesses above and below the secret number.
- Did AI help you design or understand any tests? How?
  Copilot suggested the structure of the test functions and gave example assertions for the hint messages. I reviewed the suggestions, ran the tests, and confirmed that the logic behaved as expected.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
    Using inline chat to explain changes the agent made.
- What is one thing you would do differently next time you work with AI on a coding task?
  Taking more intermediatery steps to verify AI code sequentially.
- In one or two sentences, describe how this project changed the way you think about AI generated code.
  I think this project helped me figure out how to split up tasks assigned to the AI. I think
