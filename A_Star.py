'''
Created on Sep 23, 2018

@author: gaura
'''
import random
import math
import heapq
import queue as Q
import copy   
import itertools
from copy import deepcopy

goal = [[1,2,3],[8,6,4],[7,5,0]] 

def printArr(list1):
    
    for i in list1:
        print(i.inputA, "=>",i.f)
        print("\t\t|")
        
class PuzzleNode:
    
    def _init_(self):
        self.h = 0
        self.g = 0
        self.f = 0
        self.inputA =[]
        
    def printA(self,arr): 
        print(arr)  
         
    def eqate(self,arr):
        self.inputA = arr          
        


def takeInput():
    
    inputA=[]
    inputString = input("Enter Array :");
    k=0
    for i in range(0,3):
        row =[]
        for j in range(0,3):
            row.append(int(inputString[k]))
            k=k+1
        inputA.append(row)
        
    return inputA
def find(inputA, key):

        if key < 0 or key > 8:
            raise Exception("Out of Range")

        for r in range(3):
            for c in range(3):
                if inputA[r][c] == key:
                    return r, c

def getPossibleMovies(inpArray):
    
    row, col = find(inpArray,0)
    moves = []
    if(row > 0 ):            
          r = row - 1
          moves.append((r,col))
        
    if(col > 0):
          c = col - 1
          moves.append((row,c))  
    if(row < 2):
          r= row + 1
          moves.append((r,col))
    if(col < 2):
          c = col + 1
          moves.append((row,c))
                       
    return moves
                
def Cloning(li1): 
    A = []
    for i in li1:
         A.append(i)
    return  A
                
def manhatten_heu(initalStage, GoalStage):   
    
    indexInitial = []
    indexGoal = []
    for i in range(9):
        indexInitial.append((find(initalStage,i)))
        
    for i in range(9):
        indexGoal.append((find(GoalStage,i)))
          
    h=0     
    for j in range(1,9):
               rx,cx = indexInitial[j]
               ry,cy = indexGoal[j]
               h = h + (abs(rx-ry)+abs(cx-cy))
               
    return h;

          
def makeMove(input1,target): 

    inputA = copy.deepcopy(input1)
    '''inputA=[]
    for i in input1:
          inputA.append(i)'''
    r0,c0=find(inputA,0)
    rt,ct = target
    
    inputA[r0][c0],inputA[rt][ct] = inputA[rt][ct],inputA[r0][c0];
    print(inputA)
    return inputA

def _is_visited(node,fringe,visited_or_current):
    
    tempVis = copy.deepcopy(fringe)
    i = 0
    while(len( tempVis)>0):
         if(tempVis[0].inputA == node.inputA):
             return i
         del(tempVis[0])
         i=i+1
         
    return -1   

def check_f_and_swap(fringe,node,index):
              
        if(fringe[index].f > node.f):
            fringe[index] = node
            return 0
        return -1
    
def A_Star(initialStage):
    count = 0
    visited = []
    current = []

    initialStage.h = manhatten_heu(initialStage.inputA, goal)  
    initialStage.g = count
    initialStage.f = initialStage.g + initialStage.h
    current.append(initialStage)
        
    moves = []
    #i=0
    
    
    while(len(current) >0 ):
          print(count)
          currentElement = current.pop(0)
          visited.append(currentElement)
          count=count+1
          moves =getPossibleMovies(currentElement.inputA)

          for i in moves:
            childObj = PuzzleNode()  
            childObj.g = currentElement.g+1
            childObj.inputA=makeMove( currentElement.inputA,i)
            childObj.h = manhatten_heu(childObj.inputA,goal)
            childObj.f = childObj.g + childObj.h
            
            if (childObj.inputA == goal):
                      print ("Bingo...................!!!!!!!")
                      print ("Expanded Nodes")
                      printArr(visited)
                      del(current)
                      return
                  
            if_visited_index = _is_visited(childObj,visited,1)   
            if( if_visited_index != -1):
                    check_f_and_swap(visited,childObj,if_visited_index)
            else:
                current.append(childObj)
                #print(childObj.inputA)
            
            if_current_index = _is_visited(childObj,current, 0)
            if( if_current_index != -1):
                check_f_and_swap(current, childObj, if_current_index)
                     
            current = sorted(current, key=lambda p: p.f)
             
                 
   
def main():

   inputA = takeInput()
   p = PuzzleNode();
   p.eqate(inputA)
   p.printA(p.inputA) 
   A_Star(p)
   #print(manhatten_heu(p.inputA, goal))
main()    