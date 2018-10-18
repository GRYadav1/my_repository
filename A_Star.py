'''
Created on Sep 23, 2018

@author: gaurav
'''
import random
import math
import heapq
import queue as Q
import copy
import itertools
from copy import deepcopy


# method to print the path to reach a given node
def printPath(childObj):
    path = []
    cost = childObj.g
    while(childObj != None):
        path.append(childObj.inputA)
        childObj = childObj.Parent
    print("INITIAL STATE \n |")
    for x in reversed(path):
        print(x)
    print("Total Cost = " + str(cost))

# class to define a node and its characteristics (state, heuristic, actual cost, parent)


class PuzzleNode:

    def _init_(self):
        self.h = 0
        self.g = 0
        self.f = 0

        self.Parent = None
        self.inputA = []

    def printA(self, arr):
        print(arr)

    def eqate(self, arr):
        self.inputA = arr

# Method to take initial state, goal state and heuristic type as input


def takeInput():
    inputA = []
    goalState = []
    inputString = input("Enter Array :");
    k = 0
    for i in range(0, 3):
        row = []
        for j in range(0, 3):
            row.append(int(inputString[k]))
            k = k + 1
        inputA.append(row)

    inputString = []
    inputString = input("Enter Goal State :")
    k = 0
    for i in range(0, 3):
        row = []
        for j in range(0, 3):
            row.append(int(inputString[k]))
            k = k + 1
        goalState.append(row)

    heuristic_type = int(input("Enter 1 for Manhattan Heuristic or 2 for Misplaced Tile Heuristic"))

    return inputA, goalState, heuristic_type

# method to return the coordinates/indices of a given number


def find(inputA, key):
    if key < 0 or key > 8:
        raise Exception("Out of Range")

    for r in range(3):
        for c in range(3):
            if inputA[r][c] == key:
                return r, c

# method to generate all possible moves from the current state


def getPossibleMovies(inpArray):
    row, col = find(inpArray, 0)
    moves = []
    if(row > 0):
        r = row - 1
        moves.append((r, col))
    if(col > 0):
        c = col - 1
        moves.append((row, c))
    if(row < 2):
        r = row + 1
        moves.append((r, col))
    if(col < 2):
        c = col + 1
        moves.append((row, c))

    return moves

# method to calculate the manhattan distance heuristic


def manhatten_heu(initalStage, GoalStage):
    indexInitial = []
    indexGoal = []
    for i in range(9):
        indexInitial.append((find(initalStage, i)))

    for i in range(9):
        indexGoal.append((find(GoalStage, i)))

    h = 0
    for j in range(1, 9):
        rx, cx = indexInitial[j]
        ry, cy = indexGoal[j]
        h = h + (abs(rx - ry) + abs(cx - cy))
    return h

# method to calculate the misplaced tile heuristic


def misplacedTile_heu(initialStage, GoalStage):
    h = 0
    for x in range(len(initialStage)):
        for y in range(len(initialStage[x])):
            if initialStage[x][y] != GoalStage[x][y]:
                h += 1
    return h

# method to generate a child node


def makeMove(input1, target):
    inputA = copy.deepcopy(input1)
    r0, c0 = find(inputA, 0)
    rt, ct = target

    inputA[r0][c0], inputA[rt][ct] = inputA[rt][ct], inputA[r0][c0]
    return inputA

# method to check if the node has already been explored or is in the fringe; returns -1 if the node is not a duplicate


def _is_visited(node, fringe):
    tempVis = copy.deepcopy(fringe)
    i = 0
    while(len(tempVis) > 0):
        if(tempVis[0].inputA == node.inputA):
            return i
        del(tempVis[0])
        i = i + 1

    return -1

# method to check if the duplicate node has less cost, if yes then add it again to the fringe


def check_f_and_swap(fringe, node, index):
    if(fringe[index].f > node.f):
        fringe[index] = node
        return 0
    return -1

# method which starts the A* Algorithm


def A_Star(initialStage, goal, heuristic_type):
    count = 0
    count_expanded = 0
    count_generated = 0
    visited = []
    current = []
    # heuristic calculation for the initial state
    initialStage.h = manhatten_heu(initialStage.inputA, goal) if heuristic_type == 1 else misplacedTile_heu(initialStage.inputA, goal)
    initialStage.g = count
    initialStage.f = initialStage.g + initialStage.h
    initialStage.Parent = None
    if (initialStage.inputA == goal):
        print("Bingo")
        print("Nodes Expanded", count_expanded)
        print("Nodes Generated", count_generated)
        return

    current.append(initialStage)

    moves = []
    # i=0

    while(len(current) > 0):
        currentElement = current.pop(0)
        visited.append(currentElement)  # adding the current node to visited/explored nodes
        count = count + 1
        moves = getPossibleMovies(currentElement.inputA)  # method call to generate all the possible moves from the current state
        count_expanded = count_expanded + 1
        # loop to generate all the children nodes from the current node
        for i in moves:
            childObj = PuzzleNode()
            childObj.g = currentElement.g + 1  # adding the actual cost to the child
            childObj.inputA = makeMove(currentElement.inputA, i)  # generate the child from the current node
            childObj.h = manhatten_heu(childObj.inputA, goal) if heuristic_type == 1 else misplacedTile_heu(childObj.inputA, goal)
            childObj.f = childObj.g + childObj.h  # calculation of the heuristic (actual cost + chosen heuristic)
            childObj.Parent = currentElement
            count_generated = count_generated + 1
            # condition to check if the goal state is reached
            if (childObj.inputA == goal):
                print("Bingo...................!!!!!!!")
                print("\nExpanded Nodes/Solution Path--\n")
                printPath(childObj)  # print the entire path to the goal state
                print("Nodes Expanded", count_expanded)
                print("Nodes Generated", count_generated)
                del(current)
                return

            # checking if the child is already present in the visited nodes list
            if_visited_index = _is_visited(childObj, visited)
            if(if_visited_index != -1):
                check_f_and_swap(visited, childObj, if_visited_index)
            else:
                # checking if the child is already present in the fringe
                if_current_index = _is_visited(childObj, current)
                if(if_current_index != -1):
                    check_f_and_swap(current, childObj, if_current_index)

                else:
                    current.append(childObj)

            # sort the fringe in the increasing order of their calculated heuristics
            current = sorted(current, key=lambda p: p.f)


# main method
def main():
    inputA, goal, heuristic_type = takeInput()  # method call to take all the required inputs
    p = PuzzleNode()  # method call to create the initial node
    p.eqate(inputA)
    p.printA(p.inputA)
    A_Star(p, goal, heuristic_type)


main()
