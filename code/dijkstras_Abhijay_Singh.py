import time
import numpy as np
from map import Map
from node import Node
from solver import DijkstraSolver
from visualizer import Visualizer

def main():
    map = Map(width=600, height=250, clearance=5)

    while True:
        x, y = input("\nEnter start state (x, y) : ").split()
        start = Node((int(x), int(y)), 0, None)

        x, y = input("Enter end state (x, y) : ").split()
        end = Node((int(x), int(y)), np.inf, None)

        if map.is_valid(start) and map.is_valid(end):
            print("\nStarting search...")
            break

        print("\nInvalid start or end state. Try again.")


if __name__ == "__main__":
    main()