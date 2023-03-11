import copy

class Node:
    """
    A node in the search tree.
    """
    
    def __init__(self, state : tuple, cost_to_come : float, parent):
        """
        Parameters
        ----------
        state : tuple
            The state of the node.
        cost_to_come : float
            The cost to come to this node.
        parent : Node
            The parent node.
        """
        
        self.state = state
        self.cost_to_come = cost_to_come
        self.parent = parent

        self.action_set = [
            self._action_move_up,
            self._action_move_down,
            self._action_move_left,
            self._action_move_right,
            self._action_move_up_left,
            self._action_move_up_right,
            self._action_move_down_left,
            self._action_move_down_right
        ]
    
    def __hash__(self) -> int:
        return hash(tuple(self.state))
       
    def __eq__(self, other) -> bool:
        return self.state == other.state
    
    def __lt__(self, other) -> bool:
        return self.cost_to_come < other.cost_to_come

    def _action_move_up(self) -> tuple:
        """
        Move the node up by one unit.

        Returns
        -------
        tuple
            The new state and the cost to move to the new state.
        """
        state = copy.deepcopy(self.state)
        return (state[0], state[1] - 1), 1
    
    def _action_move_down(self) -> tuple:
        """
        Move the node down by one unit.

        Returns
        -------
        tuple
            The new state and the cost to move to the new state.
        """
        state = copy.deepcopy(self.state)
        return (state[0], state[1] + 1), 1
    
    def _action_move_left(self) -> tuple:
        """
        Move the node left by one unit.

        Returns
        -------
        tuple
            The new state and the cost to move to the new state.
        """
        state = copy.deepcopy(self.state)
        return (state[0] - 1, state[1]), 1
    
    def _action_move_right(self) -> tuple:
        """
        Move the node right by one unit.

        Returns
        -------
        tuple
            The new state and the cost to move to the new state.
        """
        state = copy.deepcopy(self.state)
        return (state[0] + 1, state[1]), 1
    
    def _action_move_up_left(self) -> tuple:
        """
        Move the node up and left by one unit.

        Returns
        -------
        tuple
            The new state and the cost to move to the new state.
        """
        state = copy.deepcopy(self.state)
        return (state[0] - 1, state[1] - 1), 1.4
    
    def _action_move_up_right(self) -> tuple:
        """
        Move the node up and right by one unit.

        Returns
        -------
        tuple
            The new state and the cost to move to the new state.
        """
        state = copy.deepcopy(self.state)
        return (state[0] + 1, state[1] - 1), 1.4
    
    def _action_move_down_left(self) -> tuple:
        """
        Move the node down and left by one unit.

        Returns
        -------
        tuple
            The new state and the cost to move to the new state.
        """
        state = copy.deepcopy(self.state)
        return (state[0] - 1, state[1] + 1), 1.4
    
    def _action_move_down_right(self) -> tuple:
        """
        Move the node down and right by one unit.

        Returns
        -------
        tuple
            The new state and the cost to move to the new state.
        """
        state = copy.deepcopy(self.state)
        return (state[0] + 1, state[1] + 1), 1.4
    
    def _get_actions(self) -> list:
        """
        Get the list of actions that can be performed on the node.

        Returns
        -------
        list
            The list of actions that can be performed on the node.
        """
        actions = []
        for action in self.action_set:
            actions.append(action())
        return actions
    
    def get_children(self) -> list:
        """
        Get the list of children nodes.
        
        Returns
        -------
        list
            The list of children nodes.
        """
        children = []
        for action in self._get_actions():
            child = Node(action[0], self.cost_to_come + action[1], self)
            children.append(child)

        return children