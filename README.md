### ✊📝✂️ **Rock, Paper, Scissors Game in Python**  

**Skills:** Python, Game Logic, User Interaction  

---

#### 🚀 **Project Overview**  
This project is a **Python implementation of the classic Rock, Paper, Scissors game**, where a user plays against the computer. It showcases **Python fundamentals, control flow, randomization, and user input handling**—essential skills for **software development roles**.  

This project demonstrates:  
✅ **Conditional Logic** – Decision-making using `if-else` statements  
✅ **Randomization** – Computer selects a random move  
✅ **User Interaction** – Handling input validation and result display  
✅ **Loop Control** – Implementing a replay system  

---

#### 🎯 **How the Game Works**  
1️⃣ The player selects **Rock (r), Paper (p), or Scissors (s)**.  
2️⃣ The computer randomly selects one of the three choices.  
3️⃣ The program compares both choices and determines the winner:  
   - **Rock beats Scissors**  
   - **Scissors beat Paper**  
   - **Paper beats Rock**  
4️⃣ The game announces the result: **Win, Loss, or Tie**.  
5️⃣ The user can choose to play again or exit.  

---

#### 🏗 **Project Structure**  
📂 **main.py** – Contains the entire game logic, including:  
- **User input handling**  
- **Computer’s random selection**  
- **Game logic to determine the winner**  
- **Replay functionality**  

✅ **Example: Getting User Input & Validating Choices**  
```python
def play():
    while True:
        user = input("Enter Rock (r), Paper (p), or Scissors (s): ").lower()
        if user in ['r', 'p', 's']:
            break
        print("Invalid choice. Please select r, p, or s.")
```

---

#### 🤖 **Game Logic & Winner Calculation**  
The game logic follows standard **Rock-Paper-Scissors rules**, implemented using **conditional statements**.  

✅ **Example: Determining the Winner**  
```python
def determine_winner(user, computer):
    win_conditions = {'r': 's', 's': 'p', 'p': 'r'}

    if user == computer:
        return "It's a tie!"
    elif win_conditions[user] == computer:
        return "You win! 🎉"
    else:
        return "Computer wins! 🤖"
```
💡 **How it works:**  
- If both choices are the same → **Tie**  
- If the user's choice beats the computer’s choice → **User wins**  
- Otherwise, **Computer wins**  

---

#### 🎮 **Gameplay Example**  
```python
def play_game():
    user = input("Choose Rock (r), Paper (p), or Scissors (s): ").lower()
    computer = random.choice(['r', 'p', 's'])
    
    print(f"Computer chose: {computer.upper()}")
    result = determine_winner(user, computer)
    print(result)
```
💡 **Enhancements:**  
✔ **Computer’s choice is randomized**  
✔ **Results are printed dynamically based on input**  

---

#### 📊 **Game Features & Enhancements**  
✔ **User input validation** – Ensures correct selection  
✔ **Random computer selection** – Makes gameplay fair  
✔ **Replay option** – Allows the user to play multiple rounds  

✅ **Example: Adding Replay Functionality**  
```python
def play_again():
    while True:
        again = input("Play again? (y/n): ").lower()
        if again == 'y':
            play_game()
        elif again == 'n':
            print("Thanks for playing! 🎮")
            break
```
💡 **Why this is useful?** – The game continues until the user decides to quit.

---

#### 🔮 **Future Enhancements**  
🔹 **Score Tracking System** – Track wins, losses, and ties over multiple rounds  
🔹 **Multiplayer Mode** – Let two users play against each other  
🔹 **Graphical User Interface (GUI)** – Using `tkinter` or `Pygame`  
🔹 **Voice Command Integration** – Allow users to speak their choices  

---

#### 🛠 **How to Run This Project**  
1️⃣ Clone the repo:  
   ```bash
   git clone https://github.com/shrunalisalian/rock-paper-scissors.git
   ```
2️⃣ Install dependencies (if required):  
   ```bash
   pip install -r requirements.txt
   ```
3️⃣ Run the game:  
   ```bash
   python main.py
   ```

---

#### 📌 **Connect with Me**  
- **LinkedIn:** [Shrunali Salian](https://www.linkedin.com/in/shrunali-salian/)  
- **Portfolio:** [Your Portfolio Link](#)  
- **Email:** [Your Email](#)  

---
Reference: https://youtu.be/xRlN8CFJwAM?si=B1sEHl5gwQKLB71H
