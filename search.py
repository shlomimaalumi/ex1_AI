"""
In search.py, you will implement generic search algorithms
"""

import util
from util import Stack
from util import Queue
from util import PriorityQueueWithFunction
from util import PriorityQueueWithFunction


class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def get_start_state(self):
        """
        Returns the start state for the search problem
        """
        util.raiseNotDefined()

    def is_goal_state(self, state):
        """
        state: Search state

        Returns True if and only if the state is a valid goal state
        """
        util.raiseNotDefined()

    def get_successors(self, state):
        """
        state: Search state

        For a given state, this should return a list of triples,
        (successor, action, stepCost), where 'successor' is a
        successor to the current state, 'action' is the action
        required to get there, and 'stepCost' is the incremental
        cost of expanding to that successor
        """
        util.raiseNotDefined()

    def get_cost_of_actions(self, actions):
        """
        actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.  The sequence must
        be composed of legal moves
        """
        util.raiseNotDefined()


def generic_search(problem, generic):
    """
    Search the node by the generic data structure type (e.g. stack, queue, fringe etc.)
    """
    visited = set()
    start_state = problem.get_start_state()

    generic.push((start_state, []))

    while generic:
        current_state, actions = generic.pop()

        if problem.is_goal_state(current_state):
            return actions

        if current_state not in visited:
            visited.add(current_state)

            for successor, action, step_cost in problem.get_successors(current_state):
                if successor not in visited:
                    new_actions = actions + [action]
                    generic.push((successor, new_actions))


def depth_first_search(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches
    the goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    stack = Stack()
    return generic_search(problem, stack)


def breadth_first_search(problem):
    """
    Search the shallowest nodes in the search tree first.
    """
    queue = Queue()
    return generic_search(problem, queue)


def uniform_cost_search(problem):
    """
    Search the node of-least total cost first.
    """
    fringe = PriorityQueueWithFunction(_)
    return search_template(problem, fringe)


def null_heuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def a_star_search(problem, heuristic=null_heuristic):
    """
    Search the node that has the lowest combined cost and heuristic first.
    """
    "*** YOUR CODE HERE ***"
    fringe = PriorityQueueWithFunction(_)
    return search_template(problem, fringe)


# Abbreviations
bfs = breadth_first_search
dfs = depth_first_search
astar = a_star_search
ucs = uniform_cost_search
