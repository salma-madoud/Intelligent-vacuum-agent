# 🤖 Intelligent Vacuum Cleaning Agent — AI Simulation

> A rule-based intelligent agent that navigates and cleans a linear multi-room environment, built for **CSC3309: Introduction to Artificial Intelligence** at Al Akhawayn University.

**Team:** Doha Ilyass · Omar El Mokhtar El Bousouni · Salma Madoud · Zineb Akhouad  
**Date:** February 11, 2026

---

## 📖 Overview

This project simulates an intelligent vacuum cleaning agent operating in a linear environment of `n` rooms. Each room has a dirtiness level from 0 (clean) to 5 (very dirty), and the agent must navigate and clean all rooms while managing a limited energy budget. The environment is dynamic — clean rooms can randomly become dirty again during the simulation.

---

## ✨ Features

- 🏠 **Dynamic environment** — rooms randomly re-dirty with 10% probability each step
- ⚡ **Energy-constrained agent** — energy budget scales with room count (`2.5 × n_rooms`)
- 🧠 **Rule-based decision making** — 4 prioritized action rules
- 📊 **Action logging** — full trace of every action, room, and energy cost
- 🔁 **Bouncing strategy** — agent sweeps left and right to cover all rooms

---

## 🗂️ Project Structure

```
vacuum-agent/
│
├── main.py       # Full simulation source
└── README.md
```

### Class Architecture

| Class | Responsibility |
|---|---|
| `Room` | Stores and manages dirtiness level of a single room |
| `Environment` | Holds all rooms, handles cleaning, state queries, and dynamic re-dirtying |
| `Agent` | Perceives environment, decides actions, tracks energy and logs |
| `simulate()` | Runs the full game loop for a given number of rooms and max steps |

---

## 🚀 Getting Started

### Prerequisites

- Python **3.7+**
- No external libraries needed — uses only the standard library

### Installation & Run

```bash
# 1. Clone the repository
git clone https://github.com/YOUR_USERNAME/vacuum-agent.git
cd vacuum-agent

# 2. Run the simulation
python main.py
```

---

## 🎮 How to Use

When you run the program, you'll be prompted for two inputs:

```
Enter number of rooms: 5
Enter maximum steps: 50
```

The simulation then runs and prints a full report:

```
=== SIMULATION RESULTS ===
Steps taken: 23
Rooms cleaned: 7
Energy consumed: 17.5
Energy remaining: 5.0

Final room states: [0, 0, 2, 0, 0]

Action sequence:
  1. Suck at room 0 (cost: 3)
  2. MoveRight at room 0 (cost: 2)
  3. Suck at room 1 (cost: 4)
  ...
```

---

## 🧠 Agent Design

### Perception
At each step the agent observes:
- Its current position
- Whether the current room is clean or dirty
- The dirtiness level of the current room
- Its remaining energy

### Action Set

| Action | Energy Cost | Description |
|---|---|---|
| `Suck` | = dirt level (1–5) | Cleans the current room |
| `MoveRight` | 2 | Moves to the next room |
| `MoveLeft` | 2 | Moves to the previous room |
| `Stop` | 0 | Ends the simulation |

### Decision Rules (in priority order)

1. **Dirty room + enough energy** → `Suck`
2. **All rooms clean** → `Stop`
3. **Can move** → continue in current direction; reverse at the walls
4. **Out of energy** → `Stop`

---

## ⚙️ Environment Rules

- Rooms are initialized with a random dirtiness level between **0 and 5**
- After every step, each clean room has a **10% chance** of becoming dirty again (level 1–5)
- The agent starts at **room 0** facing right

### Energy Budget

The agent's starting energy is `2.5 × n_rooms`. For example:
- 4 rooms → 10 energy units
- 10 rooms → 25 energy units

---

## 🏁 Simulation Stop Conditions

The simulation ends when any of these is true:
1. All rooms are clean
2. The agent runs out of energy (can't move or suck)
3. The maximum number of steps is reached

---

## 📌 Known Limitations & Future Improvements

- The agent may waste energy traversing already-clean rooms — it has no path planning
- A smarter agent could prioritize the nearest dirty room to minimize travel cost
- Future versions could implement a search-based planner (e.g. BFS/A*) for optimal routing

---

## 📄 License

This project was developed as an academic assignment. Feel free to reference or build upon it with attribution.
