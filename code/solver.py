from queue import PriorityQueue
from collections import OrderedDict
from map import Map
from node import Node

class DijkstraSolver:
    """
    Dijkstra's algorithm for finding the shortest path between two nodes in a graph.
    """

    def __init__(self, start : Node, goal : Node, map : Map):
        """
        Initialize the solver with the start and goal nodes, and the map.

        Parameters
        ----------
        start : Node
            The start node.
        goal : Node
            The goal node.
        map : Map
            The map.
        """
        self.start = start
        self.goal = goal
        self.map = map

        self.open = PriorityQueue()
        self.closed = OrderedDict()

    def _check_goal(self, node : Node) -> bool:
        """
        Check if the node is the goal node.

        Parameters
        ----------
        node : Node
            The node to check.

        Returns
        -------
        bool
            True if the node is the goal node, False otherwise.
        """
        return node == self.goal
    
    def _generate_path(self, node : Node) -> list:
        """
        Generate the path from the start node to the goal node.

        Parameters
        ----------
        node : Node
            The goal node.

        Returns
        -------
        list
            The path from the start node to the goal node.
        """
        path = []
        while node:
            path.append(node)
            node = node.parent
        return path[::-1]
    
    def solve(self) -> list:
        """
        Solve the problem.

        Returns
        -------
        list
            The path from the start node to the goal node.
        """
        self.open.put(self.start)

        while not self.open.empty():
            node = self.open.get()
            
            if self._check_goal(node):
                path = self._generate_path(node)
                return path

            self.closed[hash(node)] = node

            for child in node.get_children():
                hash_val = hash(child)
                if self.map.is_valid(child):
                    if hash_val not in self.closed:
                        self.closed[hash_val] = child
                        self.open.put(child)
                    else:
                        sn = self.closed[hash_val]
                        cost = node.cost_to_come + child.cost_to_come
                        if cost < sn.cost_to_come:
                            sn.parent = node
                            sn.cost_to_come = cost

        return None

    def get_explored_nodes(self) -> list:
        """
        Get the explored nodes.

        Returns
        -------
        list
            The explored nodes.
        """
        return list(self.closed.values())
    
    def print_path(self, path : list) -> None:
        """
        Print the path from the start node to the goal node.

        Parameters
        ----------
        path : list
            The path from the start node to the goal node.
        """
        
        for node in path:
            print(node.state)