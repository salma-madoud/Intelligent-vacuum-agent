Intelligent Vacuum Agent: AI Project Canvas

This repository contains a Python implementation of an automated cleaning agent developed to demonstrate core AI principles like perception-action cycles and resource management under uncertainty.

Project Framework: 

Problem Statement: Design an agent capable of maintaining cleanliness in an n-room linear environment while managing a limited energy budget.
Environment Type: Linear and Dynamic. Rooms are arranged in a row. Even after cleaning, there is a 10% probability of a room becoming dirty again at each time step.
Agent Percepts: The agent perceives its current position, the room's dirtiness level (0 to 5), and its remaining energy.
Action Set: Suck (cleans the room), MoveLeft, and MoveRight.
Decision Logic: Rule-based priority. 1. Clean if dirty and energy is sufficient; 2. Move to explore; 3. Stop if all rooms are clean or energy is depleted.

Technical Implementation :

The Bouncing Strategy : The agent uses a deterministic direction-tracking algorithm. It moves in its current direction until it hits a boundary—Room 0 or Room n-1—at which point it reverses direction. This ensures every room is checked periodically to handle the 10% re-dirtying rule.

Energy ManagementInitial Energy: Calculated as 2.5 times the number of rooms.Action Costs: Sucking costs energy equal to the dirt level (1 to 5), while moving costs 2 units.

Safety Checks: Before every action, the agent verifies if it has enough energy to complete the task using specific validation methods.

Quick StartRequirements: 

Python 3.
Run: python main.py
Execution: The script prompts for the number of rooms and maximum steps. It then outputs a full log of every action taken and the final energy efficiency.

Research Team : Al Akhawayn University | CSC 3309: Introduction to AI 

Doha Ilyass / Omar El Mokhtar El Bousouni /  Salma Madoud / Zineb Akhouad 
