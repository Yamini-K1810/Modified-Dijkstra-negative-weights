# Modified Dijkstra's Algorithm for Negative Weights

This project implements a modified version of Dijkstra's algorithm to handle graphs with negative weights. The approach avoids using Bellman-Ford and stays true to the Dijkstra's methodology by introducing a transformation to shift all weights into the non-negative range.

## Features
- Handles graphs with negative weights by adding a minimum weight offset.
- Calculates the shortest path between nodes in a graph.
- Uses a priority queue (via `heapq`) for efficient performance.

## Problem Statement
This project was undertaken as a college assignment to implement Dijkstra's algorithm for negative weights without diverging to Bellman-Ford or other shortest path algorithms.

## How It Works
1. All edge weights are adjusted by adding the absolute value of the smallest negative weight in the graph.
2. The adjusted graph is processed using Dijkstra's algorithm.
3. The final results are interpreted to ensure correctness for the original graph.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/modified-dijkstra-negative-weights.git
