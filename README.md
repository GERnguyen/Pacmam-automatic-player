# Pac-Man AI Search Algorithms

A Python implementation of the classic Pac-Man game featuring various AI search algorithms to guide Pac-Man through different levels of complexity.

## Overview

This project demonstrates different pathfinding and decision-making algorithms through a Pac-Man game environment. The game includes four difficulty levels, each designed to showcase different types of AI algorithms.

## Features

- **Four Game Levels** with increasing difficulty
- **Multiple AI Algorithms** including:
  - Uninformed search (BFS, DFS, IDS)
  - Informed search (Greedy, A*, UCS, IDA*)
  - Local search (Hill Climbing, Simulated Annealing, Beam Search)
  - Adversarial search (Minimax, Alpha-Beta Pruning, Expectimax)
- **Visual Path Display** showing Pac-Man's planned route
- **Interactive Menu** for level and algorithm selection

## Requirements

- Python 3.x
- Pygame

## Installation

```bash
pip install pygame
```

## How to Run

```bash
cd Source
python main.py
```

## Game Levels

**Level 1 & 2**: Basic pathfinding where Pac-Man collects food pellets using uninformed and informed search algorithms.

**Level 3**: Local search challenge with visibility mechanics where Pac-Man explores the map strategically.

**Level 4**: Adversarial environment where ghosts actively chase Pac-Man using A* pathfinding.

## Controls

The game runs automatically once you select a level and algorithm. Use the menu to:
- Choose your preferred level
- Select different AI algorithms
- Navigate between maps

## Project Structure

- `Source/Algorithms/` - Implementation of all search algorithms
- `Source/Object/` - Game objects (Player, Ghost, Food, Wall)
- `Source/Utils/` - Helper functions and utilities
- `Input/` - Map files for different levels

## Algorithm Categories

**Uninformed Search**: BFS, DFS, IDS  
**Informed Search**: Greedy, A*, UCS, IDA*  
**Local Search**: Hill Climbing, Simulated Annealing, Beam Search  
**Game Theory**: Minimax, Alpha-Beta Pruning, Expectimax

Each algorithm has different performance characteristics in terms of optimality, completeness, and efficiency.
