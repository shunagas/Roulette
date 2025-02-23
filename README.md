# Roulette
Simulate the balance between your funds and bets for a winning strategy

# Martingale Simulation

This project is a Python implementation of the **Martingale Betting System**, a strategy commonly used in casino games like roulette. The program simulates a series of bets using the Martingale system and tracks the player's balance over multiple rounds.

## 🚀 Features
- Simulates betting rounds using the Martingale strategy
- Tracks the player's balance and adjusts bet sizes dynamically
- Displays each round's balance and bet amount
- Stops if funds are insufficient to continue betting

## 📜 How It Works
1. The player starts with an **initial balance** and an **initial bet amount**.
2. The player bets on a **50/50 outcome** (e.g., red/black in roulette).
3. If the player **wins**, they keep their winnings and reset the bet to the initial amount.
4. If the player **loses**, they **double the bet** and continue betting.
5. The cycle repeats for a specified number of rounds or until the player runs out of money.

## 🛠 Installation & Usage
### Prerequisites
- Python 3.x installed

### Run the simulation
```bash
python montecarlo.py
```

## 📌 Example Output
```
資金: $950, 賭金: $100
資金: $850, 賭金: $200
資金: $650, 賭金: $400
資金: $1250, 賭金: $50
...
最終残高: $X
```

## ⚠️ Disclaimer
This simulation is for educational purposes only. The Martingale system does not guarantee winnings and may lead to significant financial losses.

## 📄 License
This project is licensed under the MIT License.

